import requests
import re



headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
r = requests.get('https://music.163.com/#/user/home?id=1436779441', headers=headers)
text = re.findall(r'<img src="(.*?)', r.text)
print(text)