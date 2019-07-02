import requests

match_id = "1144521"
for inning in (1, 3):
    for page in range(1, 14):
        url = "https://site.web.api.espn.com/apis/site/v2/sports/cricket/8039/playbyplay"

        querystring = {"contentorigin": "espn",
                       "event": str(match_id),
                       "page": str(page),
                       "period": str(inning),
                       "section": "cricinfo"}

        headers = {
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Host': "site.web.api.espn.com",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
        }

        response = requests.request("GET", url, headers=headers,
                                    params=querystring)
        espncricinfo = response.json()
        commentary = espncricinfo['commentary']
        for item in commentary['items']:
            print("inning no: {} --> Over: {}, output: {}".format(
                str(inning),
                item['over']['overs'],
                item['scoreValue']))
