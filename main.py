import requests
import json
import time
import os
from colorama import Fore, init
from datetime import datetime
init()

os.system("title trade ad bot")


def info(msg): print(f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')} {Fore.LIGHTBLUE_EX}[INFO]{Fore.RESET} {msg}")
def success(msg): print(f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')} {Fore.LIGHTGREEN_EX}[SUCCESS]{Fore.RESET} {msg}")
def error(msg): print(f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')} {Fore.RED}[ERROR]{Fore.RESET} {msg}")


while True:

    with open("config.json") as f:
        config = json.load(f)["RolimonsTradeAds"]
        userId = config["userId"]
        roliVerification = config["roliVerification"]

        offerItems = config["offerItems"]
        requestItems = config["requestItems"]
        requestTags = config["requestTags"]
        offerRobux = config["offerRobux"]

    s = requests.Session()
    s.cookies["_RoliVerification"] = roliVerification


    postData = {
        "player_id": userId,
        "offer_item_ids": offerItems,
        #"offer_robux": offerRobux,
        "request_item_ids": requestItems,
        "request_tags": requestTags
    }

    adRequest = s.post("https://www.rolimons.com/tradeapi/create", json=postData)

    if adRequest.status_code == 201:
        success("Successfully posted Rolimons Trade Ad!")
    elif adRequest.status_code == 429:
        error("Failed to post Rolimons Trade ad due to being rate limited.")
    else:
        error("Failed to post Rolimons trade ad.")
        error(f"Status Code: {adRequest.status_code}")
        error(f"Error Text: {adRequest.text}")
        print(adRequest.json())

    with open("config.json") as f:
        config = json.load(f)["RoProTradeAds"]
        userId = config["userId"]
        phpsessid = config["phpsessid"]
        roproId = config["roproId"]
        roproVerification = config["roproVerification"]
        request1 = config["request1"]
        request2 = config["request2"]
        request3 = config["request3"]
        request4 = config["request4"]
        requestValue = config["requestValue"]
        offer1 = config["offer1"]
        offer2 = config["offer2"]
        offer3 = config["offer3"]
        offer4 = config["offer4"]
        message = config["message"]

    cookies = {
        'PHPSESSID': phpsessid,
    }

    headers = {
        'authority': 'api.ropro.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'chrome-extension://adbacgifemdbhdkfppmeilbgppmhaobf',
        'ropro-id': roproId,
        'ropro-verification': roproVerification,
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'none',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    data = {
        'userid': userId,
        'want_item': request1,
        'want_item2': request2,
        'want_item3': request3,
        'want_item4': request4,
        'want_value': requestValue,
        'item1': offer1,
        'item2': offer2,
        'item3': offer3,
        'item4': offer4,
        'note': message,
    }

    info("Trying to post RoPro Trade Ad...")
    response = requests.post('https://api.ropro.io/postWishlist.php', cookies=cookies, headers=headers, data=data)
    try:
        if not "error" in response.json():
            success("Successfully posted RoPro Trade Ad!")
        else:
            error("Failed to post RoPro Trade ad, most likely due to being on cooldown.")
    except json.decoder.JSONDecodeError:
        error("I have no fucking clue whats wrong to be honest")
        error(f"Response {response.status_code}")
        error(response.text)

    time.sleep(1800)
