import os
import shutil

from dotenv import load_dotenv
from instabot import Bot
from os import listdir


load_dotenv()
if os.path.exists('config'):
    shutil.rmtree('config')
bot = Bot()
bot.login(username=os.getenv("INSTA_LOGIN"), password=os.getenv("INSTA_PASSWORD"))

for number, photo_path in enumerate(listdir('images')):
    bot.upload_photo(f'images/{photo_path}', caption=f'Beautiful space photo number {number}')

for item in os.listdir('images'):
    os.remove(f'images/{item}')
