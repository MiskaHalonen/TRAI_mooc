def count_sublists(numbers):
    # aika vaativuus on O(n) koska listan numeroita käydään vain kerran läpi

    count = 0 # halututujen osalistojen määärä
    current_length = 0 # kerää peräkkäisten osalistojen määrän väli säilöön


    for number in numbers:
        if number % 2 == 0:
            current_length += 1
            count += current_length
        else:
            current_length = 0

    return count

if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000