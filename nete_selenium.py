from selenium import webdriver
import re
import prettytable as pt


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}



def get_music_id():
    option=webdriver.ChromeOptions()
    option.add_argument('headless') # 设置option
    driver = webdriver.Chrome(r'D:\Python\chromedriver.exe', chrome_options=option)
    driver.get('https://music.163.com/#/playlist?id=2526186753')
    driver.switch_to_frame('g_iframe')
    html = driver.page_source
    # print(html)
    a = re.findall(r'<a href="/song\?id=(.*?)">', html)
    b = re.findall(r'<a href="/song\?id=.*?"><b title="(.*?)">', html)
    writer = re.findall(r'<a href="/artist\?id=.*?">(.*?)</a>', html)
    tb = pt.PrettyTable()
    tb.add_column('Song Id', a)
    tb.add_column('Song Name', b)
    print(writer)
    print(tb)




if __name__ == '__main__':
  get_music_id()