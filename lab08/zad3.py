import time
import random
import threading

NUM_SOURCES = 10


def fetch_data(source_id):
    wait_time = random.uniform(0.5, 2.0)
    time.sleep(wait_time)
    print(f"\tPobrano dane ze źródła {source_id} (czas: {wait_time:.2f}s)")


def run_sequential():
    print("Wersja Sekwencyjna")
    start_time = time.perf_counter()

    for i in range(NUM_SOURCES):
        fetch_data(i)

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Koniec wersji sekwencyjnej. Łączny czas: {total_time:.2f}s\n")
    return total_time


def run_threaded():
    print("Wersja Wielowątkowa")
    start_time = time.perf_counter()
    threads = []

    for i in range(NUM_SOURCES):
        thread = threading.Thread(target=fetch_data, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Koniec wersji wielowątkowej. Łączny czas: {total_time:.2f}s\n")
    return total_time


if __name__ == "__main__":
    seq_time = run_sequential()
    thr_time = run_threaded()

    print("--- PORÓWNANIE ---")
    print(f"Sekwencyjnie: {seq_time:.2f}s")
    print(f"Wielowątkowo: {thr_time:.2f}s")
    print(f"Zysk czasu: {seq_time - thr_time:.2f}s") # wersja wielowątkowa zyskuje średnio 10 sekund
