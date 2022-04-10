import urllib.request
import json
with urllib.request.urlopen("https://rdconfig-1251945645.cos.ap-shanghai.myqcloud.com/pyrda/db.json") as url:
    data = json.loads(url.read().decode())
    print(data['mssql'])