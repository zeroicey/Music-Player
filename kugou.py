import requests
import json
import re


class Kugou:
    def searchMusic(self, headers, search_song):
        r_search = requests.get('https://songsearch.kugou.com/song_search_v2?callback=jQuery1124021060642207775926_1588250057507&keyword={0}&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1588250057509'.format(search_song), headers=headers)
        r_search = json.loads(re.match(".*?({.*}).*", r_search.text, re.S).group(1))
        r_search = r_search['data']['lists']  # 这个就是歌曲列表
        return r_search