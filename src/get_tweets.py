import requests
import os
import json


# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    """
    OUT:
    bearer_token (string): return the content of the environment variable BEARER_TOKEN
    """
    bearer_token = os.environ.get("BEARER_TOKEN")
    return bearer_token


def create_url(max_results, query):
    """
    IN:
    max_results (int): number of tweets to get from API
    query (string): twitter search query
    OUT:
    url (string): twitter API url for given query with [max_result] tweets
    """
    tweet_fields = "tweet.fields=text,lang,created_at"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&max_results={}"\
        .format(query, tweet_fields, max_results)
    return url


def create_headers(bearer_token):
    """
    IN:
    bearer_token (string): bearer_token for authentication
    OUT:
    headers (string): http headers for authentication
    """
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    """
    IN:
    url (string): twitter API url
    headers (string): http headers for authentication
    OUT:
    response.json() (json): json response from API with tweets
    """
    response = requests.request("GET", url, headers=headers)
    print("status code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(
            "Request returned an error @ {}: {} {}".format(
                url, response.status_code, response.text
            )
        )
    return response.json()


def get_trends():
    """
    OUT:
    list_trends (List): list of top 50 trends on twitter as strings at the current moment
    """
    bearer_token = auth()
    headers = create_headers(bearer_token)
    url = "https://api.twitter.com/1.1/trends/place.json?id=23424829"
    json_response = connect_to_endpoint(url, headers)
    trends = json.loads(json.dumps(json_response))

    list_trends = []
    for trend in trends[0]["trends"]:  # unpack json response and add trend to list
        list_trends.append(trend)
    return list_trends


def get_tweets(total_amount, query):
    """
    IN:
    total_amount (int): total amount of tweets to get per query
    query (string): search query(trend in our case) for tweets
    OUT:
    data (List): list of tweets in json style
    """
    bearer_token = auth()
    headers = create_headers(bearer_token)
    query = query + " lang:de"

    scrape_amount = 100
    next_token = ""
    data = []

    # twitter API can only return 100 tweets per request, therefore we take the total amount and decrement 100 per
    # iteration of the loop
    while total_amount != 0:

        # for last loop if total_amount % 100 != 0
        if total_amount < 100:
            scrape_amount = total_amount

        url = create_url(scrape_amount, query)
        # next_token tells the API where the last request ended
        if next_token != "":
            url = url + "&next_token=" + next_token
        json_response = connect_to_endpoint(url, headers)
        dict_response = json.loads(json.dumps(json_response))

        # if no next_token is provided, there are not enough tweets to match total_amount
        try:
            next_token = dict_response["meta"]["next_token"]
        except KeyError:
            print("not enough tweets for query: " + query)
            break
        data += dict_response["data"]

        total_amount -= scrape_amount

    return data


def save_trend_to_storage(trend, total_amount):

    current_dir = os.path.dirname(os.path.abspath(__file__))

    filename = trend + '.json'
    path = current_dir + '/../storage/jsons/' + filename

    # getting the trend dict for trend["query"]
    with open(current_dir + '/../storage/trends.json') as trends:
        for trend_dict in json.load(trends):
            if trend_dict["name"] == trend:
                trend = trend_dict
                break

    if isinstance(trend, str):
        raise RuntimeError('Trend not found in trends.json: ' + trend)

    if not os.path.exists(path):
        print("processing: " + trend["name"])

        data = get_tweets(total_amount, trend["query"])
        if (len(data) == 0):
            raise RuntimeError('Trend does not contain any tweets: ' + trend["name"])
        json_data = json.dumps(data, indent=4, sort_keys=True)

        with open(path, 'w') as output:
            output.write(json_data)
            print("Data successfully writen to storage/jsons" + filename)
    else:
        print("skipping " + trend["name"] + " -> already in storage")


if __name__ == "__main__":
    print("You are doing great :)")  # motivational message
