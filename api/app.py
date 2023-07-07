from quart import Quart, jsonify, request
from quart_cors import cors

# google maps api

import json

import firebase_admin
import geopy
import openai
import pickle

import pandas as pd
import tiktoken
from openai.embeddings_utils import (
    chart_from_components,
    distances_from_embeddings,
    get_embedding,
    indices_of_nearest_neighbors_from_distances,
    tsne_components_from_embeddings,
)
import requests
from firebase_admin import credentials, firestore

app = Quart(__name__)
app.config.from_prefixed_env()
app = cors(app, allow_origin="http://localhost:3000")



@app.post('/chat')
async def chat():
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {
                "role": "assistant",
                "content": "The Los Angeles Dodgers won the World Series in 2020.",
            },
            {"role": "user", "content": "Where was it played?"},
        ],
    )
    # response = openai.Completion.create(
    # model="text-davinci-003",
    # prompt="Write a tagline for an ice cream shop."
    # )
    print(resp)
    return resp


@app.post("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "extra": True}


@app.get("/health")
async def health():
    return {"status": "ok"}


embedding_encoding = "cl100k_base"

# set path to embedding cache
embedding_cache_path = "api/data/recommendations_embeddings_cache.pkl"

EMBEDDING_MODEL = "text-embedding-ada-002"

@app.post("/embeddings")
async def embeddings():
    input_datapath = 'api/data/Reviews.csv'
    df = pd.read_csv(input_datapath, index_col=0)
    df = df[['Time', 'ProductId', 'UserId', 'Score', 'Summary', 'Text']]
    df = df.dropna()
    df["combined"] = (
        "Title: " + df.Summary.str.strip() + "; Content: " + df.Text.str.strip()
    )
    df.head(2)

    # subsample to 1k more recent reviews
    top_n = 10
    df = df.sort_values(by='Time', ascending=False).tail(top_n * 2)
    df.drop('Time', axis=1, inplace=True)

    encoding = tiktoken.get_encoding(embedding_encoding)

    # omit long reviews
    df['n_tokens'] = df.Text.apply(lambda x: len(encoding.encode(x)))
    df = df[df.n_tokens <= max_tokens].tail(top_n)

    # response = openai.Embedding.create(model=embedding_model, input=batch)
    df['embedding'] = df.combined.apply(lambda x: get_embeddings(x, embedding_model))

    df.to_csv('data/reviews_embeddings.csv')
    # return str(len(df))
    return str(df)

# load the cache if it exists, and save a copy to disk
try:
    embedding_cache = pd.read_pickle(embedding_cache_path)
except FileNotFoundError:
    embedding_cache = {}
with open(embedding_cache_path, "wb") as embedding_cache_file:
    pickle.dump(embedding_cache, embedding_cache_file)

encoding = tiktoken.get_encoding(embedding_encoding)


def remove_non_alnum(s):
    return "".join(c for c in s if c.isalnum() or c.isspace())


# define a function to retrieve embeddings from the cache if present, and otherwise request via the API
def embedding_from_string(
    string: str, model: str = EMBEDDING_MODEL, embedding_cache=embedding_cache
) -> list:
    """Return embedding of given string, using a cache to avoid recomputing."""
    # embedding_cache = {}
    parsed_str = remove_non_alnum(string)
    print(parsed_str)
    print(len(parsed_str))
    # n_tokens = len(encoding.encode(string))
    if (parsed_str, model) not in embedding_cache.keys():
        print("Getting new embedding")
        embedding_cache[(parsed_str, model)] = get_embedding(parsed_str, model)
        with open(embedding_cache_path, "wb") as embedding_cache_file:
            pickle.dump(embedding_cache, embedding_cache_file)
    return embedding_cache[(parsed_str, model)]


def print_recommendations_from_strings(
    strings: list[str],
    index_of_source_string: int,
    k_nearest_neighbors: int = 1,
    model=EMBEDDING_MODEL,
) -> list[int]:
    """Print out the k nearest neighbors of a given string."""
    # get embeddings for all strings
    embeddings = []
    for string in strings:
        embedding = embedding_from_string(string, model=model)
        if embedding:
            embeddings.append(embedding)
    # get the embedding of the source string
    query_embedding = embeddings[index_of_source_string]
    # get distances between the source embedding and other embeddings (function from embeddings_utils.py)
    distances = distances_from_embeddings(
        query_embedding, embeddings, distance_metric="cosine"
    )
    # get indices of nearest neighbors (function from embeddings_utils.py)
    indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(
        distances
    )

    print('indices_of_nearest_neighbors', indices_of_nearest_neighbors)

    # print out source string
    query_string = strings[index_of_source_string]
    print(f"Source string: {query_string}")
    # print out its k nearest neighbors
    k_counter = 0
    for i in indices_of_nearest_neighbors:
        # skip any strings that are identical matches to the starting string
        if query_string == strings[i]:
            continue
        # stop after printing out k articles
        if k_counter >= k_nearest_neighbors:
            break
        
        k_counter += 1

        # print out the similar strings and their distances
        print(
            f"""
        --- Recommendation #{k_counter} (nearest neighbor {k_counter} of {k_nearest_neighbors}) ---
        String: {strings[i]}
        Distance: {distances[i]:0.3f}"""
        )

    return indices_of_nearest_neighbors


cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
db = firestore.client()


# Use a service account.
# cred = credentials.Certificate('path/to/serviceAccount.json')

# app = firebase_admin.initialize_app()

# db = firestore.client()


from dotenv import dotenv_values, load_dotenv

load_dotenv()
config = dotenv_values(".env")
api_key = config["MAPS_API_KEY"]
openai.api_key = config["OPENAI_SECRET"]

from quart import Quart, jsonify, request


@app.post('/search')
async def search():
    data = await request.get_json()
    print('data', data)
    return jsonify(search_places(**data))
    # return search_places("15125 N Scottsdale Rd", 'Healthy food', 500, "restaurant")
    
def get_current_location(address):
    location = geopy.geocoders.Nominatim(user_agent="spotsum").geocode(address)
    return [location.latitude, location.longitude]


@app.route('/geo', methods=['GET'])
async def get_geo():
    address = request.args.get('address')
    print('address', address)
    return get_current_location(address)
    # return search_places("15125 N Scottsdale Rd", 'Healthy food', 500, "restaurant")


def get_place_info(place_id):
    # Define the Places API endpoint
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,reviews&key={api_key}"

    # Send a GET request to the API
    response = requests.get(url)

    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Load the JSON data from the response
        data = json.loads(response.text)
        return data

    else:
        return None


def remove_non_alnum(s):
    return "".join(c for c in s if c.isalnum() or c.isspace())


# Find a better way to map reviews to places
def spot_summary(places, search):
    all_reviews = [search]
    places_indexes = [None]
    for place in places:
        if place['result']['reviews']:
            for review in place['result']['reviews']:
                if review['text']:
                    places_indexes.append(place["result"]["name"])
                    all_reviews.append(review['text'])
    print('al_reviews', all_reviews)
    indices = print_recommendations_from_strings(all_reviews, 0, 3)
    print('Top recommendations')
    recommendations = []
    idx = 1
    while len(recommendations) < 4 or idx > len(indices):
        if places_indexes[indices[idx]] not in recommendations:
            recommendations.append(places_indexes[indices[idx]])
        idx += 1
    print(recommendations)
    return recommendations


def search_places(address, search, radius=500, place_type="restaurant"):
    location = get_current_location(address)
    location = ",".join([str(i) for i in location])
    # Define the Places API endpoint
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={place_type}&key={api_key}"

    # Send a GET request to the API
    response = requests.get(url)

    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Load the JSON data from the response
        data = json.loads(response.text)
        places = []
        for item in data["results"]:
            place_info = get_place_info(item["place_id"])
            places.append(place_info)
        spots = spot_summary(places, search)
        print('in', spots)
        return spots
    else:
        return None


# search_places("15125 N Scottsdale Rd", 'Healthy food', 500, "restaurant")


app.run()
