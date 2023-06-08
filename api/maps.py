# google maps api

import json
import geopy
import requests
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


cred = credentials.ApplicationDefault()
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Use a service account.
cred = credentials.Certificate('path/to/serviceAccount.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('location').document('alovelace')
doc_ref.set({
    'name': "Connolly's",
    'opening_hours': {'open_now': True},
})

from dotenv import dotenv_values, load_dotenv

load_dotenv()
config = dotenv_values('.env')
api_key = config['MAPS_API_KEY']

def get_current_location(address):
    location = geopy.geocoders.Nominatim(user_agent='spotsum').geocode(address)
    return [location.latitude, location.longitude]

# 

def get_place_info(api_key, place_id):
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


def search_places(address, radius=500, place_type='restaurant'):
    location = get_current_location(address)
    location = ','.join([str(i) for i in location])
    # Define the Places API endpoint
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={place_type}&key={api_key}"

    # Send a GET request to the API
    response = requests.get(url)

    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Load the JSON data from the response
        data = json.loads(response.text)
        print(data)
        return data
    else:
        return None


search_places('15125 N Scottsdale Rd', 500, 'restaurant')


# Mock response

example = {
    'html_attributions': [],
    'next_page_token': 'AZose0mzyNL3urrh6m-igC1tVkjCXjFh85TB6zMqTi8LwVIuTlgHJuOaBJ05IaG_Sdt8Mr0GIKZio0rOFwebRQzTYHBs9HbcrI466tEmHdiIlVUL21E_OQwbrz1I265pctZqzHwja9uZ0P86h60T_YmZbaV8vbDXh93ZdUg3q1X6yoe_8O4BppQUr2ptlhUzW1CRepOdEpDrNboYD_0HJClHTvp0JXz4d3V0zMdhNMS5NJ5D52DugF27rvBiJqrjf0Ph_QP_nftmH8SqsoT6rl0GRlYTnYtqfNGKz4N8KJ8_ZYKBIMAvrIDpe-1cfoSBKAC1u34eGEIRMVSPBMocU4J5Qsw1HPqXgsiiTdUkGNXyaO8sfed37G58hWosa8cEZhNetKLybhyJ9w7LAi_uCZ0ZJ-be7ipVn-ReRMVeDVwpm5sd-1qy1QH0ejb8OXZ2',
    'results': [
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7573681, 'lng': -73.9835798},
                'viewport': {
                    'northeast': {'lat': 40.7586323302915, 'lng': -73.9823113197085},
                    'southwest': {'lat': 40.75593436970851, 'lng': -73.98500928029151},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': "Connolly's",
            'opening_hours': {'open_now': True},
            'photos': [
                {
                    'height': 4032,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/105534001865754933642">Yamit Elfassi</a>'
                    ],
                    'photo_reference': 'AZose0nlz_NG9VkMgmPAq2LSs0L3eCa840VnWt-xCnrFH2b5hrv-tpLW4x33XzPsEC0-L326QH-K0hJSXraKmkO85IeaPKzvu_kysd47d9G1pa5apvXbCNq6qqdbEl9t9l0YEkZB8gvE4xqvxdoHZ5XWp1AOQquXrJLUCOthjjTTBx3j7DOO',
                    'width': 3024,
                }
            ],
            'place_id': 'ChIJAS6GeVVYwokRPfg8xt4nH-I',
            'plus_code': {
                'compound_code': 'Q248+WH New York, NY, USA',
                'global_code': '87G8Q248+WH',
            },
            'price_level': 2,
            'rating': 4.4,
            'reference': 'ChIJAS6GeVVYwokRPfg8xt4nH-I',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 3695,
            'vicinity': '121 West 45th Street, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.757498, 'lng': -73.986654},
                'viewport': {
                    'northeast': {'lat': 40.7589112802915, 'lng': -73.98532551970851},
                    'southwest': {'lat': 40.7562133197085, 'lng': -73.98802348029152},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': "Carmine's Italian Restaurant - Times Square",
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 1080,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/107712532148225729261">Carmine&#39;s Italian Restaurant - Times Square</a>'
                    ],
                    'photo_reference': 'AZose0ncbNaFQIF2_Sl2JJ0AxUOHocDfkOsNRbDkZmUmVQRhV3yCJPLZhuN44yojnUMeZxQrKx1La_-6sZ0isYTsJ45Gy3WcxdiTFtccpwQSNN9On-4_2fQnpEwR6G5fiNtS1B2hXEvjkvtenuyV8zFjPqHy1s200xBaJ1dyPaEX-oMaGKO2',
                    'width': 1920,
                }
            ],
            'place_id': 'ChIJR9So-lRYwokRX1xEjA0rChA',
            'plus_code': {
                'compound_code': 'Q247+X8 New York, NY, USA',
                'global_code': '87G8Q247+X8',
            },
            'price_level': 2,
            'rating': 4.5,
            'reference': 'ChIJR9So-lRYwokRX1xEjA0rChA',
            'scope': 'GOOGLE',
            'types': ['restaurant', 'food', 'point_of_interest', 'establishment'],
            'user_ratings_total': 13940,
            'vicinity': '200 West 44th Street, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.75937589999999, 'lng': -73.98532519999999},
                'viewport': {
                    'northeast': {'lat': 40.76078098029149, 'lng': -73.9839495697085},
                    'southwest': {'lat': 40.75808301970849, 'lng': -73.9866475302915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Blue Fin',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 1192,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/113254462009664387662">Blue Fin</a>'
                    ],
                    'photo_reference': 'AZose0nQP84ofJSccjVusdLnvYDeEIpu2Vn2iVduPTY9qEDt8y8S0-mnzICNseX-cCfQtP0WHg5dkc4v-B_id1YFU6zKhR4PvvC83qoI3cRoUkaKj3tpmSfjaH1OE-rzN4J80s43l8cCPxyee3snhm5sFU_9eXbNRe_J9vwFhrasS9rUo4cS',
                    'width': 2119,
                }
            ],
            'place_id': 'ChIJzz-PyFVYwokRwp5z0KduYls',
            'plus_code': {
                'compound_code': 'Q257+QV New York, NY, USA',
                'global_code': '87G8Q257+QV',
            },
            'price_level': 3,
            'rating': 4.3,
            'reference': 'ChIJzz-PyFVYwokRwp5z0KduYls',
            'scope': 'GOOGLE',
            'types': ['restaurant', 'food', 'point_of_interest', 'establishment'],
            'user_ratings_total': 880,
            'vicinity': '1567 Broadway, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7584105, 'lng': -73.98921899999999},
                'viewport': {
                    'northeast': {'lat': 40.75971073029149, 'lng': -73.98776301970848},
                    'southwest': {'lat': 40.7570127697085, 'lng': -73.9904609802915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Shake Shack Theater District',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 2592,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/109780063811304933686">Shake Shack Theater District</a>'
                    ],
                    'photo_reference': 'AZose0nf0pG3528778fJfk9xEywIR_DLJWNJ6pQMf-Re9P7o5xpSLZG4zK0DPr_vsTQxM6fvkeGinTFRqSO76NaZ3qpxzcoYC714uGh1sOpJIFQv3cMWy7SpQpi0SMcqiydfnwQQm_fdhpfkClEY01TlYOhnwXTda0m_Ws2BtTV4sy6yWknP',
                    'width': 3888,
                }
            ],
            'place_id': 'ChIJhXAgf1NYwokRBzdqc2TRX_I',
            'plus_code': {
                'compound_code': 'Q256+98 New York, NY, USA',
                'global_code': '87G8Q256+98',
            },
            'price_level': 2,
            'rating': 4.4,
            'reference': 'ChIJhXAgf1NYwokRBzdqc2TRX_I',
            'scope': 'GOOGLE',
            'types': [
                'meal_delivery',
                'meal_takeaway',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 13074,
            'vicinity': '691 8th Avenue, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7594099, 'lng': -73.98222},
                'viewport': {
                    'northeast': {'lat': 40.76066863029151, 'lng': -73.98071121970848},
                    'southwest': {'lat': 40.75797066970851, 'lng': -73.98340918029149},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': "Del Frisco's Double Eagle Steakhouse",
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 532,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/113759600496570974304">Del Frisco&#39;s Double Eagle Steakhouse</a>'
                    ],
                    'photo_reference': 'AZose0k2R2Ye6A69Fo98Pg1bubn5frdFmt-P9PX52F1WrKCezXKCxzLVXza46pK37zLfz68m0lpHEVRs13nFX1vxlW4yJUk-0Ym0oNzz4HcT4b55JjLjnZJlOMQ_pZwKsPcRm-eRrBUUaEIspI9bt8LF6qzfGwvH-6LiRll1LV4JQyeqIH-a',
                    'width': 800,
                }
            ],
            'place_id': 'ChIJE1bnSP9YwokRDK7Zxnt23gE',
            'plus_code': {
                'compound_code': 'Q259+Q4 New York, NY, USA',
                'global_code': '87G8Q259+Q4',
            },
            'price_level': 4,
            'rating': 4.5,
            'reference': 'ChIJE1bnSP9YwokRDK7Zxnt23gE',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 4711,
            'vicinity': '1221 6th Avenue, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7570352, 'lng': -73.9866112},
                'viewport': {
                    'northeast': {'lat': 40.75830483029151, 'lng': -73.9851221697085},
                    'southwest': {'lat': 40.75560686970851, 'lng': -73.98782013029151},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Hard Rock Cafe',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 1152,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/112904588745782757774">Hard Rock Cafe</a>'
                    ],
                    'photo_reference': 'AZose0kKk9ME1rQH1PjeEhAFTVqXsRFoS4iBuDhvEuuhtWiclBpbuwHqLO3cs5HqN8fj6sIm9DhSgKxOw1mz3ODGEqDTbh596M6B6d3WktCjQXpf-4T-iaAONDJyZBi8Rb2-RzibFDNlgmiHl_Jo617rZfXWqb3RA-SXbpeHHQoygCH5RH1K',
                    'width': 2048,
                }
            ],
            'place_id': 'ChIJh3tl5lRYwokRtY1QuaZADu0',
            'plus_code': {
                'compound_code': 'Q247+R9 New York, NY, USA',
                'global_code': '87G8Q247+R9',
            },
            'price_level': 2,
            'rating': 4.4,
            'reference': 'ChIJh3tl5lRYwokRtY1QuaZADu0',
            'scope': 'GOOGLE',
            'types': ['restaurant', 'food', 'point_of_interest', 'establishment'],
            'user_ratings_total': 20506,
            'vicinity': '1501 Broadway, New York',
        },
        {
            'business_status': 'CLOSED_TEMPORARILY',
            'geometry': {
                'location': {'lat': 40.7579436, 'lng': -73.9851237},
                'viewport': {
                    'northeast': {'lat': 40.7592185302915, 'lng': -73.98379776970849},
                    'southwest': {'lat': 40.7565205697085, 'lng': -73.9864957302915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Planet Hollywood',
            'permanently_closed': True,
            'photos': [
                {
                    'height': 471,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/116155653431661068032">Planet Hollywood</a>'
                    ],
                    'photo_reference': 'AZose0lMRVZ2Uvttne565SsWMszTxYENv3uAHQJPRigLijiXP4SjEVir39tVA327-aQ4SXDDnuEwz55EUsZ6IrYK8-cpdvhW_57JM9OCo1ES3_qgMkakqdHG8lPrjwz1uq9JZQkBnPNoBDCw_8nNhT3VUkOoVVBfyco2EKv5xVBK6R5WswDS',
                    'width': 837,
                }
            ],
            'place_id': 'ChIJf2_0qFVYwokRu7dmhsHUrpo',
            'plus_code': {
                'compound_code': 'Q257+5X New York, NY, USA',
                'global_code': '87G8Q257+5X',
            },
            'price_level': 2,
            'rating': 3.9,
            'reference': 'ChIJf2_0qFVYwokRu7dmhsHUrpo',
            'scope': 'GOOGLE',
            'types': ['restaurant', 'food', 'point_of_interest', 'establishment'],
            'user_ratings_total': 3683,
            'vicinity': '1540 Broadway, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.759333, 'lng': -73.984667},
                'viewport': {
                    'northeast': {'lat': 40.7606842802915, 'lng': -73.98341066970849},
                    'southwest': {'lat': 40.7579863197085, 'lng': -73.9861086302915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Olive Garden Italian Restaurant',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 9000,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/113417286947647578699">Ale Ramirez</a>'
                    ],
                    'photo_reference': 'AZose0kZaLbdtQzpW-4qk_Uj0W1FgMLFtICLqHVxLeehhTomskKzv99PPLL4yAeAAw7UoBaAbkiFwMwUiTOIG0ET7HeBQF0dTwTN6r8DD_YBuevC7DsUOwz838UAFM6Wi9UeHhstgKSL2yz4GnM3793iSOYwE5cg3YB8iQCkgku-WJ9uGoyb',
                    'width': 12000,
                }
            ],
            'place_id': 'ChIJM3wn3VVYwokRvu2kbqBKUsM',
            'plus_code': {
                'compound_code': 'Q258+P4 New York, NY, USA',
                'global_code': '87G8Q258+P4',
            },
            'price_level': 2,
            'rating': 4.1,
            'reference': 'ChIJM3wn3VVYwokRvu2kbqBKUsM',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'meal_takeaway',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 5885,
            'vicinity': '2 Times Square, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7587252, 'lng': -73.98622},
                'viewport': {
                    'northeast': {'lat': 40.7600142302915, 'lng': -73.9852151697085},
                    'southwest': {'lat': 40.7573162697085, 'lng': -73.9879131302915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'The View Restaurant & Lounge',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 2232,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/113664808882100176059">The View Restaurant &amp; Lounge</a>'
                    ],
                    'photo_reference': 'AZose0k4q_W6Pg9z60XcdkdXt-XBHTpOBcNv8SFtzbWmKGfAGkoXbcWUXTVKo_dmwq6gH2zFUQsnxXCWnPkbQl4ZpOEPLpSEI8vUi5-AWHt2k-jDny--dFKsijayRcvY2sqb31JCA4J_BPV_EpjXqQ-LXQLgZkFDVCdBQa8F0FUJgtwaugMc',
                    'width': 3144,
                }
            ],
            'place_id': 'ChIJiVXoAFVYwokRaaIaoxYZBeQ',
            'plus_code': {
                'compound_code': 'Q257+FG New York, NY, USA',
                'global_code': '87G8Q257+FG',
            },
            'price_level': 4,
            'rating': 4.2,
            'reference': 'ChIJiVXoAFVYwokRaaIaoxYZBeQ',
            'scope': 'GOOGLE',
            'types': [
                'night_club',
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 3087,
            'vicinity': '1535 Broadway, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7556764, 'lng': -73.9875914},
                'viewport': {
                    'northeast': {'lat': 40.7569093802915, 'lng': -73.98628266970849},
                    'southwest': {'lat': 40.7542114197085, 'lng': -73.98898063029151},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Red Lobster',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 3072,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/100872439113709270772">Ishaan Binoy</a>'
                    ],
                    'photo_reference': 'AZose0knrPZqXcUhKPoYkyqZ7rYfaHzE19kz8xk6VjUDSl0HJVVGr9SYe6tM8zVEM_jJ58cX9g2qHxoPVcPfb56I4_sUORtxgIFQksdEYjP4TPtmyJ5fAdwr-xc_xL175Lb-6D7E6UtrD_eUZUdWybSsNQ-TVRd2eO0Y3gjJLDG6nDRgwRGg',
                    'width': 4096,
                }
            ],
            'place_id': 'ChIJc4euylRYwokRnweuR3UzKYI',
            'plus_code': {
                'compound_code': 'Q246+7X New York, NY, USA',
                'global_code': '87G8Q246+7X',
            },
            'price_level': 2,
            'rating': 4.2,
            'reference': 'ChIJc4euylRYwokRnweuR3UzKYI',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 7933,
            'vicinity': '5 Times Square, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.756536, 'lng': -73.98863399999999},
                'viewport': {
                    'northeast': {'lat': 40.7579748802915, 'lng': -73.9872335697085},
                    'southwest': {'lat': 40.7552769197085, 'lng': -73.9899315302915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': "Dave & Buster's New York City - Times Square",
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 2584,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/114858730109210687523">Dave &amp; Buster&#39;s New York City - Times Square</a>'
                    ],
                    'photo_reference': 'AZose0kh-y03PBDscKpGuSFnMNp9Go5OEpsVg0NDOMTloscPLawzo1kwlWV0X6t8rHemIbIetVQa0879odgYnmqNiqPy0u1Zi6urrKjT_qq0_4wOHpxRSmF_S-n8tlJF7sZRhJFvbnvaPopdtgImo_tFw4bfbY24mmbf8mVYu0jer6NF7pE3',
                    'width': 3828,
                }
            ],
            'place_id': 'ChIJ8VOfr1RYwokRdgk5I-NvtfE',
            'plus_code': {
                'compound_code': 'Q246+JG New York, NY, USA',
                'global_code': '87G8Q246+JG',
            },
            'price_level': 2,
            'rating': 4.2,
            'reference': 'ChIJ8VOfr1RYwokRdgk5I-NvtfE',
            'scope': 'GOOGLE',
            'types': [
                'restaurant',
                'bar',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 7912,
            'vicinity': '234 West 42nd Street 3rd Floor, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.756511, 'lng': -73.984641},
                'viewport': {
                    'northeast': {'lat': 40.7579604802915, 'lng': -73.9831899197085},
                    'southwest': {'lat': 40.7552625197085, 'lng': -73.98588788029151},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'The Lambs Club',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 4032,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/108931365027554085961">Douglas Allen</a>'
                    ],
                    'photo_reference': 'AZose0ksxWutRy8dPd0R1nwctL2Lii3D7j1z2NK2PKQxoy90zc0ZDZFTmTVlnzn0rM9x7pa79QhVcbN36Ya25zk2hqGofZsnnjcNoqAAngfyN5iyUHe50e3C72J2D8ZiG6vi4ND-DOtmGG8xgTbJlQqhyrGWMm-bLQhQNcQ2bG1D4s3dxkwN',
                    'width': 3024,
                }
            ],
            'place_id': 'ChIJu0soFVVYwokRArPqt2VGdJs',
            'plus_code': {
                'compound_code': 'Q248+J4 New York, NY, USA',
                'global_code': '87G8Q248+J4',
            },
            'price_level': 3,
            'rating': 4.4,
            'reference': 'ChIJu0soFVVYwokRArPqt2VGdJs',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 643,
            'vicinity': '132 West 44th Street, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7599972, 'lng': -73.9867421},
                'viewport': {
                    'northeast': {'lat': 40.76138308029149, 'lng': -73.98534861970849},
                    'southwest': {'lat': 40.7586851197085, 'lng': -73.9880465802915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Trattoria Trecolori',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 3456,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/111178485652298890471">Trattoria Trecolori</a>'
                    ],
                    'photo_reference': 'AZose0msgaTFFf8OVMATnQ2Sj2PPQaus9AkngKnloU0atpSF9XWUWWbl-gMSMoVoxTbb_bCb9OpJU0GbobQok0OLAioF-c_9tWhnn_dp-drDIDohzPfZazL_kkqrGjC46HtvkNoSVCtyaFnh2gcepmqRUl2y-btzrEjB_e4QgeBPjETc-rmQ',
                    'width': 5184,
                }
            ],
            'place_id': 'ChIJYepwLVRYwokRsvXclA3XFqo',
            'plus_code': {
                'compound_code': 'Q257+X8 New York, NY, USA',
                'global_code': '87G8Q257+X8',
            },
            'price_level': 2,
            'rating': 4.4,
            'reference': 'ChIJYepwLVRYwokRsvXclA3XFqo',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 2203,
            'vicinity': '254 West 47th Street, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7576912, 'lng': -73.9885419},
                'viewport': {
                    'northeast': {'lat': 40.7590031302915, 'lng': -73.9872203197085},
                    'southwest': {'lat': 40.7563051697085, 'lng': -73.9899182802915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Green Symphony',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 2832,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/110491085564248044617">Sarah G. Harris</a>'
                    ],
                    'photo_reference': 'AZose0nPKBLb8HjPnaC4kim4GKRfs7efVD0U7RLS4CfAUS2msT31ik-LcKP8YauJB7eRpt4FbI5HTPzSqawMnkTO9fXNAOEp5OzPWUQ4gxVMGRdbe6Vs306Q2A282uz92RzGfVuaVA1Lf8H5m6sxaVAGEWRahvARvbrYhLO2deC0hy9hMrzL',
                    'width': 3777,
                }
            ],
            'place_id': 'ChIJ1VR_m1RYwokRGqUM_C_WSZc',
            'plus_code': {
                'compound_code': 'Q256+3H New York, NY, USA',
                'global_code': '87G8Q256+3H',
            },
            'price_level': 1,
            'rating': 4.5,
            'reference': 'ChIJ1VR_m1RYwokRGqUM_C_WSZc',
            'scope': 'GOOGLE',
            'types': ['restaurant', 'food', 'point_of_interest', 'establishment'],
            'user_ratings_total': 254,
            'vicinity': '255 West 43rd Street, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7583364, 'lng': -73.9841591},
                'viewport': {
                    'northeast': {'lat': 40.75963908029149, 'lng': -73.98285936970849},
                    'southwest': {'lat': 40.75694111970849, 'lng': -73.9855573302915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Havana Central Times Square',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 955,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/107785244119404185612">Havana Central Times Square</a>'
                    ],
                    'photo_reference': 'AZose0nr4kL_IE3cKYhIX3GF82JOGPyPIP64hnWFyVjzR-JDyVgVRAEasnSocmNj91RhBPC4docUOeFT6nUucq1ZbVIeCrQ89uJHv0FaN6KnJB_flhWljQZDcyAk9kCvL8VvhaM5ckkG7IcCcBD0x8sXn26-C2cn8UVtLiJZfK7EpPtM_zLs',
                    'width': 1695,
                }
            ],
            'place_id': 'ChIJy0KKmVVYwokRyab_FcJzFA0',
            'plus_code': {
                'compound_code': 'Q258+88 New York, NY, USA',
                'global_code': '87G8Q258+88',
            },
            'price_level': 2,
            'rating': 4.3,
            'reference': 'ChIJy0KKmVVYwokRyab_FcJzFA0',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 5330,
            'vicinity': '151 West 46th Street, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7590167, 'lng': -73.9896861},
                'viewport': {
                    'northeast': {'lat': 40.7603276302915, 'lng': -73.9883925197085},
                    'southwest': {'lat': 40.7576296697085, 'lng': -73.9910904802915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet',
            'name': 'Birdland Jazz Club',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 4000,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/100743246936155750382">Matt zebroski</a>'
                    ],
                    'photo_reference': 'AZose0mQdEHssns8KfqRTR7chY2rTp1svRm-uSRmWz0YojHvKXHCQgzbc1uCYIMyuCI4smoYNnqr9lC5s709WzR0N2QiKarH7L2ibpVIxa1bcZc87rX3T4MtvTvMi9w5DxlPtIl0YmO4XxyOnuJx-IqnhEtZiflSyQOOrD-UffQfbs8U6mUf',
                    'width': 3000,
                }
            ],
            'place_id': 'ChIJdc9EhVNYwokR-naSYfm_Urc',
            'plus_code': {
                'compound_code': 'Q256+J4 New York, NY, USA',
                'global_code': '87G8Q256+J4',
            },
            'price_level': 3,
            'rating': 4.7,
            'reference': 'ChIJdc9EhVNYwokR-naSYfm_Urc',
            'scope': 'GOOGLE',
            'types': [
                'night_club',
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 2932,
            'vicinity': '315 West 44th Street #5402, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.75976409999999, 'lng': -73.9823074},
                'viewport': {
                    'northeast': {'lat': 40.7611526802915, 'lng': -73.98091666970849},
                    'southwest': {'lat': 40.7584547197085, 'lng': -73.98361463029151},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Oceana',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 1365,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/100507182521450733936">Oceana</a>'
                    ],
                    'photo_reference': 'AZose0l1Xca5TyWn7ogseHO4jZEX-Wd7VIuwrgniMq8Vm5FuAjn3Gc0d0zH4u2m9-Gqy-nyxUgF1iaUVXShhrSPTeUiB_baZTIMyhuAMIGxbiFnvWDXooezzU6kr3th_7GILfDnGDphnrSXrCQtkRyTpWpN6DiEoEofuIqdljSH6taRs-caO',
                    'width': 2048,
                }
            ],
            'place_id': 'ChIJ34SOS_9YwokR7vXpNdS9tZ8',
            'plus_code': {
                'compound_code': 'Q259+W3 New York, NY, USA',
                'global_code': '87G8Q259+W3',
            },
            'price_level': 4,
            'rating': 4.5,
            'reference': 'ChIJ34SOS_9YwokR7vXpNdS9tZ8',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 1115,
            'vicinity': '120 West 49th Street, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.76088499999999, 'lng': -73.9863},
                'viewport': {
                    'northeast': {'lat': 40.7621702802915, 'lng': -73.98501081970849},
                    'southwest': {'lat': 40.7594723197085, 'lng': -73.98770878029151},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'La Masseria NY',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 2848,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/106721489930317216771">La Masseria NY</a>'
                    ],
                    'photo_reference': 'AZose0knBX9EouyYWpqgIu2IGPtpOynxZd2bWghyogDgmA0rJq9O-ZbN2BscAkvISeVlZaM2XyhTqPfsEdd1WkVb6pG55WGGbBaVTOrOzURlHtQqD_5Ef6dxxai0nOgpwHkqfrW0q-wT07EXoOR4imfD2fRcXkZM8DwlLE1vkWiTiZfT1HNI',
                    'width': 4272,
                }
            ],
            'place_id': 'ChIJjfIegVZYwokRyqdwvzBC27s',
            'plus_code': {
                'compound_code': 'Q267+9F New York, NY, USA',
                'global_code': '87G8Q267+9F',
            },
            'price_level': 3,
            'rating': 4.4,
            'reference': 'ChIJjfIegVZYwokRyqdwvzBC27s',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 1072,
            'vicinity': '235 West 48th Street, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7572071, 'lng': -73.9863737},
                'viewport': {
                    'northeast': {'lat': 40.7586496802915, 'lng': -73.9848875197085},
                    'southwest': {'lat': 40.7559517197085, 'lng': -73.9875854802915},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Bubba Gump Shrimp Co.',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 9000,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/113417286947647578699">Ale Ramirez</a>'
                    ],
                    'photo_reference': 'AZose0lpT6JIyKgmomSO3FlBjGO_bggXN1g0PZbtrQewhVtWhplFyJF6MlXdUx_MNs4ELNgcF3isF-7djTSPtlds9oLBNxTSfW2ibvh2AXWx6J4e3zJ7nXzRMBRriVKU9bobJpOBjtdRCIlvlAAAmzEkL-VJbks5tGZyHJ71LQknTE7HzSCm',
                    'width': 12000,
                }
            ],
            'place_id': 'ChIJh3tl5lRYwokRzzrdicL9JxY',
            'plus_code': {
                'compound_code': 'Q247+VF New York, NY, USA',
                'global_code': '87G8Q247+VF',
            },
            'price_level': 2,
            'rating': 4.3,
            'reference': 'ChIJh3tl5lRYwokRzzrdicL9JxY',
            'scope': 'GOOGLE',
            'types': ['restaurant', 'food', 'point_of_interest', 'establishment'],
            'user_ratings_total': 12196,
            'vicinity': '1501 Broadway, New York',
        },
        {
            'business_status': 'OPERATIONAL',
            'geometry': {
                'location': {'lat': 40.7570239, 'lng': -73.98866260000001},
                'viewport': {
                    'northeast': {'lat': 40.7582828802915, 'lng': -73.9874210697085},
                    'southwest': {'lat': 40.7555849197085, 'lng': -73.99011903029151},
                },
            },
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png',
            'icon_background_color': '#FF9E67',
            'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet',
            'name': 'Dallas BBQ Times Square',
            'opening_hours': {'open_now': False},
            'photos': [
                {
                    'height': 5184,
                    'html_attributions': [
                        '<a href="https://maps.google.com/maps/contrib/100407682243951753745">Dallas BBQ Times Square</a>'
                    ],
                    'photo_reference': 'AZose0lI188Z8-zXO0xaFnKbhI89A_e5Zjx89OQj_gRzeaxbmcpuIzAp3O8o2uXX9ygciNciLWpChayca1bQsXSJHYgaPZIoXQDAfDssOd42gZtGQSmkaHGHo9o_DUhBW4cjHc1F0_2VjX88F6RC6RhwkbUaOu9MJLEFyfzq9-knZebqc59a',
                    'width': 3456,
                }
            ],
            'place_id': 'ChIJn5a71FRYwokRGB7grb84QaI',
            'plus_code': {
                'compound_code': 'Q246+RG New York, NY, USA',
                'global_code': '87G8Q246+RG',
            },
            'price_level': 2,
            'rating': 4.2,
            'reference': 'ChIJn5a71FRYwokRGB7grb84QaI',
            'scope': 'GOOGLE',
            'types': [
                'bar',
                'restaurant',
                'food',
                'point_of_interest',
                'establishment',
            ],
            'user_ratings_total': 12536,
            'vicinity': '241 West 42nd Street, New York',
        },
    ],
    'status': 'OK',
}
