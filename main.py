# from kugou import Kugou
from netease import Netease
# from qqmusic import Qmusic
# from baidumusic import Bmusic
import prettytable as pt
import requests
import os
import random


class Player():
    """docstring for Player"""
    def __init__(self):
        if not os.path.exists(r"./song"):
            os.mkdir(r"./song")

    def askMusic(self):
        use_way = input("请输入使用模式:")
        if use_way == "搜索":
            self.searchMusic()

    def downloadMusic(self):
        pass

    def showMusic(self):
        pass

    def requestsHeaders(self):
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
        return ua[random.randint(0, len(ua) - 1)]

    def searchMusic(self):
        search_song = input("请输入要搜索的歌曲:")
        search_way = input("请输入要搜索的平台(1.网易云，2.千千音乐，3.酷狗音乐，4.QQ音乐):")
        if search_way == "1":
            nete_music = Netease()
            nete_songs = nete_music.searchMusic(search_song, self.requestsHeaders())
            for nete_song in nete_songs:
                print(nete_song)


music_player = Player()
music_player.askMusic()