import re
import requests
class Xiaoshuo():
    def __init__(self,url):
        self.url = url
    def xiao(url):
        print(url)
        r = requests.get(url)
        r.encoding = 'utf-8'
        x = re.findall(r'<div id="content">(.*)</div>', r.text)[0]
        y = re.findall(r'[^&nbsp;<br />]+', x)
        biaoti = re.findall(r'<h1>(.*)</h1>', r.text)[0].replace(' ', '')
        print(biaoti)
        with open(r'/Users/zhanghang/Desktop/万族之劫.txt', "a+") as f:
            f.write(biaoti + '\n')
            for i in range(len(y)):
                f.write(y[i] + '\n')
            f.close()
link = 'https://www.xsbiquge.com/92_92520/'
r = requests.get(link)
r.encoding = 'utf-8'
urls = re.findall(r'<a href="/92_92520/(\d+).html">',r.text)
for i in range(len(urls)):
    url = 'https://www.xsbiquge.com/92_92520/'+str(urls[i])+'.html'
    xiaoshuo = Xiaoshuo.xiao(url)

