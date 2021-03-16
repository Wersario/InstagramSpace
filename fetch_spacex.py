import requests

from utils import download_image
from utils import resize_picture
from utils import save_picture_as_jpg

__all__ = ['download_image', 'resize_picture', 'save_picture_as_jpg']

def fetch_spacex_last_launch(dir_name):
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    for count, link in enumerate(response.json()['links']['flickr']['original']):
        download_image(link, f'{dir_name}/spacex{count}.jpg')
        resize_picture(save_picture_as_jpg(f'{dir_name}/spacex{count}.jpg'))
