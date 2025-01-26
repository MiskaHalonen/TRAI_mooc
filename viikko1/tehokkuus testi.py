import time
import random


# toteutus 1
def count_even1(numbers):
    starttime = time.perf_counter()
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    endtime = time.perf_counter()
    aika = endtime - starttime
    print(f"aika {aika:.6f} sekuntia")
    return result

# toteutus 2
def count_even2(numbers):
    starttime = time.perf_counter()

    result = sum(x % 2 == 0 for x in numbers)

    endtime = time.perf_counter()
    aika = endtime - starttime
    print(f"aika {aika:.6f} sekuntia")
    return result


if __name__ == "__main__":
    random_list = [random.randint(0, 100) for _ in range(10**7)]

    print("toteutus 1")

    for i in range(10):
        count_even1(random_list)

    print("toteutus 2")

    for i in range(10):
        count_even2(random_list)

