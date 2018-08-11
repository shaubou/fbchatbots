# coding=utf-8
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
# 宣告
search_link_data = None
search_detail_link = None
search_detail_data = []
datasearchtitle=[]
datasearchlink=[]
def wikisearch(recevied_message):
    print("recevied_messageJHF", recevied_message)
    search_detail_data_text = []
    search_detail_data = []
    ua = UserAgent()
    # 一般的桌面板瀏覽器
    headers = {'User-Agent': ua.random}
    # 假iPhone瀏覽器
    # mobile_headers ={'User-Agent': ua.random}
    # 網址製作區https://tw.answers.search.yahoo.com/search?fr=uh3_answers_vert_gs&type=2button&p=
    url = 'https://zh.wikipedia.org/zh-tw/'
    # 抓取網頁資料
    response = requests.get(url=url + recevied_message, headers=headers)
    input_html = response.text
    if response.status_code == requests.codes.ok:
        # 下面是整理成要用的資料
        soup = BeautifulSoup(input_html, 'html.parser')
        items = soup.select('p')
        print("tytyty",items)
        for i in items:
            # 標題
            search_detail_data_text.append(i.text)
            # 網址
        print("hjhjhj",search_detail_data_text)
        for j in search_detail_data_text:
            print("JJ-j1", j)
            j.splitlines()
            print("JJ-j2", j)
            j.strip()
            print("JJ-j3", j)
            search_detail_data.append(j+".")

    print("search_detail_dataTJ", str(search_detail_data))
    print("uyuyu",str(search_detail_data))
    return search_detail_data

def yahoodatasearch(recevied_message):
    global datasearchtitle , datasearchlink
    datasearchtitle.clear()
    datasearchlink.clear()
    print("AAdatasearchtitle",datasearchtitle)
    ua = UserAgent()
    #一般的桌面板瀏覽器
    #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    headers = {'User-Agent': ua.random}
    #假iPhone瀏覽器
    #mobile_headers ={'User-Agent': ua.random}
    url = 'https://tw.answers.search.yahoo.com/search?fr=uh3_answers_vert_gs&type=2button&p='
    # 抓取網頁資料
    response = requests.get(url=url+recevied_message,headers=headers)
    input_html = response.text
    if response.status_code == requests.codes.ok:
    # 下面是整理成要用的資料
        soup = BeautifulSoup(input_html,'html.parser')
        items = soup.select('.fz-m')
        for i in items:
            # 標題
            datasearchtitle.append(i.text+".")
            # 網址
            datasearchlink.append(i.get('href'))
    print("HHdatasearchtitle", datasearchtitle)
    print("HHdatasearchlink", datasearchlink)
    return datasearchtitle,datasearchlink

def yahoodetaillink(search_link_data):
    search_detail_link_data =[]
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    # 網址製作區
    url = "https:"+search_link_data
    #url = quote(search_link_data,'utf-8')
    # 抓取網頁資料
    response = requests.get(url=url,headers=headers)
    #response.encoding = 'utf8'
    input_html = response.text
    if response.status_code == requests.codes.ok:
    # 下面是整理成要用的資料
        soup = BeautifulSoup(input_html, 'html.parser')
        items = soup.select('meta')
        for i in items:
            search_detail_link_data.append(i.get('content'))
    search_detail_link = search_detail_link_data[1].lstrip("'0;URL=")
    search_detail_link = search_detail_link.rstrip("'")
    return search_detail_link

def yahoodetailsearch(search_detail_link):
    search_detail_data_text = []
    search_detail_data = []
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    # 網址製作區
    url = search_detail_link
    #url = quote(search_link_data,'utf-8')
    # 抓取網頁資料
    response = requests.get(url=url,headers=headers)
    #response.encoding = 'utf8'
    input_html = response.text
    if response.status_code == requests.codes.ok:
        print(response.status_code,requests.codes.ok)
    # 下面是整理成要用的資料
        soup = BeautifulSoup(input_html, 'html.parser')
        items = soup.select('.ya-q-full-text')
        print("items",items)
        for i in items:
            search_detail_data_text.append(i.text)
        print("search_detail_data_text",search_detail_data_text)
        for j in search_detail_data_text:
            print("JJ-j1",j)
            j.splitlines()
            print("JJ-j2", j)
            j.strip()
            print("JJ-j3", j)
            search_detail_data.append(j+".")
        print("QQ---",search_detail_data)
    return search_detail_data
