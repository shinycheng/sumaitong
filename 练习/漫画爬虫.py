import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
download_header = {
    'Referer': 'https://www.dmzj.com/view/yaoshenji/41917.html'
}

cookies = {
    'first_h_kp': '1606230008433',
    'count_h_kp': '1',
    'first_m_kp': '1606230008435',
    'count_m_kp': '1',
    '__music_index__': '1',
    '2756_2327_115.216.98.120': '1',
    'UM_distinctid': '175fa5149595fd-03df7c7259f49d-326f7907-13c680-175fa51495ab3e',
    'display_mode': '0',
    'pic_style': '0',
    'setUp': '0',
    'show_tip_1': '0',
    '2756_2326_115.216.98.120': '1',
    '2756_2328_115.216.98.120': '1',
    'CNZZDATA1000465408': '931696067-1606220209-%7C1606225609',
    'CNZZDATA1253965819': '760886324-1606217362-%7C1606228168',
    'fixedview_2756': 'H7csklj6BJ%252Fh7itVfr2rzxVoR49CYzIppqZiRuqferg%252F2Ss09%252Fgsk6lb0lhpZKEQx1aQYWetWu4wcd98F7lQvPaUvHHUz0P9zjyCKf4T8OQ%252Fr4Bb7cJn7S8q61jlfQzND5MqprhQ0GJtwGdKTPA85zBpQxAP99RDe7Yu4q%252FCMWa47PnrXkruYiNN8SmlZFQEJjEiQSjJ3mdImr4AbCWX74WNjLoXr%252FPF4xHq2oBqx7DXzKADf2EMgPM3nu82KPJGtDtX63Co6o8Z8BZ2NPhrUivybqnZiqETxAgkTzERMxw5Ro4iD1RqVOdiAZfe3AMp3DrnKbtl3PLYVB8RZGasWA%253D%253D',
}
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.dmzj.com/view/yaoshenji/41919.html',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
}
response = requests.get('https://www.dmzj.com/info/yaoshenji.html', headers=headers, cookies=cookies)
soup = BeautifulSoup(response.text,'lxml')
btid = soup.find('ul',class_="list_con_li autoHeight")
id = re.findall(r'<a href="https://www.dmzj.com/view/yaoshenji/(\d+).html"',str(btid))
id.reverse()
bt = re.findall(r'title="(.*?)\d+-\d+-\d+">',str(btid))
bt.reverse()
for i in range(len(id)):
    url = 'https://www.dmzj.com/view/yaoshenji/' +id[i] +'.html'
    cookies = {
        'first_h_kp': '1606222432357',
        'first_m_kp': '1606222432358',
        '__music_index__': '2',
        'count_h_kp': '6',
        'count_m_kp': '6',
        '2756_2327_115.216.98.120': '1',
        'UM_distinctid': '175fa5149595fd-03df7c7259f49d-326f7907-13c680-175fa51495ab3e',
        'CNZZDATA1000465408': '931696067-1606220209-%7C1606220209',
        'CNZZDATA1253965819': '760886324-1606217362-%7C1606217362',
        'display_mode': '0',
        'pic_style': '0',
        'setUp': '0',
        'show_tip_1': '0',
        '2756_2326_115.216.98.120': '1',
        '2756_2328_115.216.98.120': '1',
        'fixedview_2756': 'jndYUndkWwhfba24c2FVrLLIwat11TOBWzzEluGF0GPShD9vW2Z4csCkslZ8ME2R4tdFSonhQ7ui9JeA%252BbfqKGBNVlW2hnZ3vl9C6y6DNyyp3kbvaCXM76IK2LuohZhZRynPVZd4afSS0wWZPTnZXuxtCqTQEePHBKIeHxUP0EjeWVciyZ%252BxJnHm7Xnhm27Ur30KjKWmEdjJ5FjY%252FCfxrkyRDaGqwBiSv7%252F%252BNc0zVeyij0JJpbCzzrWEo8%252BxxbgQwBFrnv8Io4gNpsa8T%252BaEtdGtk6cGO8Cuqcdn3iLGtVnOU4%252B7uEBGxXGIhSWo9FG7rpxFiY2XRDm8M5LVVPVN4w%253D%253D',
    }
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.dmzj.com/view/yaoshenji/41917.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
    }
    response = requests.get(url, headers=headers, cookies=cookies,stream=True)
    r = response.text
    soup = BeautifulSoup(r, 'lxml')
    img = soup.find('script', type="text/javascript")
    img1 = re.findall('\d{5}', str(img))[0]
    img2 = re.findall('\d{13,}', str(img))

    for i in range(len(img2)):
        if len(img2[i]) == 13:
            img2[i] = int(img2[i])*10
    img2 = sorted(img2,key=lambda x:int(x))
    for j in range(len(img2)):

        if str(img2[j])[-1] == '0':
            img2[j] = str(img2[j])[:-1]
        link ='https://images.dmzj.com/img/chapterpic/3059/'+str(img1)+'/'+str(img2[j])+'.jpg'
        headers = {
            'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
            'Referer': 'https://www.dmzj.com/',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        }
        response = requests.get(str(link), headers=headers)

        with open(r'/Users/zhanghang/Desktop/妖神记/'+str(img2[j])+'.jpg','wb') as f:
            for i in response.iter_content():
                f.write(i)
