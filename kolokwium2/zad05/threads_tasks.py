import threading
import queue
import time

wyniki = []
lista_blokada = threading.Lock()
kolejka = queue.Queue()

SENTINEL = None


def konsument(id_watku):
    """Funkcja wykonywana przez każdy z wątków-konsumentów."""
    print(f"[Wątek-{id_watku}] Uruchomiony.")

    while True:
        liczba = kolejka.get()

        if liczba is SENTINEL:
            kolejka.task_done()
            print(f"[Wątek-{id_watku}] Odebrano SENTINEL. Kończę pracę.")
            break

        kwadrat = liczba ** 2

        time.sleep(0.05)

        with lista_blokada:
            wyniki.append((liczba, kwadrat))

        kolejka.task_done()


def main():
    for i in range(1, 21):
        kolejka.put(i)

    liczba_watkow = 4
    for _ in range(liczba_watkow):
        kolejka.put(SENTINEL)

    watki = []
    for i in range(liczba_watkow):
        watek = threading.Thread(target=konsument, args=(i + 1,))
        watki.append(watek)
        watek.start()

    for watek in watki:
        watek.join()

    print("\n--- Wszystkie wątki zakończyły pracę ---")

    wyniki.sort()
    print("Wyniki (liczba -> kwadrat):")
    for liczba, kwadrat in wyniki:
        print(f"{liczba} -> {kwadrat}")


if __name__ == "__main__":
    main()