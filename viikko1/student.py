def check_number(number):
    if len(number) != 9 or not number.startswith("0"):
        return False

    luvut = [int(l) for l in number]

    tarkistusluku = luvut[-1]

    kertoimet = [3, 7, 1, 3, 7, 1, 3, 7]

    lukujensumma = sum(l*k for l,k in zip(luvut[:-1], kertoimet))
    #print((lukujensumma + 9) // 10 * 10)

    if (lukujensumma + 9) // 10 * 10 -lukujensumma == tarkistusluku:
        return True
    else:
        return False





if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False