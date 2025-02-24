def count_parts(songs):
    n = len(songs)
    vasen = 0
    maara = 0
    edellinen_paikka = {}

    for oikea in range(n):
        if songs[oikea] in edellinen_paikka:
            vasen = max(vasen,edellinen_paikka[songs[oikea]] + 1)
        edellinen_paikka[songs[oikea]] = oikea
        maara += oikea-vasen + 1

    return maara

if __name__ == "__main__":
    print(count_parts([1, 1, 1, 1])) # 4
    print(count_parts([1, 2, 3, 4])) # 10
    print(count_parts([1, 2, 1, 2])) # 7
    print(count_parts([1, 2, 1, 3])) # 8
    print(count_parts([1, 1, 2, 1])) # 6

    songs = [1, 2] * 10**5
    print(count_parts(songs)) # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs)) # 15000050000