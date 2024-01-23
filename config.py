import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')

# pingvin_chat_id = os.getenv('pingvin_chat_id')

ALLOWED_UPDATES = ['message, edited_message']
