# from kugou import Kugou
from netease import Netease
# from qqmusic import Qmusic
# from baidumusic import Bmusic
import prettytable as pt
import requests
import os
import random
import sys


class Player():
    """docstring for Player"""
    def __init__(self):
        if not os.path.exists(r"./song"):
            os.mkdir(r"./song")
            os.mkdir(r'./song/网易云音乐')
            os.mkdir(r'./song/千千音乐')
            os.mkdir(r'./song/QQ音乐')
            os.mkdir(r'./song/酷狗音乐')
        self.introduce_pt = pt.PrettyTable(['作者', '联系方式', '开发时间'])
        self.introduce_pt.add_row(['孤痕', 'QQ:3245632373', '2020/4/25'])
        print(self.introduce_pt)
        input('按回车继续')

        self.music_singer = []
        self.music_name = []
        self.music_album = []
        self.music_id = []

    def askUse(self):
        try:
            os.system('cls')
            print(self.introduce_pt)
        except:
            pass
        print('使用模式：搜索歌曲，下载歌单')
        use_way = input("请输入使用模式:")
        if use_way == "搜索歌曲":
            self.askSearch()
        elif use_way == "下载歌单":
            self.listMusic()

    def askSearch(self):
        search_song = input("请输入要搜索的歌曲:")
        search_way = input("请输入平台(1.网易云，2.千千音乐，3.酷狗音乐，4.QQ音乐)(输入数字):")
        self.searchMusic(search_way, search_song)

    def askContinue(self, how):
        print('您可以：1.下载我想要的音乐，2.继续搜索音乐，3.我要换一种模式，4.退出程序')
        continue_input = input("请输入接下来的操作(数字)：")
        if continue_input == "1":
            self.downloadMusic(how)
        else:
            try:
                self.music_name = []
                self.music_id = []
                self.music_album = []
                self.music_singer = []
                os.system('cls')
                print(self.introduce_pt)
            except:
                pass
            if continue_input == "2":
                self.askSearch()
            elif continue_input == "3":
                self.askUse()
            elif continue_input == "4":
                sys.exit()

    def downloadMusic(self, how):
        if how == "netease":
            down_id = int(input("请输入要下载的歌曲编号：")) - 1
            if self.music_id[down_id]:
                try:
                    r_download = requests.get('http://music.163.com/song/media/outer/url?id={0}.mp3'.format(self.music_id[down_id]), headers={
                'User-agent': self.requestsHeaders()})
                    with open('./song/网易云音乐/{0}.mp3'.format(self.music_name[down_id]), "wb") as file1:
                        file1.write(r_download.content)
                    print("已下载在./song/网易云音乐/{0}.mp3".format(self.music_name[down_id]))
                except Exception as e:
                    print(e)
                    print("请检查文件是否完整，本次下载失败")
            else:
                print('你输入的啥玩意')
            self.askContinue(how)

    def showMusic(self, songs, use_way):
        if use_way == "netease":
            for song in songs:
                # 获取歌曲ID
                Id = song['id']
                self.music_id.append(Id)
                # print(Id)
                # 获取歌曲名称
                name = song['name']
                self.music_name.append(name)
                # print(name)
                # 获取歌手名称
                singer = ""
                for ar in song['ar']:
                    singer += ar['name']
                    singer += '/'
                singer = list(singer)
                singer[-1] = ""
                singer = "".join(singer)
                # print(singer)
                self.music_singer.append(singer)
                # 获取专辑名称
                if song['al']['name']:
                    album = song['al']['name']
                    # print(album)
                    self.music_album.append(album)
                else:
                    self.music_album.append('暂无专辑')
            netease_pt = pt.PrettyTable()
            netease_pt.add_column('编号', [i + 1 for i in range(len(self.music_id))])
            netease_pt.add_column('ID', self.music_id)
            netease_pt.add_column('歌曲', self.music_name)
            netease_pt.add_column('歌手', self.music_singer)
            netease_pt.add_column('专辑', self.music_album)
            print(netease_pt)
            netease_pt = None
        elif use_way == "qqmusic":
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

    def searchMusic(self, search_way, search_song):
        if search_way == "1":
            nete_music = Netease()
            nete_songs = nete_music.searchMusic(search_song, self.requestsHeaders())
            self.showMusic(nete_songs, 'netease')
            self.askContinue('netease')
        elif search_way == "2":
            pass

        elif search_way == "3":
            pass

        elif search_way == "4":
            pass

    def listMusic(self):
        search_way = input("请输入平台(1.网易云，2.千千音乐，3.酷狗音乐，4.QQ音乐)(输入数字):")
        search_user = input("请输入此平台的用户名:")
        if search_way == "1":
            pass
        elif search_way == "2":
            pass

        elif search_way == "3":
            pass

        elif search_way == "4":
            pass


music_player = Player()
music_player.askUse()