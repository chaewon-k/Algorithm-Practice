import requests
import json


def avgRotorSpeed(statusQuery, parentId):
    url = 'https://jsonmock.hackerrank.com/api/iot_devices/search'
    status = requests.get(url, params={"status": statusQuery})
    jsonToDic = json.loads(status.text)
    pages = jsonToDic["total_pages"]

    rotorSpeed = []
    for i in range(pages):
        pageData = requests.get(url, params={"status": statusQuery, "page": str(i + 1)}).text
        pageDataToDic = json.loads(pageData)
        item = pageDataToDic["data"]

        for j in item:
            if "parent" in j.keys() and j["parent"] != None:
                if j["parent"]["id"] == parentId:
                    rotorSpeed.append(j["operatingParams"]["rotorSpeed"])

    if len(rotorSpeed) > 0:
        answer = sum(rotorSpeed) / len(rotorSpeed)
    else:
        answer = 0
    return answer


print(avgRotorSpeed('RUNNING', 7))