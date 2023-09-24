# Fast Food Locator

## Introduction

Fast Food Locator is a web application that helps users find nearby fast food restaurants based on their ZIP code. It utilizes Python, Flask, and the Google Maps API to provide this functionality. This project demonstrates my skills and passion for web development, data analysis, and creating practical solutions.

## Features

### Key Features

- **ZIP Code-Based Search**: Users can search for fast food restaurants by entering a ZIP code.
- **Proximity Sorting**: Search results are sorted by proximity to the user's entered ZIP code.
- **Detailed Restaurant Information**: Users can access detailed information about each restaurant by clicking on its name in the results list, including the restaurant's address.

## Technology Stack

- **Python and Flask**: The backend of the application is developed using Python and the Flask web framework, allowing for seamless route handling and HTML template rendering.

- **Google Maps API**: For geolocation and distance calculations, the Google Maps API is integrated to determine the proximity of restaurants to the user's input ZIP code.

- **MySQL Database**: The project utilizes a MySQL database to store and manage restaurant data, including name, address, and geographical coordinates.

## Getting Started

To run this project on your local machine, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/SuraajVarne/Fast-Food-Locator-GPS.git
   
## Navigate to the project directory

cd Fast-Food-Locator-GPS
pip install -r requirements.txt

## Database Setup

Ensure that you have a MySQL database server running.

Import the database schema from database_dump.sql into your database.

Update the database configuration in main.py to match your setup:
db = pymysql.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database_name"
)
Remember to replace the API key in main.py with your own Google Maps API key to get results with accurate distance calculations. gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')


## Usage

Run-python main.py
Access the web application in your web browser at http://localhost:5000

## Conclusion
Fast Food Locator represents my dedication to web development, data integration, and creating practical solutions for everyday challenges. I hope this project demonstrates my skills and commitment to building innovative and user-friendly applications.

