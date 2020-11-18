from multiprocessing import Process, Queue
import time
import requests
import re
f_list = []
with open(r'alexa.txt','r') as f:
    f = f.readlines()
    for i in f:
        i = re.findall(r'\d+\t(.*)',i)[0]
        f_list.append(i)
start = time.time()
class MyProcess(Process):
    def __init__(self,q):
        Process.__init__(self)
        self.q = q
    def run(self):
        print("start",self.pid)
        while not self.q.empty():
            crew(self.q)
        print("exit",self.pid)
def crew(q):
    url = q.get(timeout=2)
    r = requests.get(url)
    print(r.status_code,url)
if __name__ == '__main__':
    workqueue = Queue(1000)
    for url in f_list:
        workqueue.put(url)
    for i in range(0,16):
        p = MyProcess(workqueue)
        p.daemon =True
        p.start()
        p.join()
    end = time.time()
    print("time",end-start)