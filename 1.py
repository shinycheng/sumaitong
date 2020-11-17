import threading
import requests
import re
import time
f_list = []
link_list = [(0,200),(201,400),(401,600),(601,800),(801,1000)]
with open(r'alexa.txt','r') as f:
    f = f.readlines()
    for i in f:
        i = re.findall(r'\d+\t(.*)',i)[0]
        f_list.append(i)
start = time.time()
class Mythread(threading.Thread):
    def __init__(self,name,link):
        threading.Thread.__init__(self)
        self.name = name
        self.link = link
    def run(self):
        print("Start",self.name)
        crew(self.name,self.link)
        print("Exit",self.name)
def crew(name,link):
    for i in range(link[0],link[1]+1):
        r = requests.get(f_list[i])
        print(name,r.status_code,f_list[i])


threads = []
for i in range(len(link_list)):
    link = link_list[i]
    thread = Mythread("Thread"+str(i+1),link)
    thread.start()
    threads.append(thread)
for i in threads:
    i.join()
end = time.time()
print("time",end-start)



