import time as t
from functools import wraps

def repeat(ile_razy: int):
    def time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = t.perf_counter()
            result = None
            for _ in range(ile_razy):
                result = func(*args, **kwargs)
            end_time = t.perf_counter()

            duration = end_time - start_time
            print(f'{func.__name__} run {ile_razy} times and took {duration:.8f} seconds')
            return result
        return wrapper
    return time


@repeat(1000)
def alg1(a: int, n: int) -> int:
    def _alg1_func(a: int, n: int) -> int:
        if n == 0:
            return 1
        if n % 2 == 0:
            polowa = _alg1_func(a, n // 2)
            return pow(polowa, 2)
        return a * _alg1_func(a, n - 1)

    return _alg1_func(a, n)


@repeat(1000)
def alg2(a: int, n: int) -> int:
    wynik, i = 1, 1
    while i <= n:
        wynik *= a
        i += 1
    return wynik


@repeat(1000)
def alg3(a: int, n: int) -> int:
    def _alg3_func(a: int, n: int) -> int:
        if n == 0:
            return 1
        return a * _alg3_func(a, n - 1)

    return _alg3_func(a, n)


if __name__ == '__main__':
    print(alg1(2, 996))
    print(alg2(2, 996))
    print(alg3(2, 996))
    # help(alg1(2,996))
