import requests

from utils import download_image
from utils import get_link_extension


def fetch_hubble_id_photo(image_id, number, dir_name):
    url = f'https://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    image = response.json()['image_files'][-1]
    download_image(f"https:{image['file_url']}", f"{dir_name}/hubble{image_id}_{number}{get_link_extension(image['file_url'])}")
    print(f"https:{image['file_url']}", 'downloaded')


def fetch_hubble_collection(collection_name, dir_name):
    url = f'https://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    for number, image_id in enumerate(response.json()):
        fetch_hubble_id_photo(image_id['id'], number, dir_name)
