def count_splits(sequence):
    # Lasketaan nollien ja ykkösten kokonaismäärät
    total_zeros = sequence.count('0')
    total_ones = sequence.count('1')

    # Jos nollien ja ykkösten määrät eivät ole samat, ei ole mahdollisia jakoja
    if total_zeros != total_ones:
        return 0

    # Jos nollien tai ykkösten määrä on pariton, ei ole mahdollisia jakoja
    if total_zeros % 2 != 0 and total_ones % 2 == 0 or total_ones % 2 != 0 and total_zeros % 2 == 0:
        return 0

    # Alustetaan muuttujat
    zero_count = 0
    one_count = 0
    split_count = 0

    # Käydään merkkijono läpi (viimeistä merkkiä ei tarkisteta, koska jako ei ole mahdollinen siinä kohdassa)
    for i in range(len(sequence) - 1):
        if sequence[i] == '0':
            zero_count += 1
        else:
            one_count += 1

       
        if zero_count ==  one_count and (total_ones-one_count) == (total_zeros-zero_count):
            split_count += 1

    return split_count


if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999