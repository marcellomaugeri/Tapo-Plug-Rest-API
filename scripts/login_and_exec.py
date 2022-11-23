from tapo_plug import tapoPlugApi
import json
f = open('json/config.json')
device = json.load(f)
print(tapoPlugApi.getDeviceInfo(device))
print("Login successful")