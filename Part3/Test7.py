#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author fzl
# Date 2017/2/25 11:53
# EMAIL fangjalylong@qq.com
# Desc 获取所有可用的代理ip
# --------------------------
import codecs
import time

from bs4 import BeautifulSoup
import requests
import random
url = 'http://www.xicidaili.com/nn/'
headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
	}
def get_ip_list(page):
	web_data = requests.get(url+str(page), headers=headers)
	soup = BeautifulSoup(web_data.text, 'lxml')
	ips = soup.find_all('tr')

	for i in range(1, len(ips)):
		ip_info = ips[i]
		tds = ip_info.find_all('td')
		file.write(tds[1].text + ':' + tds[2].text+"\n\n")
	return



def get_random_ip(ip_list):
	proxy_list = []
	for ip in ip_list:
		proxy_list.append('http://' + ip)
	proxy_ip = random.choice(proxy_list)
	proxies = {'https': proxy_ip}
	return proxies


if __name__ == '__main__':
	file = codecs.open("ip.txt", "wb+", "utf-8")
	x=1
	for x in  range(500):
		ip_list = get_ip_list(x)
		x+=1;
		time.sleep(0.5)
	file.close()

