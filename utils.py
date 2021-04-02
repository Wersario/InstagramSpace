import os

import requests

from PIL import Image


def save_picture_as_jpg(path):
    image = Image.open(path)
    image.convert('RGB').save(f'{os.path.splitext(path)[0]}.jpg')
    if get_link_extension(path) != '.jpg':
        os.remove(path)


def get_link_extension(link):
    _, extension = os.path.splitext(link)
    return extension


def resize_picture(path):
    image = Image.open(path)
    image.thumbnail((1080, 1080))
    image.save(path)


def download_image(url, path):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
