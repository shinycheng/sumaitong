import requests

cookies = {
    'PHPSESSID': 'cm1qm3vqmapa7rq2l6f7su1bm3',
    'UM_distinctid': '17609f6dd50474-062ed937f49b1-16144b58-1fa400-17609f6dd515cf',
    'CNZZDATA1263424981': '1033893872-1606481598-%7C1606481598',
    'mac_history': '%7Bvideo%3A%5B%7B%22name%22%3A%22%u73AF%u592A%u5E73%u6D0B%22%2C%22link%22%3A%22/%3Fm%3Dvod-detail-id-4782.html%22%2C%22typename%22%3A%22%u79D1%u5E7B%u7247%22%2C%22typelink%22%3A%22/%3Fm%3Dvod-type-id--pg-1.html%22%2C%22pic%22%3A%22upload/vod/2017-12/151438897310.jpg%22%7D%2C%7B%22name%22%3A%22%u73AF%u5927%u897F%u6D0B%22%2C%22link%22%3A%22/%3Fm%3Dvod-detail-id-10962.html%22%2C%22typename%22%3A%22%u79D1%u5E7B%u7247%22%2C%22typelink%22%3A%22/%3Fm%3Dvod-type-id--pg-1.html%22%2C%22pic%22%3A%22upload/vod/2018-03/152215280215.jpg%22%7D%5D%7D',
}
headers = {
    'Proxy-Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://www.jisudhw.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://www.jisudhw.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
}
params = (
    ('m', 'vod-search'),
)
data = {
  'wd': '\u73AF\u592A\u5E73\u6D0B',
  'submit': 'search'
}
response = requests.post('http://www.jisudhw.com/index.php', headers=headers, params=params, cookies=cookies, data=data, verify=False)
print(response.text)