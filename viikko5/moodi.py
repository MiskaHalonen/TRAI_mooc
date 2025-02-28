import random
import time


def find_mode(numbers):
    start_time = time.time()

    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    end_time = time.time()

    result_time = end_time - start_time

    return print(result_time, "sekuntia")

def find_moodi(numbers):
    start_time = time.time()

    numbers = sorted(numbers)
    max_count = 1
    current_count = 1
    moodi = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                moodi = numbers[i - 1]
            current_count = 1

    if current_count > max_count:
        moodi = numbers[-1]

    end_time = time.time()

    result_time = end_time - start_time

    return print(result_time, "sekuntia")

if __name__ == "__main__":
    randomlist = list()
    for i in range(10**7):
        n = random.randint(1,1000)
        randomlist.append(n)

    print(find_mode(randomlist))
    print(find_moodi(randomlist))