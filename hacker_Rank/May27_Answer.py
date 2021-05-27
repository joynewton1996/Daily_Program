def solution(a):
    print(a)
    sequence = []
    dominator = 0
    for i in range(0, len(a)):
        print(f"iteration {i}")
        b = a.count(a[i])
        print("b", b)
        c = a[0:i]
        d = a[i:len(a)]
        count_c = c.count(a[i])
        count_d = d.count(a[i])

        print("1st sequence", c)
        print("2nd sequence", d)

        print("count_c", count_c)
        print("count_d", count_d)
        if count_c > len(c) / 2 and count_d > len(d) / 2:
            print("hello")
            sequence = sequence.append(i)
    print(sequence)


if __name__ == "__main__":
    a = [4, 3, 4, 4, 4, 2]
    result = solution(a)
