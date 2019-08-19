import requests


def fetch_countries(country_prefix, page_no):
    url = "https://jsonmock.hackerrank.com/api/countries/search"

    querystring = {"name": country_prefix, "page": str(page_no)}

    headers = {
        'Host': "jsonmock.hackerrank.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def getCountries(s, p):
    json_data = fetch_countries(s, 1)
    countries = 0
    for page_no in range(1, int(json_data["total_pages"]) + 1):
        json_data = fetch_countries(s, page_no)
        for country in json_data["data"]:
            if country['population'] > p:
                countries = countries + 1

    return countries


result = getCountries("in", 10000)
