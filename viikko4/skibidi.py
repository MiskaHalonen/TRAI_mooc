import random
import time


def find_mode(numbers):
    count = {}
    mode = numbers[0]
    start_time = time.time()

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x
    end_time = time.time()

    result_time = end_time - start_time

    return print(result_time, "sekuntia")


if __name__ == "__main__":
    n = 10 ** 7
    lista = random.choices(range(1, 10 ** 7), k=n)

    find_mode(lista)