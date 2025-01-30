# törkeen vaikee mut hauska huomata kuinka hitaasti tällä tavalla numeroita oikeasti käydään
def count_numbers(a, b):
    counter = 0
    d = a
    while d <= b:

        if any(digit in str(d) for digit in "01346789"):
            d += 1
        else:
            counter += 1
            d += 1
            print(counter)

    return counter

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512