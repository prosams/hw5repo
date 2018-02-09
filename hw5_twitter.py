from requests_oauthlib import OAuth1
import json
import sys
import requests
import secret_data # file that contains OAuth credentials
import nltk # uncomment line after you install nltk

## SI 206 - HW
## COMMENT WITH: Samantha Lu
## Your section day/time: Tuesday 2-3:30
## Any names of people you worked with on this assignment:

#usage should be python3 hw5_twitter.py <username> <num_tweets>
username = sys.argv[1]
num_tweets = sys.argv[2]

consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

#Code for OAuth starts
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
requests.get(url, auth=auth)
#Code for OAuth ends

#Write your code below:
#Code for Part 3:Caching


CACHE_FNAME = 'cache.json'

try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

def getWithCaching(baseURL, params={}):
  req = requests.Request(method = 'GET', url =baseURL, params = sorted(params.items()))
  prepped = req.prepare()
  fullURL = prepped.url

  # if we haven't seen this URL before
  if fullURL not in CACHE_DICTION:
      # make the request and store the response
      response = requests.Session().send(prepped)
      CACHE_DICTION[fullURL] = response.text

      # write the updated cache file
      cache_file = open(CACHE_FNAME, 'w')
      cache_file.write(json.dumps(CACHE_DICTION))
      cache_file.close()

  # if fullURL WAS in the cache, CACHE_DICTION[fullURL] already had a value
  # if fullRUL was NOT in the cache, we just set it in the if block above, so it's there now
  return CACHE_DICTION[fullURL]

#Finish parts 1 and 2 and then come back to this

#Code for Part 1:Get Tweets

#Code for Part 2:Analyze Tweets



if __name__ == "__main__":
    if not consumer_key or not consumer_secret:
        print("You need to fill in client_key and client_secret in the secret_data.py file.")
        exit()
    if not access_token or not access_secret:
        print("You need to fill in this API's specific OAuth URLs in this file.")
        exit()
