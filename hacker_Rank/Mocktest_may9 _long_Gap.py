def long_gap_character_in_string(s):
    a = s
    count = 0
    long_gap = 0
    letter = ""
    print(a)
    for i in range(len(a)):
        # print("iteration i ", i)
        for j in range(i + 1, len(a)):
            # print("iteration J ", j)
            # print(a[i], "==", a[j])
            if a[i] == a[j]:
                # print("if", a[i], "==", a[j])
                count += (j - i)
                # print("if count", count)
                count = count - long_gap
            elif long_gap <= count:

                # print("long_gap", long_gap, "<", count)
                long_gap = count
                # print("long_gap", long_gap)
                letter = a[i]
                count = 0
    print(letter, "long gap", long_gap)


if __name__ == '__main__':
    a = "abcdefgcabxyzca"

    long_gap_character_in_string(a)
