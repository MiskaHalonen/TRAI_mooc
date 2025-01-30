def find_rounds(numbers):
    n = len(numbers)
    keratyt = set()
    results = []
    kierros = []
    seuraaava_numero = 1

    while len(keratyt) < n:
        for num in numbers:
            if num == seuraaava_numero and num not in keratyt:
                kierros.append(num)
                keratyt.add(num)
                seuraaava_numero += 1
        if kierros:
            results.append(kierros)
            kierros = []

    return results


if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]

    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]