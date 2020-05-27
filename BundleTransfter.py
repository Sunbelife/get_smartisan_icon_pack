import requests
import json
from bs4 import BeautifulSoup

android_bundle_id = "com.qq.reader"
android_info_query_url = "https://www.coolapk.com/apk/" + android_bundle_id

android_info_result = requests.get(android_info_query_url)

soup = BeautifulSoup(android_info_result.text,"html.parser")

keyword = soup.title.string.split("-")[0]

print("嗯嗯，安卓 bundle 叫：「" + android_bundle_id + "」，我去找找。。。")
print("找到狸，是：「" + keyword + "」。")
print("嗯嗯，现在去 App Store 狸。")

url = "https://itunes.apple.com/search?term=" + keyword + "&entity=software&limit=5"

result = requests.get(url = url)

result_json = json.loads(result.text)
result_list = []

print("嗯嗯，一共找到了" + str(result_json['resultCount']) + "个\n让我整理一下。") 

for i in result_json['results']:
	result_list.append({ "trackName" : i['trackName'], "bundleId" : i['bundleId']})
	
print("嗯嗯，都在这里狸：")
index = 0
for i in result_list:
	print("[" + str(index) + "]" + str(i["trackName"]) + str(i["bundleId"]))
	index = index + 1

input_index = int(input("你要哪个狸？可以在这里输入："))
print("嗯嗯，知道了。")
print("那就是这个：「" + result_list[input_index]["bundleId"] + "」。")

