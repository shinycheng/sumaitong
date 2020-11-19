import requests
import json
import time
import pandas as pd
cookies = {
    'ali_apache_id': '11.134.216.25.1600073409124.416382.1',
    'cna': 'wRzmFzPlABgCAXrqDvimynu3',
    'aep_common_f': 't2YVGFhCDVHj6ccVWGXh3GvjD7O9gH5oyspNr6HF9qF8TvwlTe6yPA==',
    '_ga': 'GA1.2.1793992446.1600076572',
    '_bl_uid': '04ks8fkt2smf4b2Cmfp0bb8yjaCp',
    '_fbp': 'fb.1.1600081258112.1037710499',
    'UM_distinctid': '17492994b80823-0a2dd2d141046e-333769-1fa400-17492994b8110e1',
    '__utma': '3375712.1793992446.1600076572.1600695971.1600695971.1',
    '__utmz': '3375712.1600695971.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'af_ss_a': '1',
    'af_ss_b': '1',
    '_lang': 'zh_CN',
    '_gid': 'GA1.2.87036607.1604829555',
    'xlly_s': '1',
    '_m_h5_tk': '0cbb33cd31eaaeabd7d17c428d06b28e_1604912571755',
    '_m_h5_tk_enc': 'a11078896b6c51a89bc7b3638e3d51ff',
    'acs_usuc_t': 'acs_rt=28abcffaf5234cc0a8c26337a60e49cd&x_csrf=q9is2svl25eu',
    'havana_tgc': 'eyJjcmVhdGVUaW1lIjoxNjA0OTA0NTI0OTY5LCJsYW5nIjoiemhfQ04iLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDgwOTYxMzgyMTYsInRndElkIjoiMXRMTHFWZXdvM0E0ck5YdXNBVGZueHcifX19fQ',
    '_hvn_login': '13',
    'xman_us_t': 'x_lid=cn1532108722sapg&sign=y&rmb_pp=yolocity_001@163.com&x_user=YIN5SEciKlOt02QyptvISG3HJYdt2UVolmB/n3m6Mak=&ctoken=ka_0udm9a3k4&need_popup=y&l_source=aliexpress',
    'aep_usuc_t': 'ber_l=A0',
    'xman_f': '0a/9ygc3JdF5OKWNS83Ws23Yhfp7b2MarY0nRgzt9VFk7P3EPEFL/70qX24KoNt61aO5x/B1pl/muI07q1zX9EBxPIW5xbS/NGjuDPB9GzRxHBTl6OKuY1Ocw/+uQm83VaW3QSZmVD2x83C+/yptYZQP0e/KBxtBtkIAzRJxjDXfCmT8d5E+MmAmEYQMXRZlgx4WA/ZjVciHYx4RFAVU2IC02uNt++mEXZ6oyqJ2fjb0EUTVyMjY3Q52uY7D7nCrV4m+u1vLm0saNDj9ybqbFevFJiehJ9JvQj5129KffMwp1mYoX6wwwv9KoyPExP84KpU8WQSJ0ovN3JvV2LLhULceLZwe/w3XbA8hul1/wH7sZxh1xMblTqimwcb74pvqFer9vvIZoJmqCy2m5Rb106jMNFw+11RccsUvhWtsp8UhFbxDul8xDnwoTZcbfDZY',
    'ali_apache_tracktmp': 'W_signed=Y',
    'intl_locale': 'en_US',
    'XSRF-TOKEN': 'ba58a4e1-f3ac-47f8-9011-17c15954cac0',
    'ali_apache_track': 'mt=2|ms=|mid=cn1532108722sapg',
    'aep_usuc_f': 'isfm=y&site=glo&province=&city=&c_tp=USD&x_alimid=242241330&iss=y&s_locale=zh_CN&region=CA&b_locale=en_US',
    'intl_common_forever': 'jnzAKQZPWRkZ0curxDnxQYvZmGwIylW4yQSRBD2NVNZcNQ7dXrWCrQ==',
    'xman_us_f': 'zero_order=y&x_locale=en_US&x_l=1&last_popup_time=1600073413668&x_user=CN|null|null|cnfm|242241330&no_popup_today=n&x_lid=cn1532108722sapg&x_c_chg=0&x_c_synced=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1604835175953%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=3de2e8b17de845a08dcd54a51d9946cf',
    'aep_history': 'keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005001667875263%091005001617950091%094000857368257%091005001617950091%091005001346393889%091005001617950091%091005001691045244%091005001691045244',
    'xman_t': '0OW5z237RMkL4XzIQQSvdsT/64i/+usU2dSl3tyy3EeaOGCuGpOitPrWjvsjcMmJG5z4e//fgg3fL/W2jvASheQIPKVYIQxmp3GfqIs6e9p36jClTX1MR5dFMn5Mpx/jPTwtExb9kQRvoJs4XnpZxTHdRf8ENNn+s0sIeLtgYnDHnw/6bO7B+JlJi11h0xZCH5UHtFw4BPjHzOUecF0sg31aQA7d6QymEbuRBA6hsAXmXVboVt2fxowuDOG1vCxGoUGJYDL9wp0xJiYSS/sgN9Vu2RiaDqAlBoKHAwhNOTlRGyZdRWhDHmytykfnA8xtYyl6g9ns+m1yT6ip04GpqhXbHfW5EI2R+pO746ASX3B9sZIw6SxfX9X+U7WEKoyMgIxsIJXDuoawmulNG/mLejtGyyKZZPSLkjAOsUVZQCny69L7C6QavttJWq9XQhjNaGSrXAIlL1U4Kh53f/ktsQKSTh0/OqMWkxVeikJcpC3z/10megjRtAOQ9KekCBBOF99V9NDuE2fMBY5AeiH6ezx/S/th5M8NRXq5Nzld2eITH9zGG4qfFiPs95FIyv249DhyduZLLHskRJkVN74gXVGRLyuxsIZhvPHxnOyks8qfs4t3DCp4mx0bu1k/gsrVH0K7x3oyVB+Nayi72bpM1uHsiBW1TkLF',
    'JSESSIONID': '226B6FD73F9A9332FB2B669BB27D0797',
    'tfstk': 'cZ8FBmsAd23eMR7SDw_zANAf1KpdaEOHZP5fx3r8ysPQ3rbA3sAze1cHm155HVjh.',
    'l': 'eB_StJ6rOz7KmzPjBO5wourza77tiLRf5sPzaNbMiInca69AgFh6eNQVXRxpzdtjgt5j0FKyGmkaaRFDJkz_WE9h_FhEZzskGKJMRe1..',
    'isg': 'BHNzKc64KLJCDeQRO4GcqlpAAnedqAdqfd-yqyUaShLgJJrGqHgruNny3lTKhF9i',
}
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
headers = {
    'authority': 'www.aliexpress.com',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.aliexpress.com/item/1005001691045244.html?spm=5261.ProductManageOnline.0.0.e7864edfRkTmFJ',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ru;q=0.6',
}
print("输入产品id：")
productId =input()
list = []
for i in range(len(countrys)):
    country = countrys[i]

    params = (
        ('productId', productId),
        ('count', '1'),
        ('minPrice', '46.96'),
        ('maxPrice', '49.11'),
        ('country', country),
        ('provinceCode', ''),
        ('cityCode', ''),
        ('tradeCurrency', 'USD'),
        ('sellerAdminSeq', '242241330'),
        ('userScene', 'PC_DETAIL_SHIPPING_PANEL'),
        ('displayMultipleFreight', 'false'),
        ('ext', '{"p1":"46.96","p2":"49.11","p3":"USD"}'),
    )

    response = requests.get('https://www.aliexpress.com/aeglodetailweb/api/logistics/freight', headers=headers, params=params, cookies=cookies)
    json_text = response.text
    json_text = json.loads(json_text)
    a_dict = {}
    try:
        freightResult = json_text['body']['freightResult']
        for i in range(len(freightResult)):
            company = freightResult[i]['company']
            freightAmount = freightResult[i]['freightAmount']['value']
            a_dict['country'] = country
            a_dict['company'] = company
            a_dict['price'] = freightAmount
            df = pd.DataFrame(a_dict, index=[1])
            list.append(df)
    except:
        a_dict['country'] = country
        a_dict['company'] = None
        a_dict['price'] = None
        df =pd.DataFrame(a_dict,index= [1])
        list.append(df)


df = pd.concat(list)
df = df.set_index(keys = 'country')
df_Not_duplicated = df[~df.index.duplicated()]
df_Duplicated_1 = df[df.index.duplicated()]
df_Duplicated_2 = df_Duplicated_1[df_Duplicated_1.index.duplicated()]
df_Duplicated_1 = df_Duplicated_1[~df_Duplicated_1.index.duplicated()]
df = pd.merge(df_Duplicated_1,df_Duplicated_2,how = 'left', on = 'country')
df = pd.merge(df_Not_duplicated, df,how= 'left', on = 'country')
df = df.fillna(' ')
df.to_excel(r'价格.xlsx')

