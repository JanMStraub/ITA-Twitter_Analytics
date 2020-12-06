import requests
import os
import json

# sample code for API auth: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
# info on pagination: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url(max_results, query):
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
            "Request returned an error @ {}: {} {}".format(
                url, response.status_code, response.text
            )
        )
    return response.json()


# get top 50 german trends and returns their queries
# returns dicts {'name', 'query', 'tweet_volume', ...} -> tweet_volume is often Null
def getTrends(headers):
    bearer_token = auth()
    url = "https://api.twitter.com/1.1/trends/place.json?id=23424829"
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    trends = json.loads(json.dumps(json_response))


    listTrends = []
    for trend in trends[0]["trends"]:
        listTrends.append(trend)
    return listTrends


def getTweets(total_amount, query, headers):
    scrape_amount = 100
    next_token = ""
    data = []

    while(total_amount != 0):

        if (total_amount < 100):
            scrape_amount = total_amount
        
        url = create_url(scrape_amount, query)
        if (next_token != ""):
            url = url + "&next_token=" + next_token
        json_response = connect_to_endpoint(url, headers)
        dict_response = json.loads(json.dumps(json_response))
        next_token = dict_response["meta"]["next_token"]
        data += dict_response["data"]
        
        total_amount -= scrape_amount

    return data


if __name__ == "__main__":
    headers = create_headers(auth())
    current_dir = os.path.dirname(os.path.abspath(__file__))
    trend_amount = 5
    total_amount = 10 # leave at 10 for testing

    trends = getTrends(headers)[:trend_amount]

    for trend in trends:
        filename = trend["name"] + '.json'
        path = current_dir + '/../storage/' + filename

        if not os.path.exists(path):
            print("processing: " + trend["name"])
        
            data = getTweets(total_amount,trend["query"], headers)
            json_data = json.dumps(data, indent=4, sort_keys=True)

            current_dir = os.path.dirname(os.path.abspath(__file__))
            with open(path, 'w') as output:
                output.write(json_data)
                print("Data successfully writen to storage/" + filename)
        else:
            print("skipping " + trend["name"] + " -> already in storage")

    print("You are doing great :)")

"""
TODO:
    - implement feature to get new, more or less tweets to their appropriate storage file
        -> important for testing of parameters for ML-Methods
    - run flake8 and tidy up
    - document/comment functions
    - rebase main code into seperate function for external access
    - possible feature? -> possibility to get tweets for a costum query 
"""