import threading
import time

counter = 0

def inc_unsafe():
    global counter
    for _ in range(50):
        local_copy = counter
        time.sleep(0.00000001)
        counter = local_copy + 1


def main():
    threads = []
    for _ in range(20):
        t = threading.Thread(target=inc_unsafe)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(counter) # tutaj najczęściej zwraca w okolicy 55, gdyż występuje race condition, pylint nie wykrywa go


if __name__ == '__main__':
    main()
