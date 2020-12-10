import requests
import os
import json

# sample code for API auth: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py
# info on pagination: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

def auth():
    bearer_token = os.environ.get("BEARER_TOKEN")
    return bearer_token


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
def getTrends():
    bearer_token = auth()
    headers = create_headers(bearer_token)
    url = "https://api.twitter.com/1.1/trends/place.json?id=23424829"
    json_response = connect_to_endpoint(url, headers)
    trends = json.loads(json.dumps(json_response))

    listTrends = []
    for trend in trends[0]["trends"]:
        listTrends.append(trend)
    return listTrends


def getTweets(total_amount, query):
    bearer_token = auth()
    headers = create_headers(bearer_token)
    query = query + " lang:de"

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
        try:
            next_token = dict_response["meta"]["next_token"]
        except KeyError:
            print("not enough tweets for query: " + query)
        data += dict_response["data"]
        
        total_amount -= scrape_amount

    return data


def saveTweetsToStorage(trend_amount, total_amount):
    """
    input:  trend_amount: amount of top trends to fetch
            total_amount: amount of tweets to fetch per trend
    output: None (.json created in storage)
    """
    if trend_amount > 50:
        raise Exception("trends_amount can only be 50 at maximum")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    trends = getTrends()[:trend_amount]

    for trend in trends:
        filename = trend["name"] + '.json'
        path = current_dir + '/../storage/' + filename

        if not os.path.exists(path):
            print("processing: " + trend["name"])
        
            data = getTweets(total_amount, trend["query"])
            json_data = json.dumps(data, indent=4, sort_keys=True)

            with open(path, 'w') as output:
                output.write(json_data)
                print("Data successfully writen to storage/" + filename)
        else:
            print("skipping " + trend["name"] + " -> already in storage")


if __name__ == "__main__":
    saveTweetsToStorage(30, 200) # leave at (5, 10) for testing
    print("You are doing great :)") # motivational message

"""
TODO:
    - run flake8 and tidy up
    - document/comment functions
"""