def hash_value(string):
    A = 23
    M = 2 ** 32
    n = len(string)
    hash_val = 0

    for i, char in enumerate(string):
        # Muunnetaan merkki vastaavaksi numeroksi (a=0, b=1, ..., z=25)
        c = ord(char) - ord('a')
        # Lasketaan hajautusarvo
        hash_val = (hash_val * A + c) % M

    return hash_val

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440