#coding:utf8
import urllib2
from bs4 import BeautifulSoup
url="http://www.chinacaipu.com/menu/chinacaipu/"

def get_content_from_web(url_address):
    html =urllib2.urlopen(url_address)
    content =html.read()
    html.close()
    soup = BeautifulSoup(content,"html.parser",from_encoding="utf8")
    all_title =soup.find_all('div',class_='pic')
    for t in all_title:
        
        print "http://www.chinacaipu.com"+t.a['href'],t.a.img['alt'],t.a.img['src']
get_content_from_web(url)
