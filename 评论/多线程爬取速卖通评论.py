import requests
import re
import requests
from bs4 import BeautifulSoup
import threading
import queue

#需要输入的参数
productId=4001194049725
ownerMemberId=201975727
companyId=214510452

# 获取总页数
def comment_page(productId,ownerMemberId,companyId):
    cookies = {
        'ali_apache_id': '11.180.122.25.1590413831636.233412.0',
        'cna': 'CLhSFwH4MmcCATyxVFFC+YKD',
        '_ga': 'GA1.2.57210478.1590413834',
        'aep_common_f': 'mDtIp9CrgzENqa+IZhfyCtiouYyIw14Pd4LcNigtdzFzLaboM1Qcng==',
        'ae-msite-city': '',
        'ae-msite-province': '',
        '_lang': 'zh_CN',
        '_fbp': 'fb.1.1604130214911.337659290',
        'ali_apache_track': 'mt=2|mid=cn1532108722sapg',
        'intl_locale': 'en_US',
        'intl_common_forever': '97EKFUjJUdvCD00XAB7q3yST5ijjlIj9j8rz53TnRdCcG44ZTQBy0w==',
        '_m_h5_tk': '90d734c057c8d63526947a09ea944fde_1604552141827',
        '_m_h5_tk_enc': '5be4b0cd1143fcafe38245c2e34638c9',
        'xlly_s': '1',
        'ali_apache_tracktmp': '',
        '_gid': 'GA1.2.2050648121.1604542423',
        'aep_history': 'keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%094000166899970%091005001484666692%091005001389808485%0932961034907%091005001667875263%094000114526864%094000124111607%094000166899970',
        'havana_tgc': 'eyJjcmVhdGVUaW1lIjoxNjA0NTQzNzc1NjM5LCJsYW5nIjoiemhfQ04iLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDgwOTYxMzgyMTYsInRndElkIjoiMTNRV1o0LXNjNXFPbkVBSlJLWmVIaVEifX19fQ',
        '_hvn_login': '13',
        'aep_usuc_f': 'site=glo&region=AF&b_locale=en_US&iss=y&s_locale=zh_CN&isfm=y&c_tp=USD&x_alimid=242241330',
        'aep_usuc_t': 'ber_l=A0',
        'xman_f': 'WZEkqb/p/Su/CxEycW31S5KAZ60/kFl+TJbGYRzSRQykB3MwN7daY4a1uxJbZCGq50iUZcRsM5wk9x2Om49kJsPE7wd8GNAVISrVe/mmebOljmX9tk5+gkQewP27S3CsBQWOP58mCxagm6s5SobY8eSQJmerp3E2VjWYvWtQiYH02F835p6U2yWog0nCbDpm8n6YZcXL2as11Ez6GlDF8i3v91M/GhX3CCWc5SwW3bBvHrCvlgW9q5+wY3ldG8NYje6laU96newdIMQ1kypsShEiXmFlGbol6gXoPU5Yg1krF7gegocFu40PqXxKCJbz/iLOvSPAAS/WtfKJrQMtE7hqOIEJfqoR/8QgQNoFLcWJWetLpCwoAV+YnVg3QEhgqv315/Old66NpR1YkrdV/4SH0b+Ys/L59UvqiNnp/Zkzvv80hc9Fey5ZePBNN20c',
        'xman_us_f': 'zero_order=y&x_locale=en_US&x_l=1&last_popup_time=1590495451952&x_user=CN|null|null|cnfm|242241330&no_popup_today=n&x_lid=cn1532108722sapg&x_c_chg=0&x_c_synced=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1604196169079%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=a4d1fc34026042d7b6480fcd59a2ba5c',
        'acs_usuc_t': 'x_csrf=1cbt0n0s68p2g&acs_rt=49d3a586703a425a8171214141ee4a14',
        'xman_t': 'gdO53s/kF6RdYwKD8zrAwy0jIokN6LGg72j/3xSCkXwWb3ChlkM0ZGeD7/Q/2wiD',
        'JSESSIONID': '1259C25E6125521C953AB954750134C1',
        'isg': 'BFRUAut296TP42KAVC2jLvzKJZTGrXiX2z4Tz-41IF942fUjFr_hJbsf2NHBbLDv',
        'tfstk': 'cTe5BA0f8ye2zC1eUusq4Ksvb3DCZiXmmM0bV7Fgr19BD8Z5im9Z5hZShUJx6m1..',
        'l': 'eBO7cchmQeDU6vysBO5ahurza77OwIRb8NFzaNbMiInca1R19tjXvNQVmbSHWdtxgt5mtetrpE0xqReyW84T-xsjvKhEvQHQmpJ68e1..',
    }
    headers = {
        'authority': 'feedback.aliexpress.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://feedback.aliexpress.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://feedback.aliexpress.com/display/productEvaluation.htm',
        'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
    }
    data = {
        'ownerMemberId': str(ownerMemberId),
        'memberType': 'seller',
        'productId': str(productId),
        'companyId': str(companyId),
        'evaStarFilterValue': 'all Stars',
        'evaSortValue': 'sortdefault@feedback',
        'page': '1',
        'currentPage': '3',
        'startValidDate': '',
        'i18n': 'true',
        'withPictures': 'false',
        'withPersonalInfo': 'false',
        'withAdditionalFeedback': 'false',
        'onlyFromMyCountry': 'false',
        'version': '',
        'isOpened': 'true',
        'translate': ' Y ',
        'jumpToTop': 'true',
        'v': '2'
    }
    response = requests.post('https://feedback.aliexpress.com/display/productEvaluation.htm', headers=headers,cookies=cookies, data=data)
    soup = BeautifulSoup(response.text, 'lxml')
    page = soup.find('div', class_="customer-reviews")
    page = re.findall(r'<div class="customer-reviews">Customer Reviews (.*?)</div>', str(page))[0].replace('(','').replace(')', '')
    page = int(int(page) / 10) + 2
    return page
#多线程类
class Mythread(threading.Thread):
    def __init__(self,name,productId,ownerMemberId,companyTd,p):
        threading.Thread.__init__(self)
        self.name = name
        self.productId = productId
        self.ownerMemberId = ownerMemberId
        self.companyId = companyTd
        self.p = p
    def run(self):
        print("start",self.name)
        while True:
            try:
                all_comments(self.name,self.productId,self.ownerMemberId,self.companyId,self.p)
            except Exception as e:
                print(e)
                break

def all_comments(name,productId,ownerMemberId,companyTd,p):
    # 定义评论用户信息
    name_dict = {}
    page = p.get(timeout = 2)
    cookies = {
        'ali_apache_id': '11.180.122.25.1590413831636.233412.0',
        'cna': 'CLhSFwH4MmcCATyxVFFC+YKD',
        '_ga': 'GA1.2.57210478.1590413834',
        'aep_common_f': 'mDtIp9CrgzENqa+IZhfyCtiouYyIw14Pd4LcNigtdzFzLaboM1Qcng==',
        'ae-msite-city': '',
        'ae-msite-province': '',
        '_lang': 'zh_CN',
        '_fbp': 'fb.1.1604130214911.337659290',
        'ali_apache_track': 'mt=2|mid=cn1532108722sapg',
        'intl_locale': 'en_US',
        'intl_common_forever': '97EKFUjJUdvCD00XAB7q3yST5ijjlIj9j8rz53TnRdCcG44ZTQBy0w==',
        '_m_h5_tk': '90d734c057c8d63526947a09ea944fde_1604552141827',
        '_m_h5_tk_enc': '5be4b0cd1143fcafe38245c2e34638c9',
        'xlly_s': '1',
        'ali_apache_tracktmp': '',
        '_gid': 'GA1.2.2050648121.1604542423',
        'aep_history': 'keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%094000166899970%091005001484666692%091005001389808485%0932961034907%091005001667875263%094000114526864%094000124111607%094000166899970',
        'havana_tgc': 'eyJjcmVhdGVUaW1lIjoxNjA0NTQzNzc1NjM5LCJsYW5nIjoiemhfQ04iLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDgwOTYxMzgyMTYsInRndElkIjoiMTNRV1o0LXNjNXFPbkVBSlJLWmVIaVEifX19fQ',
        '_hvn_login': '13',
        'aep_usuc_f': 'site=glo&region=AF&b_locale=en_US&iss=y&s_locale=zh_CN&isfm=y&c_tp=USD&x_alimid=242241330',
        'aep_usuc_t': 'ber_l=A0',
        'xman_f': 'WZEkqb/p/Su/CxEycW31S5KAZ60/kFl+TJbGYRzSRQykB3MwN7daY4a1uxJbZCGq50iUZcRsM5wk9x2Om49kJsPE7wd8GNAVISrVe/mmebOljmX9tk5+gkQewP27S3CsBQWOP58mCxagm6s5SobY8eSQJmerp3E2VjWYvWtQiYH02F835p6U2yWog0nCbDpm8n6YZcXL2as11Ez6GlDF8i3v91M/GhX3CCWc5SwW3bBvHrCvlgW9q5+wY3ldG8NYje6laU96newdIMQ1kypsShEiXmFlGbol6gXoPU5Yg1krF7gegocFu40PqXxKCJbz/iLOvSPAAS/WtfKJrQMtE7hqOIEJfqoR/8QgQNoFLcWJWetLpCwoAV+YnVg3QEhgqv315/Old66NpR1YkrdV/4SH0b+Ys/L59UvqiNnp/Zkzvv80hc9Fey5ZePBNN20c',
        'xman_us_f': 'zero_order=y&x_locale=en_US&x_l=1&last_popup_time=1590495451952&x_user=CN|null|null|cnfm|242241330&no_popup_today=n&x_lid=cn1532108722sapg&x_c_chg=0&x_c_synced=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1604196169079%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=a4d1fc34026042d7b6480fcd59a2ba5c',
        'acs_usuc_t': 'x_csrf=1cbt0n0s68p2g&acs_rt=49d3a586703a425a8171214141ee4a14',
        'xman_t': 'gdO53s/kF6RdYwKD8zrAwy0jIokN6LGg72j/3xSCkXwWb3ChlkM0ZGeD7/Q/2wiD',
        'JSESSIONID': '1259C25E6125521C953AB954750134C1',
        'isg': 'BFRUAut296TP42KAVC2jLvzKJZTGrXiX2z4Tz-41IF942fUjFr_hJbsf2NHBbLDv',
        'tfstk': 'cTe5BA0f8ye2zC1eUusq4Ksvb3DCZiXmmM0bV7Fgr19BD8Z5im9Z5hZShUJx6m1..',
        'l': 'eBO7cchmQeDU6vysBO5ahurza77OwIRb8NFzaNbMiInca1R19tjXvNQVmbSHWdtxgt5mtetrpE0xqReyW84T-xsjvKhEvQHQmpJ68e1..',
    }
    headers = {
        'authority': 'feedback.aliexpress.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://feedback.aliexpress.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://feedback.aliexpress.com/display/productEvaluation.htm',
        'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
    }
    data = {
        'ownerMemberId': str(ownerMemberId),
        'memberType': 'seller',
        'productId': str(productId),
        'companyId': str(companyId),
        'evaStarFilterValue': 'all Stars',
        'evaSortValue': 'sortdefault@feedback',
        'page': str(page),
        'currentPage': '3',
        'startValidDate': '',
        'i18n': 'true',
        'withPictures': 'false',
        'withPersonalInfo': 'false',
        'withAdditionalFeedback': 'false',
        'onlyFromMyCountry': 'false',
        'version': '',
        'isOpened': 'true',
        'translate': ' Y ',
        'jumpToTop': 'true',
        'v': '2'
    }
    response = requests.post('https://feedback.aliexpress.com/display/productEvaluation.htm', headers=headers,cookies=cookies, data=data)
    soup = BeautifulSoup(response.text, 'lxml')
    # 单页评论信息
    comments = soup.find_all('div', class_='feedback-item clearfix')
    for comment in comments:
        user_country = comment.find_all('div', class_="user-country")
        user_info = comment.find('div', class_="user-order-info")
        comment_time = comment.find('span',class_="r-time-new")
        country = re.findall('<b class="css_flag css.*?">(.*?)</b>', str(user_country))
        name = re.findall(r'<strong>(.*?):</strong>', str(user_info))
        name_dict['country'] = country[0]
        for i in range(len(name)):
            name_dict[name[i]] = re.findall(r'<strong>' + str(name[i]) + ':</strong>(.*?)</span>',str(user_info).replace(' ', '').replace('\n', '').replace('\t',''))[0]
        comment_time = re.findall(r'<span class="r-time-new">(.*?)</span>',str(comment_time))
        name_dict['time'] = comment_time[0]
        print(name_dict)

pages = comment_page(productId,ownerMemberId,companyId)
Thread_list = ["Thread1","Thread2","Thread3","Thread4","Thread5","Thread6","Thread7","Thread8","Thread9","Thread10","Thread11","Thread12","Thread13","Thread14","Thread15","Thread16","Thread17","Thread18","Thread19","Thread20"]
workqueue = queue.Queue(pages)
Threads = []
for i in Thread_list:
    thread = Mythread(i,productId,ownerMemberId,companyId,workqueue)
    thread.start()
    Threads.append(thread)
for i in range(1,pages+1):
    workqueue.put(i)
for i in Threads:
    i.join()