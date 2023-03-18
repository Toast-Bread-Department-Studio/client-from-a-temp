import requests



req = requests.get("http://127.0.0.1:7860/sdapi/v1/sd-models").json()
for i in req:
    print(i["hash"])