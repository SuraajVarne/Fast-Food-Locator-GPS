import requests

def get_coordinates_from_zip(zip_code, api_key=None):
    try:
        # Base URL for the Nominatim API
        base_url = 'https://nominatim.openstreetmap.org/search?'

        # Parameters for the API request
        params = {
            'format': 'json',
            'postalcode': zip_code,
        }

        # If you have an API key, include it in the headers
        if api_key:
            headers = {'User-Agent': 'YourApp', 'apikey': api_key}
        else:
            headers = {'User-Agent': 'YourApp'}

        # Send the API request
        response = requests.get(base_url, params=params, headers=headers)

        # Parse the JSON response
        data = response.json()

        # Extract latitude and longitude from the response (if available)
        if data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            return lat, lon
        else:
            return None, None
    except Exception as e:
        print("Error fetching coordinates:", e)
        return None, None
