from functools import partial

def power(x, n):
    return x ** n

square = partial(power, n=2)

cube = partial(power, n=3)

print(square(5)) # 25

print(cube(3)) # 27