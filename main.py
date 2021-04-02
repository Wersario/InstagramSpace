import os
from os import listdir

import shutil
from dotenv import load_dotenv
from instabot import Bot

from fetch_hubble import fetch_hubble_collection
from fetch_spacex import fetch_spacex_last_launch
from utils import resize_picture
from utils import save_picture_as_jpg


if __name__ == '__main__':

    load_dotenv()
    dir_name = 'images'
    collection_name = 'spacecraft'

    os.makedirs(dir_name, exist_ok=True)
    fetch_spacex_last_launch(dir_name)
    fetch_hubble_collection(collection_name, dir_name)

    for photo in os.listdir(dir_name):
        save_picture_as_jpg(f'{dir_name}/{photo}')
        resize_picture(f'{dir_name}/{f"{os.path.splitext(photo)[0]}.jpg"}')

    if os.path.exists('config'):
        shutil.rmtree('config')
    bot = Bot()
    bot.login(username=os.getenv('INSTA_LOGIN'), password=os.getenv('INSTA_PASSWORD'))

    for number, photo_path in enumerate(listdir(dir_name)):
        bot.upload_photo(f'{dir_name}/{photo_path}', caption=f'Beautiful space photo number {number}')

    for item in os.listdir(dir_name):
        shutil.rmtree(f'{dir_name}/{item}')

