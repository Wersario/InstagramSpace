import requests

from utils import create_directory
from utils import download_image
from utils import get_link_extension
from utils import resize_picture


def fetch_hubble_id_photo(image_id, number, dir_name):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    image = response.json()['image_files'][-1]
    download_image(f"https:{image['file_url']}", f"{dir_name}/hubble{image_id}_{number}{get_link_extension(image['file_url'])}", dir_name)
    resize_picture(f"{dir_name}/hubble{image_id}_{number}{get_link_extension(image['file_url'])}")


def fetch_hubble_collection(collection_name, dir_name):
    create_directory(dir_name)
    url = f'http://hubblesite.org/api/v3/image/{collection_name}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    for number, image_id in enumerate(response.json()['id']):
        fetch_hubble_id_photo(image_id, number, dir_name)
