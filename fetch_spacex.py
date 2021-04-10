import requests

from utils import download_image
from utils import fix_link


def fetch_spacex_last_launch(dir_name):
    response = requests.get('https://api.spacexdata.com/v3/launches/64')
    response.raise_for_status()
    for count, link in enumerate(response.json()['links']['flickr_images']):
        fixed_link = fix_link(link)
        download_image(fixed_link, f'{dir_name}/spacex{count}.jpg')