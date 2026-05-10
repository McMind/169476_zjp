import threading

def inc(counter_wrapper, lock):
    for _ in range(10000):
        with lock:
            counter_wrapper[0] += 1

def main():
    counter_wrapper = [0]
    lock = threading.Lock()
    threads = []
    for _ in range(5):
        t = threading.Thread(target=inc, args=(counter_wrapper, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(counter_wrapper[0])

if __name__ == '__main__':
    main()
