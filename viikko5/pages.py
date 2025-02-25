def create_string(pages):
    pages = sorted(set(pages))

    vastaus = []
    valimuisti = [pages[0]]

    for sivu_num in range(1,len(pages)):
        if pages[sivu_num] == valimuisti[-1] + 1:
            valimuisti.append(pages[sivu_num])

        else:
            if len(valimuisti) == 1:
                vastaus.append(str(valimuisti[0]))

            else:
                vastaus.append(f"{valimuisti[0]}-{valimuisti[-1]}")

            valimuisti = [pages[sivu_num]]

    if len(valimuisti) == 1:
        vastaus.append(str(valimuisti[0]))
    else:
        vastaus.append(f"{valimuisti[0]}-{valimuisti[-1]}")

    return ",".join(vastaus)

if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]
