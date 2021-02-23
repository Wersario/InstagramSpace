import requests

from utils import create_directory
from utils import download_image
from utils import resize_picture


def fetch_spacex_last_launch(dir_name):
    create_directory(dir_name)
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    for count, link in enumerate(response.json()['links']['flickr']['original']):
        download_image(link, f'{dir_name}/spacex{count}.jpg', dir_name)
        resize_picture(f'{dir_name}/spacex{count}.jpg')
