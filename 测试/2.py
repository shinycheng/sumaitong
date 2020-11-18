import threading
import requests
import time
import re
link_list = []
with open('alexa.txt','r') as f:
    f_list = f.readlines()
    for i in f_list:
        link = re.findall(r'\d+(.*)',i)[0].replace('\t','')
        link_list.append(link)
start = time.time()
for i in link_list:
    r = requests.get(i)
    print( r.status_code,i)
end =time.time()
print('总共花费',end-start)