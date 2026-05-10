import threading
import queue

def process_queue(input_queue, results):
    while True:
        try:
            number = input_queue.get(timeout=0.1)
            results.append(pow(number, 2))
            input_queue.task_done()
        except queue.Empty:
            break

def main():
    numbers_to_process = range(1, 21)
    input_queue = queue.Queue()
    results = []
    threads = []
    num_threads = 4

    for num in numbers_to_process:
        input_queue.put(num)

    for _ in range(num_threads):
        thread = threading.Thread(target=process_queue, args=(input_queue, results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Wyniki: {sorted(results)}")

if __name__ == "__main__":
    main()
