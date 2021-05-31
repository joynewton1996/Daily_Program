def solution(a):
    print(a)
    position = 0
    for i in range(1, len(a)):
        c = a[:i]
        c_len = len(c) / 2
        d = a[i:]
        d_len = len(d) / 2
        count_c = [i for i in c if c.count(i) > c_len and i == max(c)]
        count_d = [j for j in d if d.count(j) > d_len and j == max(d)]
        if set(count_c) == set(count_d):
            position += 1

    if position:
        return position
    else:
        return -1


if __name__ == "__main__":
    a = [4, 3, 4, 4, 4, 2]
    result = solution(a)
    print(result)
