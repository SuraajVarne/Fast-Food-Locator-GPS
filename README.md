# Fast Food Locator

## Introduction

Fast Food Locator is a web application that helps users find nearby fast food restaurants based on their ZIP code. It uses Python, Flask, and the Google Maps API to provide this functionality.

## Features

- Search for fast food restaurants by entering a ZIP code.
- View a list of fast food restaurants sorted by proximity.
- Click on a restaurant to see more details.

## Technologies Used

- Python
- Flask
- Google Maps API
- MySQL

## Getting Started

To run this project on your local machine, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/SuraajVarne/Fast-Food-Locator-GPS.git

   Navigate to the project directory:cd Fast-Food-Locator-GPS

   Install the required Python packages:pip install -r requirements.txt

## Config 

Set up the MySQL database:

Ensure that you have a MySQL database server running.

Import the database schema from database_dump.sql into your database.

Update the database configuration in main.py to match your setup:db = pymysql.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database_name"
) replace the API key in main.py with your own:gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')

## Usage 
Run the Flask application:python main.py
Access the web application in your web browser at http://localhost:5000.
