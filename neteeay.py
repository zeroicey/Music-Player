import requests
import random
from Crypto.Cipher import AES
import base64
import codecs
import os
import json
from pypinyin import  lazy_pinyin
import prettytable as pt



ua =  [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'
]


b = '010001'
c = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
d = '0CoJUm6Qyw8W8jud'
#随机的十六位字符串
def createSecretKey(size):
	return (''.join(map(lambda xx: (hex(ord(xx))[2:]), str(os.urandom(size)))))[0:16]
#AES加密算法
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    if type(text)==type(b''):
        text = str(text, encoding='utf-8')
    text = text + str(pad * chr(pad))
    encryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
    encrypt_text = encryptor.encrypt(text.encode("utf8"))
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text
#得到第一个加密参数
def Getparams(a,SecretKey):
    #0102030405060708是偏移量，固定值
    iv = '0102030405060708'
    h_encText = AES_encrypt(a,d,iv)
    h_encText = AES_encrypt(h_encText,SecretKey,iv)
    return h_encText
#得到第二个加密参数
def GetSecKey(text, pubKey, modulus):
    # 因为JS做了一次逆序操作
    text = text[::-1]
    rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)
#得到表单的两个参数
def GetFormData(a):
    SecretKey = createSecretKey(16)
    params = Getparams(a,SecretKey)
    enSecKey = GetSecKey(SecretKey,b,c)
    data = {
		"params":str(params,encoding='utf-8'),
		"encSecKey":enSecKey
	}
    return data

musicPY = input("请输入歌曲名称:")

searchUrl = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
musicStr = ''.join(lazy_pinyin(musicPY))
key = '{hlpretag:"",hlposttag:"</span>",s:"'+musicStr+'",type:"1",csrf_token:"",limit:"30",total:"true",offset:"0"}'
dataStr=str({'s': musicStr, 'csrf_token': ''})
FormData = GetFormData(key)
response = requests.request('POST', searchUrl, data=FormData,headers={
        'User-agent': ua[random.randint(1, len(ua) - 1)],
        'referer': 'https://music.163.com/',
        'Host':'music.163.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
})
song_writer = []
song_id = []
song_name = []
song_zj = []
song_dict = json.loads(response.text)
for song in song_dict['result']['songs']:
    # print(song)
    song_name.append(song['name'])
    song_id.append(song['id'])
    song_ar = song['ar']
    if len(song_ar) == 2:
        song_writer.append(song_ar[0]['name'] + '_' + song_ar[1]['name'])
    else:
        song_writer.append(song_ar[0]['name'])
    song_zj.append(song['al']['name'])

tb = pt.PrettyTable()
tb.add_column('ID', song_id)
tb.add_column('名称', song_name)
tb.add_column('作者', song_writer)
tb.add_column('专辑', song_zj)

print(tb)

