from asyncio import threads
import threading
import datetime

Flag=0

class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threaID=counter
        self.name=name
        self.counter=counter

    def run(self):
        print("Starting "+self.name)
        threadLock.acquire()
        print_date(self.name,self.counter)
        threadLock.release()
        print("Exit: "+self.name)
    
def print_date(threadName,counter):
    datefields=[]
    today=datetime.date.today()
    datefields.append(today)
    print("%s[%d] : %s" % (threadName, counter, datefields[0]))

threadLock=threading.Lock()
threads=[]

thread1=myThread("Thread", 1)
thread2=myThread("Thread", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print("Exit programm!")
