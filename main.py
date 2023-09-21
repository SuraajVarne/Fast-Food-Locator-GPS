from flask import Flask, render_template, request
from geopy.distance import geodesic
import mysql.connector
from zip_to_coordinates import get_coordinates_from_zip  # Import the function

app = Flask(__name__)

# Database Configuration (Replace with your actual database configuration)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Flashboy1234$",
    database="fastfooddatadb"  # Change to your database name
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/find', methods=['POST'])
def find_nearest():
    try:
        user_zip = request.form['zip_code']
        
        # Print the user's ZIP code for debugging
        print(f'User ZIP Code: {user_zip}')
        
        user_latitude, user_longitude = get_coordinates_from_zip(user_zip)

        # Print the user's coordinates for debugging
        print(f'User Latitude: {user_latitude}, User Longitude: {user_longitude}')

        cursor.execute("SELECT name, address, latitude, longitude FROM fast_food_restaurants")
        places = cursor.fetchall()

        nearest_places = []

        for place in places:
            place_name, place_address, place_latitude, place_longitude = place
            distance = geodesic((user_latitude, user_longitude), (place_latitude, place_longitude)).miles
            nearest_places.append({
                'name': place_name,
                'address': place_address,
                'distance': round(distance, 2)
            })

        nearest_places.sort(key=lambda x: x['distance'])

        return render_template('output.html', data=nearest_places)
    
    except mysql.connector.Error as db_error:
        error_message = f"MySQL Error: {db_error}"
        return render_template('error.html', message=error_message)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', message=error_message)

@app.route('/test-database')
def test_database():
    try:
        cursor.execute("SELECT * FROM fast_food_restaurants LIMIT 5")
        data = cursor.fetchall()
        print(data)
        return "Database connection is working. Fetched data: " + str(data)
    except mysql.connector.Error as db_error:
        return "MySQL Error: " + str(db_error)

if __name__ == '__main__':
    app.run(debug=True)
