import requests
import os
import json

# sample code for this file: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
# info on pagination: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

def auth():
    return os.environ.get("BEARER_TOKEN")

# query needs to be url encoded: # := %23; [space] ;= + OR %20
# further information: https://de.wikipedia.org/wiki/URL-Encoding 
def getQuery():
    trends = getTrends()
    return trends[0] + " lang:de"

def create_url(max_results):
    query = getQuery()
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=text,lang,created_at"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&max_results={}".format(query, tweet_fields, max_results)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

# get top 50 german trends and returns their queries
def getTrends():
    bearer_token = auth()
    url = "https://api.twitter.com/1.1/trends/place.json?id=23424829"
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    trends = json.loads(json.dumps(json_response))


    listTrends = []
    for trend in trends[0]["trends"]:
        listTrends.append(trend["query"])
    return listTrends

def main(max_results):
    bearer_token = auth()
    url = create_url(max_results)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    
    
    next_token = json.loads(json.dumps(json_response))["meta"]["next_token"]
    new_url = url + "&next_token=" + next_token
    json_response2 = connect_to_endpoint(new_url, headers)
    print(json.dumps(json_response2, indent=4, sort_keys=True))

"""
current state:
    - max_results is the number of tweets per request
    - max_results can only be a value between 10 and 100
    - more tweets can be obtained via the next_token

TODO:
    - implement an iterative approch to get more than 100 tweets via the next_token
    - concentate all resulting JSONs in a big one
"""


if __name__ == "__main__":

    max_results = 10

    main(max_results)

    print("You are doing great :)")