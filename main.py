import json
import requests
from collections import defaultdict


def match_height_in_inches(targetHeight):
    playersInfo = json.loads(requests.get("https://mach-eight.uc.r.appspot.com/").text)["values"];
    r = defaultdict(list)
    for player in playersInfo:
        r[int(player['h_in'])].append(player['first_name'] + " " + player['last_name'])

    return [player1 + "     " + player2
            for height in r
            if targetHeight - height in r
            for player2 in r[targetHeight - height]
            for player1 in r[height]
            if player1 < player2
            ]


targetHeight = 139
results = match_height_in_inches(targetHeight)
for result in results:
    print(" - " + result)
