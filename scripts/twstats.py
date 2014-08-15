import os
import os.path
import sys
from ConfigParser import ConfigParser

from twython import Twython

__CONFIG_PATH = './twstats.ini'
__TOKEN_PATH = '.twstats-token'

def init_app():
    config = ConfigParser()
    if not os.path.isfile(__CONFIG_PATH) or not os.access(__CONFIG_PATH, os.R_OK):
        print 'The file %s has been created. Please edit it before running the command again.' % (__CONFIG_PATH)
	config.add_section('Twitter App')
	config.set('Twitter App', 'API_KEY', '<YOUR_API_KEY> # See Twitter apps documentation about OAuth')
	config.set('Twitter App', 'API_SECRET', '<YOUR_API_SECRET>')
	with open(__CONFIG_PATH, 'wb') as config_file:
	    config.write(config_file)

	sys.exit(0)

    config.read(__CONFIG_PATH)
    api_key = config.get('Twitter App', 'API_KEY') 
    api_secret = config.get('Twitter App', 'API_SECRET') 

    if not os.path.isfile(__TOKEN_PATH) or not os.access(__TOKEN_PATH, os.R_OK):
        twitter = Twython(APP_KEY, access_token=token)
	
    twitter = Twython(api_key, api_secret, oauth_version=2)
    token = twitter.obtain_access_token()
    
    with open(__TOKEN_PATH, 'wb') as token_file:
        token_file.write(token)

    twitter = Twython(api_key, access_token=token)
    return twitter

if __name__ == '__main__':
    twitter = init_app()
    results = twitter.search(q='python')
    print results

