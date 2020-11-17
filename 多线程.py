import re
import time
import requests
import threading
import queue
f_list = []
with open(r'alexa.txt','r') as f:
    f = f.readlines()
    for i in f:
        i = re.findall(r'\d+\t(.*)',i)[0]
        f_list.append(i)
start = time.time()
class Mythread(threading.Thread):
    def __init__(self,name,a):
        threading.Thread.__init__(self)
        self.name = name
        self.a = a
    def run(self):
        print("start",self.name)
        while True:
            try:
                crew(self.name,self.a)
            except:
                break
        print("end",self.name)

def crew(name,a):
    url = a.get(timeout = 2)
    r = requests.get(url)
    print(name,r.status_code,url)

Thread_list = ["Thread1","Thread2","Thread3","Thread4","Thread5"]
workqueue = queue.Queue(1000)
Threads = []
for i in Thread_list:
    thread = Mythread(i,workqueue)
    thread.start()
    Threads.append(thread)
for url in f_list:
    workqueue.put(url)
for i in Threads:
    i.join()

end = time.time()
print("time",end-start)




