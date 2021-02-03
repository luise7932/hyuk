import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working:{i}\n")

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)          # 스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start()                                       # 스레드를 실행한다.

for t in threads:
    t.join()

print("End")