import requests
from bs4 import BeautifulSoup
import re
import requests

cookies = {
    'wdcid': '1e844a8c45e21481',
    'JSESSIONID': '208CF79D1F8D233DF95D1E01D821368C',
    'zhuzhan': '44186949',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://zwgk.mwr.gov.cn',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://gjkj.mwr.gov.cn/',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
}

data = {
  'bzfl': '0',
  'fbsj': '',
  'zyml': '',
  'gnxl': ''
}

response = requests.post('http://zwgk.mwr.gov.cn/jsp/yishenqing/appladd/bzsearch.jsp', headers=headers, cookies=cookies, data=data, verify=False)


soup = BeautifulSoup(response.text,"lxml")
biaozhun = soup.find_all('tr',class_='gradeX')
list =[]
for eachone in biaozhun:
    eachone = str(eachone).replace('\n','').replace(' ','')
    name = re.findall(r'target="_blank">(.*?)</a>',eachone)[0]
    sname = re.findall(r'</a></td><tdstyle="display:none;">.*?</td><td>(.*)</td><td>.*</td><td>.*</td><td>.*</td><td>.*</td><tdstyle="display:none">',eachone)[0]
    x = str(sname+name)
    list.append(x)
print(list)
