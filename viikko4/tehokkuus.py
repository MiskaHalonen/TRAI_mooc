import random
import time


# molemmat O(n) joten ajat periaatteessa identtiset

def count_rounds_sanakirja(numbers):
    starttime = time.perf_counter()

    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    stoptime = time.perf_counter()
    totaltime = stoptime-starttime
    return totaltime



def count_rounds_lista(numbers):
    starttime = time.perf_counter()

    num_to_index = {num: idx for idx, num in enumerate(numbers)}
    rounds = 0
    n = len(numbers)


    for i in range(1, n + 1):
        # Jos nykyisen luvun indeksi on pienempi kuin edellisen luvun indeksi,
        # aloitamme uuden kierroksen
        if i == 1 or num_to_index[i] < num_to_index[i - 1]:
            rounds += 1



    stoptime = time.perf_counter()
    totaltime = stoptime - starttime
    return totaltime

if __name__ == "__main__":
    testi_lista = list(range(1, 10 ** 7 + 1))
    random.shuffle(testi_lista)

    print("listatoteutuksen aika: " + str(count_rounds_lista(testi_lista)) + "s")
    print("sanakirjatoteutuksen aika: " + str(count_rounds_sanakirja(testi_lista)) + "s")