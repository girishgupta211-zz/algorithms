import json
from collections import defaultdict

import requests


def parse_espn(match_id, inning_dict):
    mismatches = []
    count_mismatches = []
    for inning in (1, 2):
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
                over = item['over']['overs']
                toch_out = inning_dict[str(inning)][str(over)]

                # if item['over']['wickets'] == 1:
                if "out" in item['playType']['description'].lower():
                    espn_out = 'out'
                else:
                    espn_out = str(item['scoreValue'])

                resp = ("Inning: {}  Over: {}, espn: {} toch: {}".format(
                    str(inning), over, espn_out, toch_out))

                if espn_out in toch_out and len(toch_out) == 1:
                    pass
                    # print("exact match")
                elif espn_out in toch_out and len(toch_out) > 1:
                    # print("matches but multiple outcomes by Toch")
                    count_mismatches.append(resp)
                else:
                    print("does not match:  {}".format(resp))
                    # print(querystring)
                    mismatches.append(resp)

    print("mismatches: {}".format(mismatches))
    print("count mismatches: {}".format(count_mismatches))


def create_dict_from_toch_file(file_path):
    match_dict_1 = defaultdict(list)
    match_dict_2 = defaultdict(list)
    inning_dict = {'1': match_dict_1, '2': match_dict_2}
    with open(file_path) as json_file:
        # data = json.load(json_file)
        lines = json_file
        for line in lines:
            row = json.loads(line.rstrip('\n'))
            # print(row)
            if row['innings_no'] == '1':
                key = str(row['over_no']) + "." + row['delivery_no']
                match_dict_1[key].append(row['outcome'])

            if row['innings_no'] == '2':
                key = str(row['over_no']) + "." + row['delivery_no']
                match_dict_2[key].append(row['outcome'])
    return inning_dict


toch_dict = create_dict_from_toch_file(
    '/Users/girish/toch/toch_match_190774_delivery.json')
parse_espn("1144523", toch_dict)
