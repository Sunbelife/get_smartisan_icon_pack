import requests
import json

apps = "apps_category.json"
fp = open(apps, "r")

fp_result = fp.readlines()
fp_result = json.loads(fp_result[0])

def check_if_exisit(bundle_id):
    url = "http://icon.smartisan.com/info/" + bundle_id + "/icon_provided_by_smartisan.xml"
    result = requests.get(url)
    print(url)
    return result.status_code

def download_it(bundle_id):
    url = "http://icon.smartisan.com/drawable/" + bundle_id + "/icon_provided_by_smartisan.png"
    result = requests.get(url)
    file= bundle_id + ".png"
    with open(file,'wb')as f:
        f.write(result.content)
    return result.status_code

print("一共有 " + str(len(fp_result)) + " 个狸：")

for i in fp_result:
    print("=========")
    code = check_if_exisit(i)
    print(code)
    if code == 200:
        download_it(i)
        print("downloaded!")