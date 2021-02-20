import os
import shutil

from dotenv import load_dotenv
from instabot import Bot
from os import listdir


if __name__ == '__main__':

    load_dotenv()
    if os.path.exists('config'):
        shutil.rmtree('config')
    dir_name = 'images'
    bot = Bot()
    bot.login(username=os.getenv("INSTA_LOGIN"), password=os.getenv("INSTA_PASSWORD"))

    for number, photo_path in enumerate(listdir(dir_name)):
        bot.upload_photo(f'{dir_name}/{photo_path}', caption=f'Beautiful space photo number {number}')

    for item in os.listdir(dir_name):
        os.remove(f'{dir_name}/{item}')
