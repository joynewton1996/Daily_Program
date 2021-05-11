def long_gap_character_in_string(s):
    a = s
    count = 0
    long_gap = 0
    letter = ""
    print(a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                count += (j - i)
                count = count - long_gap
            elif long_gap <= count:
                long_gap = count
                letter = letter + a[j]
                count = 0
    print("'", letter, "'", "long gap", long_gap)


if __name__ == '__main__':
    a = "abcdefgcabxyzca"

    long_gap_character_in_string(a)
