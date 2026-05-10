import threading
import time

counter = 0
lock = threading.Lock()

def inc_safe():
    global counter
    for _ in range(50):
        with lock:
            local_copy = counter
            time.sleep(0.00000001)
            counter = local_copy + 1


def main():
    threads = []
    for _ in range(20):
        t = threading.Thread(target=inc_safe)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(counter) # 50 * 20 = 1000 i tyle jest zwracane


if __name__ == '__main__':
    main()
