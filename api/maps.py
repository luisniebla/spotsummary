# google maps api

import json

import firebase_admin
import geopy
import openai
import requests
from firebase_admin import credentials, firestore

import app
import embeddings
# print_recommendations_from_strings

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


@app.app.post('/search')
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
    indices = embeddings.print_recommendations_from_strings(all_reviews, 0, 3)
    print('Top recommendations')
    recommendations = []
    for i in range(1, 4):
        recommendations.append(places_indexes[indices[i]])
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
