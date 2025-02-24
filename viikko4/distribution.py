def create_distribution(string):
    osajoukot = set()
    n = len(string)

    for i in range(n):
        current_substring = ""
        for j in range(i, min(i + 20, n)):  # Koska merkkijonon pituus on enintään 20
            current_substring += string[j]
            osajoukot.add((current_substring, len(current_substring)))  # hylkää automaattisesti duplikaatit joten
            # voidaan huoletta lisätä kaikki löydetyt


    distribution = {} # sanakirja johon tulokset tallennetaan
    for osajoukko, pituus in osajoukot:
        if pituus in distribution:
            distribution[pituus] += 1
        else:
            distribution[pituus] = 1

    #jörjestetään lista vielä osajoukkojen pituuden mukaan
    sorted_distribution = dict(sorted(distribution.items()))

    return sorted_distribution

if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}

    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}

    print(create_distribution("abcd"))
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}