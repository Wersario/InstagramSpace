import os

import requests

import urllib.parse
from PIL import Image


def fix_link(url):
    url_with_spaces = urllib.parse.unquote(url, encoding='utf-8', errors='replace')
    fixed_link = urllib.parse.urlparse(url_with_spaces)[2]
    return fixed_link


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
    width = 1800
    length = 1800
    image.thumbnail((width, length))
    image.save(path)


def download_image(url, path):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)