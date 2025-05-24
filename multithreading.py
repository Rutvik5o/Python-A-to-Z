import threading,time

def worker(num):

    print(f"Thread {num} : Starting\n-----------")
    time.sleep(2)
    print(f"Thread {num} : Finishing\n")


threads = []

for i in range(3):

    thread = threading.Thread(target=worker,args=(i,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join() # wait for all threads for finish

print("All Threads Completed")
