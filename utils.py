import os

import requests

from PIL import Image
from urllib.parse import urlparse


def create_directory(dir_name):
    os.makedirs(dir_name, exist_ok=True)


def get_link_extension(link):
    separated_link = os.path.splitext(urlparse(link).path)[1]
    return '.' + separated_link[-1]


def resize_picture(path):
    image = Image.open(path)
    image.thumbnail((1080, 1080))
    image.convert('RGB').save(f'{os.path.splitext(path)[0]}.jpg')
    if get_link_extension(path) != '.jpg':
        os.remove(path)


def download_image(url, path, dir_name):
    create_directory(dir_name)
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path, "wb") as file:
        file.write(response.content)
