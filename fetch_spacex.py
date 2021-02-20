import os

import requests

from utils import resize_picture
from utils import download_image


def fetch_spacex_last_launch():
    os.makedirs("images", exist_ok=True)
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    for count, link in enumerate(response.json()['links']['flickr']['original']):
        download_image(link, f'images/spacex{count}.jpg')
        resize_picture(f'images/spacex{count}.jpg')
