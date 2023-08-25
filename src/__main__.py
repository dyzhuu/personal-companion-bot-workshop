from bot import client, TOKEN
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    if not os.getenv('API_KEY'):
        raise Exception('API_KEY missing from .env')
    if not os.getenv('TOKEN'):
        raise Exception('TOKEN missing from .env')
    if not os.getenv('BOT_ID'):
        raise Exception('BOT_ID missing from .env')
    client.run(TOKEN)