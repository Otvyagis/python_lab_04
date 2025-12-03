# Задание 2

from random import randint

def tuple_generator(n, a, b):
    if n <= 0:
        raise ValueError("Размер кортежа должен быть > 0")

    while True:
        yield tuple(randint(a, b) for _ in range(n))


def generate_matrix():
    gen = tuple_generator(20, -5, 5)
    return [next(gen) for _ in range(20)]


if __name__ == "__main__":
    matrix = generate_matrix()
    for row in matrix:
        print(row)
