def count_rounds(numbers):
    num_to_index = {num: idx for idx, num in enumerate(numbers)}
    rounds = 0
    n = len(numbers)

    for i in range(1, n + 1):
        # Jos nykyisen luvun indeksi on pienempi kuin edellisen luvun indeksi,
        # aloitamme uuden kierroksen
        if i == 1 or num_to_index[i] < num_to_index[i - 1]:
            rounds += 1

    return rounds


if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000