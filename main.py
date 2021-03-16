import os

import shutil

from dotenv import load_dotenv
from instabot import Bot
from os import listdir
from fetch_hubble import fetch_hubble_collection
from fetch_spacex import fetch_spacex_last_launch

__all__ = ['fetch_hubble_collection', 'fetch_spacex_last_launch']

if __name__ == '__main__':

    load_dotenv()
    dir_name = 'images'
    collection_name = 'holiday_cards'

    os.makedirs(dir_name, exist_ok=True)
    fetch_spacex_last_launch(dir_name)
    fetch_hubble_collection(collection_name, dir_name)

    if os.path.exists('config'):
        shutil.rmtree('config')
    bot = Bot()
    bot.login(username=os.getenv('INSTA_LOGIN'), password=os.getenv('INSTA_PASSWORD'))

    for number, photo_path in enumerate(listdir(dir_name)):
        bot.upload_photo(f'{dir_name}/{photo_path}', caption=f'Beautiful space photo number {number}')

    for item in os.listdir(dir_name):
        shutil.rmtree(f'{dir_name}/{item}')
