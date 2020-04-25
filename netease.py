import requests
import random
from Crypto.Cipher import AES
import base64
import codecs
import os
import json
from pypinyin import  lazy_pinyin


class Netease:
    def __init__ (self):
        self.b = '010001'
        self.c = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.d = '0CoJUm6Qyw8W8jud'
    #随机的十六位字符串

    def createSecretKey(self, size):
        return (''.join(map(lambda xx: (hex(ord(xx))[2:]), str(os.urandom(size)))))[0:16]
    #AES加密算法

    def AES_encrypt(self, text, key, iv):
        pad = 16 - len(text) % 16
        if type(text)==type(b''):
            text = str(text, encoding='utf-8')
        text = text + str(pad * chr(pad))
        encryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
        encrypt_text = encryptor.encrypt(text.encode("utf8"))
        encrypt_text = base64.b64encode(encrypt_text)
        return encrypt_text
    #得到第一个加密参数

    def Getparams(self, a, SecretKey):
        #0102030405060708是偏移量，固定值
        iv = '0102030405060708'
        h_encText = self.AES_encrypt(a, self.d, iv)
        h_encText = self.AES_encrypt(h_encText,SecretKey,iv)
        return h_encText

    #得到第二个加密参数

    def GetSecKey(self, text, pubKey, modulus):
        # 因为JS做了一次逆序操作
        text = text[::-1]
        rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
        return format(rs, 'x').zfill(256)

    #得到表单的两个参数

    def GetFormData(self, a):
        SecretKey = self.createSecretKey(16)
        params = self.Getparams(a, SecretKey)
        enSecKey = self.GetSecKey(SecretKey, self.b, self.c)
        data = {
            "params" : str(params, encoding='utf-8'),
            "encSecKey" : enSecKey
        }
        return data

    def searchMusic(self, search_song, headers):
        searchUrl = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        musicStr = ''.join(lazy_pinyin(search_song))
        key = '{hlpretag:"",hlposttag:"</span>",s:"' + musicStr + '",type:"1",csrf_token:"",limit:"30",total:"true",offset:"0"}'
        dataStr = str({'s': musicStr, 'csrf_token': ''})
        FormData = self.GetFormData(key)
        response = requests.request('POST', searchUrl, data=FormData, headers={
            'User-agent': headers,
            'referer': 'https://music.163.com/',
            'Host': 'music.163.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'})
        song_writer = []
        song_id = []
        song_name = []
        song_zj = []
        song_dict = json.loads(response.text)
        for song in song_dict['result']['songs']:
            print(song)
            song_name.append(song['name'])
            song_id.append(song['id'])
            song_ar = song['ar']
            if len(song_ar) == 2:
                song_writer.append(song_ar[0]['name'] + '_' + song_ar[1]['name'])
            else:
                song_writer.append(song_ar[0]['name'])
            song_zj.append(song['al']['name'])
        return song_dict['result']['songs']
if __name__ == '__main__':
    search_song = input("请输入搜索音乐的名称:")
    nete_music = Netease()
    song = nete_music.searchMusic(search_song, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
    print(song)