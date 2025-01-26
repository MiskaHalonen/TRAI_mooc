def find_segments(data):
    segments = []

    if not data:
        return segments

    char = data[0]
    count = 0

    for i in data:
        if i == char:
            count += 1
        else:
            segments.append((count,char))
            char = i
            count = 1

    segments.append((count,char))
    return segments

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]