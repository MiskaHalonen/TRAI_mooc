import random

def check_overlapping(reservations):
    reservations = sorted(reservations)

    # Käydään läpi varaukset ja tarkistetaan päällekkäisyys
    for i in range(1, len(reservations)):
        prev_a, prev_b = reservations[i - 1]
        curr_a, curr_b = reservations[i]

        # Jos edellisen varauksen loppupäivä on suurempi tai yhtä suuri kuin nykyisen varauksen alkupäivä,
        # varaukset menevät päällekkäin
        if prev_b >= curr_a:
            return True

    return False


if __name__ == "__main__":
    print(check_overlapping([])) # False
    print(check_overlapping([(1, 3)])) # False
    print(check_overlapping([(4, 7), (1, 2)])) # False
    print(check_overlapping([(4, 7), (1, 5)]))  # True
    print(check_overlapping([(1, 1), (2, 2)]))  # False
    print(check_overlapping([(1, 1), (1, 1)]))  # True
    print(check_overlapping([(2, 3), (5, 5), (3, 4)]))  # True
    print(check_overlapping([(2, 3), (5, 5), (1, 4)]))  # True
    print(check_overlapping([(2, 3), (5, 5), (1, 5)]))  # True

    reservations = [(day, day) for day in range(1, 10 ** 5 + 1)]
    random.shuffle(reservations)
    print(check_overlapping(reservations))  # False

    reservations.append((42, 1337))
    random.shuffle(reservations)
    print(check_overlapping(reservations))  # True