def count_substrings(string):
    # aika vaativuus O(n^2) mutta stringin pituus rajoitettu joten toimii tehokkaasti vaadittuun tehtävään
    osajoukot = set()
    n = len(string)

    for i in range(n):
        current_substring = ""
        for j in range(i, min(i + 20, n)):  # Koska merkkijonon pituus on enintään 20
            current_substring += string[j]
            osajoukot.add(current_substring) # hylkää automaattisesti duplikaatit joten
                                             # voidaan huoletta lisätä kaikki löydetyt

    return len(osajoukot)


if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110
