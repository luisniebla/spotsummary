# google maps api

import json
import geopy
import requests
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from embeddings import embedding_from_string, print_recommendations_from_strings

import openai


cred = credentials.ApplicationDefault()
app = firebase_admin.initialize_app(cred)
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


def get_current_location(address):
    location = geopy.geocoders.Nominatim(user_agent="spotsum").geocode(address)
    return [location.latitude, location.longitude]


#


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
    
# Find a better way to map reviews to places
def spot_summary(places, search):
    all_reviews = [search]
    places_indexes = [None]
    for place in places:
        places_indexes.extend([place["result"]["name"] for r in place['result']['reviews']])
        all_reviews.extend([r['text'] for r in place["result"]["reviews"]])
    print('al_reviews', all_reviews)
    indices = print_recommendations_from_strings(
       all_reviews, 0, 3
    )
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
