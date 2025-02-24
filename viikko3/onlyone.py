def find_number(numbers):
    luku = numbers[0]

    # tarkistetaan ensimmäinen luku
    if numbers[0] != numbers[1] and numbers[0] != numbers[2]:
        return numbers[0]

    # käydään loppu lista läpi ja skipataan ensimmäinen
    i = 1
    for i in range(len(numbers)):
        if numbers[i] != numbers[i-1] and numbers[i] != luku:
            luku = numbers[i]
            return luku
        else: i += 1

    return luku



if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2