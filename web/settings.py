from web.env_urls import factspace_url, pubsub_url
from os.path import dirname, join as pathjoin
from web.factspace import Factspace
from web.pubsub import PubSub

with open(pathjoin(dirname(__file__), 'home.html')) as f:
    HOME_HTML = f.read()
CHARSET = 'utf-8'

FACTSPACE = Factspace(factspace_url)
PUBSUB = PubSub(pubsub_url, 'combo')
