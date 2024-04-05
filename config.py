import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')


postgres_host = os.getenv('POSTGRES_HOST')
postgres_port = os.getenv('POSTGRES_PORT')
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_db = os.getenv('POSTGRES_DB')


db_lite = os.getenv('DB_LITE')




# pingvin_chat_id = os.getenv('pingvin_chat_id')

# ALLOWED_UPDATES = ['message, edited_message']  испоьзовать если в app.py  allowed_updates=ALLOWED_UPDATES а не dp.resolve_used_update_types()
