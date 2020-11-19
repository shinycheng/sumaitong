import re
import json
import requests
import pandas as pd

#构建产品url、spm
print("输入产品id：")
productId =input()
countrys = ["RU",
"US",
"CA",
"ES",
"FR",
"UK",
"NL",
"IL",
"BR",
"CL",
"AU",
"UA",
"BY",
"JP",
"TH",
"SG",
"KR",
"ID",
"MY",
"PH",
"VN",
"IT",
"DE",
"SA",
"AE",
"PL",
"TR",
"PT"
]
list = []
spm = 'a2g0o.store_home.smartLeaderboard_92859956.'+productId
url = 'https://www.aliexpress.com/item/'+productId+'.html'


for i in range(len(countrys)):
    country = countrys[i]
    aep_usuc_f ='isfm=y&site=glo&c_tp=USD&x_alimid=242241330&iss=y&s_locale=zh_CN&region='+country+'&b_locale=en_US'
    cookies = {
        'ali_apache_id': '11.180.122.25.1590413831636.233412.0',
        'cna': 'CLhSFwH4MmcCATyxVFFC+YKD',
        '_bl_uid': 'X6k2naXImR1jL0bzmz7Rq3zrkF0w',
        '_ga': 'GA1.2.57210478.1590413834',
        'aep_common_f': 'mDtIp9CrgzENqa+IZhfyCtiouYyIw14Pd4LcNigtdzFzLaboM1Qcng==',
        'ae-msite-city': '',
        'ae-msite-province': '',
        '_lang': 'zh_CN',
        '_fbp': 'fb.1.1604130214911.337659290',
        'ali_apache_track': 'mt=2|mid=cn1532108722sapg',
        'intl_locale': 'en_US',
        'XSRF-TOKEN': 'bda4e7aa-22d5-48e9-9927-7716d61024a3',
        'ali_apache_tracktmp': '',
        'havana_tgc': 'eyJjcmVhdGVUaW1lIjoxNjA0NTQzNzc1NjM5LCJsYW5nIjoiemhfQ04iLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDgwOTYxMzgyMTYsInRndElkIjoiMTNRV1o0LXNjNXFPbkVBSlJLWmVIaVEifX19fQ',
        '_hvn_login': '13',
        'aep_usuc_t': 'ber_l=A0',
        'xman_f': 'WZEkqb/p/Su/CxEycW31S5KAZ60/kFl+TJbGYRzSRQykB3MwN7daY4a1uxJbZCGq50iUZcRsM5wk9x2Om49kJsPE7wd8GNAVISrVe/mmebOljmX9tk5+gkQewP27S3CsBQWOP58mCxagm6s5SobY8eSQJmerp3E2VjWYvWtQiYH02F835p6U2yWog0nCbDpm8n6YZcXL2as11Ez6GlDF8i3v91M/GhX3CCWc5SwW3bBvHrCvlgW9q5+wY3ldG8NYje6laU96newdIMQ1kypsShEiXmFlGbol6gXoPU5Yg1krF7gegocFu40PqXxKCJbz/iLOvSPAAS/WtfKJrQMtE7hqOIEJfqoR/8QgQNoFLcWJWetLpCwoAV+YnVg3QEhgqv315/Old66NpR1YkrdV/4SH0b+Ys/L59UvqiNnp/Zkzvv80hc9Fey5ZePBNN20c',
        'acs_usuc_t': 'x_csrf=1cbt0n0s68p2g&acs_rt=49d3a586703a425a8171214141ee4a14',
        'xman_t': 'gdO53s/kF6RdYwKD8zrAwy0jIokN6LGg72j/3xSCkXwWb3ChlkM0ZGeD7/Q/2wiD',
        'aep_usuc_f': aep_usuc_f,
        'intl_common_forever': 'WRD0nzcjGMSDMCbUWjIC6xw8bEk6xUvgkbsLkQAYaiqSq/u141pZZQ==',
        '_m_h5_tk': 'ec1c03a2232fa7029dddff9453dc3046_1604572807123',
        '_m_h5_tk_enc': 'a719077f174e7cdc43ece7b55a146e7c',
        'JSESSIONID': 'ABF4F0EDDA79668AD3C9CC2FB041A055',
        'aep_history': 'keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005001484666692%091005001389808485%0932961034907%091005001667875263%094000114526864%094000124111607%094000166899970%094000166899970',
        'tfstk': 'crKhBsOWF1Nfzy_MlDsBHqGpQykOCN2N9QRBbho9Rzb2suc2Bw50VPz2zYgGsBx8P',
        'l': 'eBO7cchmQeDU6wTkBOfwlurza77tYIRxMuPzaNbMiOCP_jf95ZLPBZSP2j8pCnGVhs_MR3kpoqnuBeYBchxMzpbk-UyzYVMmn',
        'isg': 'BDQ0Rkdc18FIrkJgtI1DzhwqBfSmDVj3-97zL86VmL9DOdSD9hxSh97zuXHhl5BP',
        'xman_us_f': 'zero_order=y&x_locale=en_US&x_l=1&last_popup_time=1590495451952&x_user=CN|null|null|cnfm|242241330&no_popup_today=n&x_lid=cn1532108722sapg&x_c_chg=0&x_c_synced=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1604196169079%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=a4d1fc34026042d7b6480fcd59a2ba5c',
    }
    headers = {
        'authority': 'www.aliexpress.com',
        'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
    }
    params = (
        ('gps-id', 'pcStoreLeaderboard'),
        ('scm', '1007.22922.122102.0'),
        ('scm_id', '1007.22922.122102.0'),
        ('scm-url', '1007.22922.122102.0'),
        ('pvid', '0f1f8141-dedf-4195-b040-38c5a149a2a3'),
        ('spm', spm),
    )
    response = requests.get(url, headers=headers, params=params, cookies=cookies)


    r = response.text.replace('\t','').replace('\n','').replace(' ','')
    #json格式文本
    data = re.findall(r'window.runParams=.*?data:(.*?),csrfToken:',r)[0]
    data_json = json.loads(data)
    skuModule = data_json['skuModule']
    #商品属性列表
    productSKUPropertyList_dict = {}
    productSKUPropertyList = skuModule['productSKUPropertyList']
    for i in range(len(productSKUPropertyList)):
        skuPropertyName = productSKUPropertyList[i]['skuPropertyName']
        skuPropertyValues = productSKUPropertyList[i]['skuPropertyValues']
        skuPropertyId = productSKUPropertyList[i]['skuPropertyId']
        productSKUPropertyList_dict[skuPropertyId] = skuPropertyName #200009720 = Lengh
        for i in range(len(skuPropertyValues)):
            propertyValueDisplayName = skuPropertyValues[i]['propertyValueDisplayName']
            propertyValueId = skuPropertyValues[i]['propertyValueId']
            productSKUPropertyList_dict[propertyValueId] = propertyValueDisplayName #201484780 = 25FT-7.5MExtended
    #商品价格列表
    skuPriceList = skuModule['skuPriceList']
    product_dict = {}
    for i in range(len(skuPriceList)):
        skuAttr = skuPriceList[i]['skuAttr']
        skuAttr_skuName = re.findall(r'(\d+):',skuAttr)
        skuAttr_skuValueId = re.findall(r':(\d+)',skuAttr)
        freightExt = skuPriceList[i]['freightExt']
        price = re.findall(r'{"p0":".*?","p1":"(.*?)",', freightExt)[0]
        product_dict['country'] = country
        product_dict['price'] = price
        for i in range(len(skuAttr_skuName)):
            name = productSKUPropertyList_dict[int(skuAttr_skuName[i])]
            value = productSKUPropertyList_dict[int(skuAttr_skuValueId[i])]
            product_dict[name] = value
        df =pd.DataFrame(product_dict,index= [1])
        list.append(df)
        print(product_dict)
df = pd.concat(list)
df.to_excel(r'价格.xlsx')








