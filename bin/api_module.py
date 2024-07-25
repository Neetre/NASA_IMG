import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()
NASA_KEY = os.getenv("NASA_KEY")

def get_apod(count, download=False):
    data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}&count={count}")
    data = data.json()

    if download:
        # Ensure the directory exists
        os.makedirs("../data/APOD", exist_ok=True)
        for i in range(count):
            url = data[i]["url"]
            path = f"../data/APOD/apod_{time.time()}.jpg"
            download_image(url, path)
    
    return data


def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, "wb") as file:
            file.write(response.content)
            print("Image downloaded successfully.")
    else:
        print("Failed to download image.")


def search_asteroids():
    data = requests.get(f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={NASA_KEY}")
    data = data.json()
    print(data)


def create_plot():
    pass


def save_data():
    pass


def main():
    get_apod(4, True)
    search_asteroids()
    create_plot()
    save_data()


if __name__ == "__main__":
    main()