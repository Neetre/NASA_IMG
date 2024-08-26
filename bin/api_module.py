import os
import requests
from dotenv import load_dotenv
import time
import json
import csv
import matplotlib.pyplot as plt
from PIL import Image

load_dotenv()
NASA_KEY = os.getenv("NASA_KEY")

def get_apod(count, download=False):
    try:
        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}&count={count}")
        response.raise_for_status()
        data = response.json()

        if download:
            os.makedirs("../data/APOD", exist_ok=True)
            for i in range(count):
                url = data[i]["url"]
                path = f"../data/APOD/apod_{time.time()}.jpg"
                download_image(url, path)
        
        return data, Image.open(path)
    except requests.RequestException as e:
        print(f"Error fetching APOD data: {e}")
        return None

def download_image(url, path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(path, "wb") as file:
            file.write(response.content)
            print("Image downloaded successfully.")
    except requests.RequestException as e:
        print(f"Failed to download image: {e}")

def search_asteroids():
    try:
        response = requests.get(f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={NASA_KEY}")
        response.raise_for_status()
        data = response.json()
        print(data)
        asteroid_id = data["near_earth_objects"][0]["id"]
        
        response = requests.get(f"https://api.nasa.gov/neo/rest/v1/neo/{asteroid_id}?api_key={NASA_KEY}")
        response.raise_for_status()
        data = response.json()
        print(data)
        return data
    except requests.RequestException as e:
        print(f"Error fetching asteroid data: {e}")
        return None

def create_plot(data):
    if not data:
        print("No data available for plotting.")
        return

    dates = [item['date'] for item in data]
    titles = [item['title'] for item in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, titles, marker='o')
    plt.title("APOD Titles Over Time")
    plt.xlabel("Date")
    plt.ylabel("Title")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def save_data(data, file_format='json'):
    if not data:
        print("No data available to save.")
        return

    os.makedirs("../data", exist_ok=True)
    file_path = f"../data/apod_data.{file_format}"
    
    try:
        if file_format == 'json':
            with open(file_path, "w") as file:
                json.dump(data, file)
        elif file_format == 'csv':
            with open(file_path, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data[0].keys())  # Write the header
                for item in data:
                    writer.writerow(item.values())
        print(f"Data saved successfully to {file_path}.")
    except IOError as e:
        print(f"Failed to save data: {e}")

def search_mars_rover_photos(rover_name, sol=1000):
    try:
        response = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_name}/photos?sol={sol}&api_key={NASA_KEY}")
        response.raise_for_status()
        data = response.json()
        print(data)
        return data
    except requests.RequestException as e:
        print(f"Error fetching Mars Rover photos: {e}")
        return None

def main():
    apod_data = get_apod(1, False)
    asteroid_data = search_asteroids()
    mars_rover_data = search_mars_rover_photos('curiosity')

    if apod_data:
        create_plot(apod_data)
        save_data(apod_data, 'json')
        save_data(apod_data, 'csv')

if __name__ == "__main__":
    main()
