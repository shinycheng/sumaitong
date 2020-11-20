import requests
import re
from bs4 import BeautifulSoup
a_dict = {}
f_list = ["SL+74%EF%BC%8D2019",
"SL+310%EF%BC%8D2019",
"GB51304-2018",
"GB+50433-2018",
"SL41-2018",
"GB51247-2018",
"GB50288-2018",
"SL253-2018",
"SL314-2018",
"SL282-2018",
"SL319-2018",
"SL303-2017",
"JJG%EF%BC%88%E6%B0%B4%E5%88%A9%EF%BC%89005-2017",
"SL252-2017",
"GB51177-2016",
"SL400-2016",
"SL265-2016",
"SL279-2016",
"GB50179-2015",
"SL714-2015",
"GB50071-2014",
"GB51018-2014",
"JJG%EF%BC%88%E6%B0%B4%E5%88%A9%EF%BC%89004-2015",
"SL702-2015",
"GB50201-2014",
"SL32-2014",
"SL62-2014",
"SL677-2014",
"SL644-2014",
"SL17-2014",
"GB50987-2014",
"SL655-2014",
"SL266-2014",
"SL275-2014",
"GB50199-2013",
"SL189-2013",
"SL623-2013",
"SL648-2013",
"SL642-2013",
"SL609-2013",
"SL645-2013",
"GB50286-2013",
"SL228-2013",
"SL575-2012",
"SL566-2012",
"SL561-2012",
"GB50773-2012",
"SL462-2012",
"GB50707-2011",
"GB50706-2011",
"SL229-2011",
"SL511-2011",
"SL318-2011",
"SL482-2011",
"SL486-2011",
"SL492-2011",
"GB50265-2010",
"SL485-2010",
"GB50599-2010",
"SL166-2010",
"JJG%EF%BC%88%E6%B0%B4%E5%88%A9%EF%BC%89003-2009",
"JJG%EF%BC%88%E6%B0%B4%E5%88%A9%EF%BC%89002-2009",
"JJG%EF%BC%88%E6%B0%B4%E5%88%A9%EF%BC%89001-2009",
"SL290-2009",
"GB50487-2008",
"SL443-2009",
"SL191-2008",
"SL430-2008",
"SL223-2008",
"SL401-2007",
"SL399-2007",
"SL398-2007",
"SL377-2007",
"SL378-2007",
"SL176-2007",
"SL386-2007",
"SL379-2007",
"GB50501-2007",
"SL326-2005",
"SL188-2005",
"SL311-2004",
"SL302-2004",
"SL291-2003",
"SL289-2003",
"SL285-2003",
"SL281-2003",
"SL276-2002",
"SL274-2001",
"GB18523-2001",
"SL168-2012",
"SL171-96",
"SL47-94",
"SL53-94"
]
import requests
for i in range(len(f_list)):
    cookies = {
        'wdcid': '1e844a8c45e21481',
        'zhuzhan': '44186949',
        'JSESSIONID': '6442656D46D5C5710C09FBCEB9102D42',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://zwgk.mwr.gov.cn/jsp/yishenqing/appladd/bzsearch.jsp',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
    }

    params = (
        ('bzbh', f_list[i]),
    )

    response = requests.get('http://zwgk.mwr.gov.cn/jsp/yishenqing/appladd/biaozhunfile/detail.jsp', headers=headers, params=params, cookies=cookies, verify=False)
    soup = BeautifulSoup(response.text,'lxml')
    book = soup.find('div',class_='detail')
    bianhao = re.findall(r'标准编号：(.*?) </h1>',str(book))[0]
    name = re.findall(r'中文标准名称：</span> (.*?) </li>',str(book))[0]
    id = re.findall('biaozhunfile/flash/pdf/\"\+\(\"(.*?)\"\)\+\"\.pdf\"\)',str(response.text.replace('\n','').replace('\t','').replace(' ','')))[0]
    a_dict[id] = bianhao+name+id
    print(name)
