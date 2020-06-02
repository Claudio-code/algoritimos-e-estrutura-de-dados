from threading import Thread
import time

def my_thread(i):
    print("Iniciando a thread %d" % i)
    time.sleep(5)

    print("Thread finalizada %d" % i)


for i in range(10):
    t = Thread(target=my_thread, args=(i,))
    t.start()