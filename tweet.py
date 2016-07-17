#!/usr/bin/env python

import tweepy, time, sys, os
from logo_gen import gen_logo


# enter the corresponding information from your Twitter application:
CONSUMER_KEY = '***REMOVED***'
CONSUMER_SECRET = '***REMOVED***'
ACCESS_KEY = '***REMOVED***'
ACCESS_SECRET = '***REMOVED***'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# DEV
BOTDIR = os.getcwd() + '/'

# PROD
# BOTDIR = '/home/ianfitzpat/webapps/ianfitzpatrick_com/tplogobot/'


logo = BOTDIR + gen_logo()
api.update_with_media(logo)

