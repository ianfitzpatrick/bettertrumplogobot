#!/usr/bin/env python

import tweepy, time, os, sys, yaml
from logo_gen import gen_logo


# Load twitter credentials for this bot from config file
BOTCRED_FILE = '%s/.twurlrc' % os.path.expanduser('~') 
with open(BOTCRED_FILE, 'r') as credfile:
	full_config = yaml.load(credfile)
	api_key = api_key = full_config['profiles']['bettertrumplogo'].keys()[0]
	bot_creds = full_config['profiles']['bettertrumplogo'][api_key]

CONSUMER_KEY = bot_creds['consumer_key']
CONSUMER_SECRET = bot_creds['consumer_secret']
ACCESS_KEY = bot_creds['token']
ACCESS_SECRET = bot_creds['secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# DEV
# BOTDIR = os.getcwd() + '/'

# PROD
BOTDIR = '/home/ianfitzpat/webapps/ianfitzpatrick_com/tplogobot/'

logo = gen_logo(BOTDIR)
api.update_with_media(logo)

