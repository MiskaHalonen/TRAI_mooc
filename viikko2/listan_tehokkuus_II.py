import random
import time


def alg(n):
    lista = []
    starttime = time.perf_counter()

    for i in range(n):
        lista.append(i)

    stoptime = time.perf_counter()
    execution_time = stoptime - starttime
    print(f"lisäys aika {execution_time:.6f} sekuntia")

    starttime = time.perf_counter()


    while lista != []:
        lista.pop(0)


    stoptime = time.perf_counter()
    execution_time = stoptime - starttime
    print(f"poisto aika {execution_time:.6f} sekuntia \n")




if __name__ == "__main__":
    luku = random.randint(100000, 999999)
    print(f"n= {luku}")

    for i in range(10):
        alg(luku)