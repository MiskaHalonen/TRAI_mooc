def count_splits(numbers):
    from collections import defaultdict

    # Lasketaan jokaisen alkion esiintymiskerrat ja jos jokin alkio esiintyy vain kerran, halkaisuja ei ole
    total_counts = defaultdict(int)
    for num in numbers:
        total_counts[num] += 1

    if any(count == 1 for count in total_counts.values()):
        return 0


    # Alustetaan sanakirjat
    left_counts = defaultdict(int)
    right_counts = total_counts.copy()
    split_count = 0

    for i in range(len(numbers) - 1):
        num = numbers[i]
        left_counts[num] += 1
        right_counts[num] -= 1

        if right_counts[num] == 0:
            del right_counts[num]


        if len(left_counts) == len(total_counts) and len(right_counts) == len(total_counts):
            split_count += 1

    return split_count



if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1