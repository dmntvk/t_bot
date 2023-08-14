import os
from dotenv import load_dotenv
from pyqiwip2p import QiwiP2P

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

p2p = QiwiP2P(auth_key=os.getenv('QiwiToken'))

admin_id = [
    331224038
]

ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASS = str(os.getenv('PGPASS'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASS}@{ip}/{DATABASE}'

Chanel = [['Основной канал', '-1001871426229', 'https://t.me/justttdoitbot']]

