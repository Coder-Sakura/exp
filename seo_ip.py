import requests
import random
import time
from lxml import etree
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning     # 用于强制取消警告
from requests.adapters import HTTPAdapter                                   # 用于强制取消警告

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)      # 强制取消警告

class seo_ip():

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        self.agent_ip_list = []
    
    def Agent(self,ip_agent_url):
        html = requests.get(url=ip_agent_url,headers=self.headers,verify=False,timeout=5)
        html_soup = BeautifulSoup(html.text, 'lxml')
        # 去除第一个和前25个，26-50为国外ip
        ip_list = html_soup.find('tbody').find_all('tr')[26:]    
        items = []
        print('搜索完成,代理信息如下:') 
        for item in ip_list:        
            ip_port = list(item)[0].get_text() + ':' +list(item)[1].get_text()
            # list(ip_port)[0]为ip,[1]为端口,[2]响应时间,[3]位置,[4]最后验证时间
            print('ip: %s ,响应时间: %ss ,ip位置: %s' % (ip_port,list(item)[2].get_text(),list(item)[3].get_text()))
            items.append(ip_port)        #存储爬取到的ip(需要添加)
        return items

    def judge(self,items):       # 检验ip活性     # https://ip.seofangfa.com/
        print('正在进行代理池ip活性检测......')
        for item in items:
            try:
                proxy = {
                    'http':item,
                    'https':item
                    }
                # 遍历时，利用百度，设定timeout，未响应则断开连接
                judge_url = 'https://www.baidu.com/'     
                response = requests.get(url=judge_url,headers=self.headers,proxies=proxy,verify=False,timeout=5)
                self.agent_ip_list.append(item)
                print(item,'可用...')
            except:
                print(item,'不可用...')
        print('代理池ip活性检测完毕...\n代理池总量:',len(self.agent_ip_list),'\n代理池:',self.agent_ip_list)

    def work(self):
        ip_agent_url = 'https://ip.seofangfa.com/'
        items = self.Agent(ip_agent_url)
        self.judge(items)

seo_ip = seo_ip()
seo_ip.work()