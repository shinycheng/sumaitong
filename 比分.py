from bs4 import BeautifulSoup
import re
import requests
cookies = {
    'ASP.NET_SessionId': 'anxam404nmfwywjxhecku0ox',
    'nw_sessionID': 'a7e07fc903634e94ba2fe963d1ccf51a',
    'Cookie': 'null',
    'UM_distinctid': '175adcee3191023-0c171afe24b14c-230346d-1fa400-175adcee31a8ff',
    'CNZZDATA1548435': 'cnzz_eid%3D1830697989-1604937612-%26ntime%3D1604937612',
    'Hm_lvt_6d1449e50f0f8c32ef85dd1332224afb': '1604938818',
    'CNZZDATA1637943': 'cnzz_eid%3D2016991888-1604934588-null%26ntime%3D1604940014',
    'nw_sessionIDToken': '39625597edd64db38a1956686cf95a51',
    'Hm_lpvt_6d1449e50f0f8c32ef85dd1332224afb': '1604941074',
}
headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://score.nowscore.com/odds/3in1Odds.aspx?companyid=23&id=1888095',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
}
params = (('companyid', '3'),('id', '1884782'),)

response = requests.get('http://score.nowscore.com/odds/3in1Odds.aspx', headers=headers, params=params, cookies=cookies, verify=False)
r = response.text
soup = BeautifulSoup(r,'lxml')
gta = soup.find('tr',class_='gt1')
zhu = re.findall('<td style="color:.*?;">(.*?)</td>',str(gta))
print(zhu)