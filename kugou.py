# # import requests
# # import json
# # import re



# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 Edg/81.0.416.58'
# # }

# # song_name = 'hey'

# # url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery112408274198452165868_1587380958225&keyword={}&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1587380958234'.format(song_name)

# # r = requests.get(url, headers=headers)
# # text = json.loads(re.match(".*?({.*}).*", r.text, re.S).group(1))
# # song_list = text['data']['lists']
# # for i in song_list:
# #     print(i['FileHash']+'   '+i['AlbumID'])
# # # print(song_list)

# import requests
# import json
# import re
# # 请求搜索列表数据
# search = 'hey'#input('音乐名:')  # 控制台输入搜索关键词
# pagesize = "10"  # 请求数目
# url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery11240251602301830425_1548735800928&keyword=%s&page=1&pagesize=%s&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1548735800930' % (search, pagesize)
# res = requests.get(url)  # 进行get请求
# # 需要注意一点，返回的数据并不是真正的json格式，前后有那个多余字符串需要用正则表达式去掉,只要大括号{}包着的内容
# # json.loads就是将json数据转为python字典的函数
# res = json.loads(re.match(".*?({.*}).*", res.text, re.S).group(1))
# list_ = res['data']['lists']  # 这个就是歌曲列表
# #建立List存放歌曲列表信息，将这个歌曲列表输出，别的程序就可以直接调用
# musicList = []
# #for循环遍历列表得到每首单曲的信息
# for item in list_:
#     #将列表每项的item['FileHash'],item['AlnbumID']拼接请求url2
#     url2 = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery191010559973368921649_1548736071852&hash=%s&album_id=%s&_=1548736071853' % (
#     item['FileHash'], item['AlbumID'])
#     res2 = requests.get(url2)
#     res2 = json.loads(re.match(".*?({.*}).*", res2.text).group(1))['data']#同样需要用正则处理一下才为json格式,再转为字典
#     #打印一下
#     # print(res2['album_name'])
#     # print(res2['author_name'])
#     print(res2)
#     print('')
#     #将单曲信息存在一个字典里
#     dict = {
#         'author': res2['author_name'],
#         'title': res2['song_name'],
#         'id': str(res2['album_id']),
#         'type': 'kugou',
#         'pic': res2['img'],
#         'url': res2['play_url'],
#         'lrc': res2['lyrics']
#     }
#     #将字典添加到歌曲列表
#     musicList.append(dict)

data = b'jQuery191010559973368921649_1548736071852({"status":1,"err_code":0,"data":{"hash":"963AADE6107F9152B9155B6863A75338","timelength":279936,"filesize":4479405,"audio_name":"\u4f55\u65e0\u7a7a - \u5c11\u5e74\u518d\u89c1","have_album":1,"album_name":"\u5c11\u5e74\u518d\u89c1","album_id":"24018760","img":"http:\/\/imge.kugou.com\/stdmusic\/20190702\/20190702174125270688.jpg","have_mv":0,"video_id":0,"author_name":"\u4f55\u65e0\u7a7a","song_name":"\u5c11\u5e74\u518d\u89c1","lyrics":"[id:$00000000]\r\n[ar:\u4f55\u65e0\u7a7a]\r\n[ti:\u5c11\u5e74\u518d\u89c1]\r\n[by:\u53ef\u7231\u4e0e\u5229\u76ca]\r\n[hash:963aade6107f9152b9155b6863a75338]\r\n[al:\u5c11\u5e74\u518d\u89c1]\r\n[sign:]\r\n[qq:]\r\n[total:279936]\r\n[offset:0]\r\n[00:00.00]\u4f5c\u66f2 : \u4f55\u65e0\u7a7a\r\n[00:00.00]\u4f5c\u8bcd : \u4f55\u65e0\u7a7a\r\n[00:00.00]\u5c11\u5e74\u518d\u89c1\r\n[00:00.00]\u8bcd\u66f2\uff1a\u8d3a\u5b50\u552f\r\n[00:00.00]\u7f16\u66f2\uff1a\u6bdb\u8983\u6109\r\n[00:00.00]\u97f3\u4e50\u5236\u4f5c\uff1a\u683e\u9e4f\u7965\r\n[00:00.78]\u5fae\u7b11\u7684\u5c11\u5e74\u7ad9\u5728\u6821\u95e8\u524d\r\n[00:05.43]\u548c\u5bb6\u4eba\u5408\u5f71\u7559\u5ff5\u7136\u540e\u9053\u522b\r\n[00:09.91]\u8fd9\u6837\u7684\u753b\u9762\u53d1\u751f\u5728\u56db\u5e74\u524d\r\n[00:19.01]\u4e0a\u6b21\u662f\u4f60\u597d \u4eca\u5929\u662f\u518d\u89c1\r\n[00:28.49]\u563f\u4f60\u597d \u6545\u4e8b\u91cc\u7684\u8bfe\u5802\u8fd8\u6709\u5bdd\u5ba4\u697c\u4e0b\u7684\u732b\r\n[00:36.87]\u80fd\u5426\u66ff\u6211\u8bb0\u4f4f\r\n[00:39.39]\u90a3\u4e2a\u63d0\u8d77\u540d\u5b57\u5c31\u4f1a\u5fc3\u75db\u7684\u59d1\u5a18\r\n[00:46.09]\u7b2c\u4e00\u5929\u89c1\u4f60\r\n[00:49.45]\u56db\u5468\u662f\u706f\u5149\u4eba\u7fa4\u6211\u53ea\u80fd\u770b\u89c1\u4f60\r\n[00:55.00]\u5e74\u5c11\u603b\u65e0\u77e5\u4ee5\u4e3a\u76f8\u7231\u53ea\u8981\u7231\u60c5\u624d\u77e5\u9053\u4e16\u754c\u603b\u65e0\u60c5\r\n[01:07.17]\u563f\u4f60\u597d \u5357\u8fb9\u7684\u99a8\u65e6\u82d1\u4e1c\u8fb9\u7684\u90d1\u627f\u9976\r\n[01:15.56]\u662f\u5426\u8fd8\u80fd\u5c1d\u5230 \u9c7c\u4e38\u84b8\u997a\u8336\u53f6\u86cb\u8fd8\u6709\u9999\u80a0\r\n[01:24.62]\u7b2c\u4e00\u6b21\u89c1\u4f60\r\n[01:28.02]\u90a3\u65f6\u7684\u6211\u591a\u5fe7\u5fc3\u5934\u53d1\u548c\u660e\u5929\u7684\r\n[01:32.03]pre\r\n[01:33.87]\u53ef\u662f\u547d\u8fd0\u6349\u5f04\u65f6\u95f4\u5306\u5306\u5c0f\u5c4b\u4eba\u53bb\u697c\u7a7a\r\n[01:45.14]\u518d\u89c1\r\n[01:47.50]\u518d\u89c1\r\n[01:49.42]\u8bf4\u8fc7\u7684\u5927\u8bdd\u8fd8\u6ca1\u5b9e\u73b0\u5c31\u5df2\u8fc7\u4e86\u56db\u5e74\r\n[01:55.32]\u7545\u8c08\u7406\u60f3\u7684\u5149\u8349\u5149\u9636\u8981\u8ba9\u7ed9\u66f4\u5e74\u8f7b\u7684\u5fc3\u613f\r\n[02:03.21]\u518d\u89c1\r\n[02:05.39]\u518d\u89c1\r\n[02:07.63]\u90a3\u65f6\u7684\u6211\u4eec\u4ece\u6765\u4e0d\u7528\u8003\u8651\u660e\u5929\r\n[02:13.20]\u6bcf\u4e00\u4e2a\u65e9\u6668\u90fd\u662f\u65b0\u7684\u5192\u9669\u4eca\u5929\u5374\u5f00\u59cb\u56de\u5fc6\u6628\u5929\r\n[02:21.13]\u548c\u670b\u53cb\u5531\u5427\u7b11\u5427\u843d\u6cea\u5427\u8fd9\u6837\u7684\u673a\u4f1a\u4e0d\u4f1a\u518d\u6709\r\n[02:30.10]\u4f60\u66fe\u7ecf\u558a\u8fc7\u7231\u8fc7\u4e5f\u5931\u53bb\u8fc7\u600e\u4e48\u80fd\u5199\u8fdb\u8fd9\u4e00\u9996\u6b4c\r\n[02:59.20]\u65e6\u590d\u65e6\u516e\u65f6\u95f4\u4e0d\u505c\u5730\u50ac\r\n[03:07.81]\u4e0d\u5fc5\u6050\u614c\u5c11\u5e74\u4f60\u53ea\u8981\u548c\u81ea\u5df1\u8d5b\u8dd1\r\n[03:16.92]\u6211\u7231\u7684\u4e00\u5207\u73b0\u5728\u7559\u7ed9\u6211\u7684\u6628\u5929\r\n[03:26.85]\u660e\u5929\u6211\u8981\u53bb\u7231\u4e0a\u4e00\u4e2a\u65b0\u7684\u4e16\u754c\r\n[03:35.65]\u8d81\u73b0\u5728\u5531\u5427\u7b11\u5427\u843d\u6cea\u5427\u8fd9\u6837\u7684\u673a\u4f1a\u4e0d\u4f1a\u518d\u6709\r\n[03:44.74]\u66fe\u7ecf\u4f60\u558a\u8fc7\u7231\u8fc7\u4e5f\u5931\u53bb\u8fc7\u600e\u4e48\u80fd\u5199\u8fdb\u8fd9\u4e00\u9996\u6b4c\r\n[03:54.16]\u73b0\u5728\u5531\u5427\u7b11\u5427\u843d\u6cea\u5427\u62e5\u62b1\u540e\u5c31\u4e0d\u8981\u518d\u7275\u6302\r\n[04:02.87]\u4f60\u8fd8\u8981\u53bb\u558a\u53bb\u7231\u53bb\u843d\u6cea\u53bb\u51c6\u5907\u4e0b\u4e00\u9996\u6b4c\r\n[04:14.50]\u5fae\u7b11\u7684\u5c11\u5e74\u7ad9\u5728\u6821\u95e8\u524d\r\n[04:19.29]\u548c\u5bb6\u4eba\u5408\u5f71\u7559\u5ff5\u7136\u540e\u9053\u522b\r\n[04:24.43]\u590d\u65e6\u4f60\u597d\r\n[04:31.67]\u590d\u65e6\u518d\u89c1\r\n","author_id":0,"privilege":0,"privilege2":"0","play_url":"https:\/\/webfs.yun.kugou.com\/202004202017\/17c5d6340cfdc01c6a6c6f72bf4edd95\/G168\/M03\/18\/03\/SIcBAF0bGYaAbWFvAERZrVrZEJI542.mp3","authors":[{"author_id":0,"author_name":"\u4f55\u65e0\u7a7a"}],"is_free_part":0,"bitrate":128,"audio_id":"56556040","play_backup_url":"https:\/\/webfs.cloud.kugou.com\/202004202017\/dce14050d221d5aac0fb3994b6c1ec4e\/G168\/M03\/18\/03\/SIcBAF0bGYaAbWFvAERZrVrZEJI542.mp3"}});'
data = str(data,encoding='utf-8')
print(data)