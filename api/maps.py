# google maps api

import json
import geopy
import requests
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

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
        for review in data["result"]["reviews"]:
            embedding = openai.Embedding.create(
                input=review["text"], model="text-embedding-ada-002"
            )["data"][0]["embedding"]

            doc_ref = db.collection("locations").document(data["result"]["name"])
            doc_ref.set({"embedding": embedding})
            break
        return data

    else:
        return None


def search_places(address, radius=500, place_type="restaurant"):
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
        for item in data["results"]:
            get_place_info(item["place_id"])

        return data
    else:
        return None


search_places("15125 N Scottsdale Rd", 500, "restaurant")
