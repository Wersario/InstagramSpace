import os

import requests

from utils import get_link_extension
from utils import resize_picture
from utils import download_image


def fetch_hubble_id_photos(image_id, number):
    os.makedirs("images", exist_ok=True)
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    image = response.json()['image_files'][-1]
    download_image(f"https:{image['file_url']}", f"images/hubble{image_id}_{number}{get_link_extension(image['file_url'])}")
    resize_picture(f"images/hubble{image_id}_{number}{get_link_extension(image['file_url'])}")
