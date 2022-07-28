import threading
import time



def task1():
    counter=0
    print("{} is running at {}".format(threading.current_thread().name, counter))
    while counter<=60:
        time.sleep(1)
        counter += 1
        if counter % 5 == 0:
            print("{} is running at {}".format(threading.current_thread().name, counter))
            if counter==20:
                t2.start()
                time.sleep(18)



def task2():
    counter=0
    print("{} is running at {}".format(threading.current_thread().name, counter))
    while counter<=60:
        time.sleep(1)
        counter += 1
        if counter % 5 == 0:
            print("{} is running at {}".format(threading.current_thread().name, counter))

    # creating threads
def task3():
    counter=0
    print("{} is running at {}".format(threading.current_thread().name, counter))
    while counter<=60:
        time.sleep(1)
        counter += 1
        if counter % 5 == 0:
            print("{} is running at {}".format(threading.current_thread().name, counter))
            if counter==35:
                time.sleep(30)





t1 = threading.Thread(target=task1, name='Thread 1')
t2 = threading.Thread(target=task2, name='Thread 2')
t3 = threading.Thread(target=task3, name='Thread 3')


t1.start()
t3.start()





