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
    return "%23nofilter lang:en"

def create_url():
    query = getQuery()
    max_results = 10 # value between 10 and 100
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

def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":

    main()
    print("Everything works fine :)")