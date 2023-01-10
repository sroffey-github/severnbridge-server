from logging.handlers import RotatingFileHandler
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests, os, logging, datetime

load_dotenv()

URL = 'https://nationalhighways.co.uk/travel-updates/the-severn-bridges/'
LOG_PATH = f'{os.getcwd()}/logs/severnbridge.log'
TOKEN = os.getenv('TOKEN')

def log(msg):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(LOG_PATH, maxBytes=10000, backupCount=3)
    logger.addHandler(handler)
    logger.info(f'[{str(datetime.datetime.now())}] {msg}')

def notify(status):
    params = {'status':status}
    req = requests.post(f'https://maker.ifttt.com/trigger/severnbridge_status_change/json/with/key/{TOKEN}', data=params)
    log(f'Notification Sent [{str(req.status_code)}] - "{status}"')

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
titles = soup.findAll('div', {'class':'severn-crossing-status__heading'})

old_bridge = titles[0].text
new_bridge = titles[1].text

if not os.path.isfile(f'{os.getcwd()}/status'):
    with open('status', 'w') as f:
        f.write(old_bridge)
    if 'closed' in old_bridge.lower(): notify(old_bridge)
else:
    with open('status', 'r+') as f:
        old_status = f.read()
        if old_status != old_bridge:
            notify(old_bridge)
        else: pass