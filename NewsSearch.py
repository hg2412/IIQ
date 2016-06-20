#Reference: https://xyang.me/using-bing-search-api-in-python/

import urllib
import requests
from requests.auth import HTTPBasicAuth

# Bing API key
API_KEY = "###########################"


def bing_api(query, source_type="news", top=20, format='json'):
    """Returns the decoded json response content

    :param query: query for search
    :param source_type: type for seacrh result
    :param top: number of search result
    :param format: format of search result
    """
    # set search url
    query = urllib.quote(query)
    # web result only base url
    base_url = 'https://bingapis.azure-api.net/api/v5/news/search'
    url = base_url + '?q=' + query + \
        '&responseFilter=news' + '&count=' + str(top)
    # create credential for authentication
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
    # set headers
    headers = {'User-Agent': user_agent, 'Ocp-Apim-Subscription-Key':API_KEY}
    # get response from search url
    response_data = requests.get(url, headers=headers)
    print response_data
    # decode json response content
    json_result = response_data.json()
    return json_result

def search_news(comp_list, top=20):
    results = []
    for comp in comp_list:
        result = bing_api(comp, 'news', top)
        results.append(result)
    return results
