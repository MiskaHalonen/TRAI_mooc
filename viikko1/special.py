def check_year(year):
    # jaetaan luku kahteen osaan
    part1 = year // 100
    part2 = year % 100

    if (part1 + part2)**2==year:
        return True
    else:
        return False

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False