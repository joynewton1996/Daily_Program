def solution(a):
    print(a)
    sequence = []
    dict_c = {}
    dict_d = {}
    position = 0
    for i in range(0,len(a)):
        c = a[:i]
        d = a[i:]

        if len(c) >= 1 and len(d) >= 1:

            count_c = {l: c.count(l) for l in c}
            count_d = {k: d.count(k) for k in d}
            max_count_c = max(count_c.values())
            max_count_d = max(count_d.values())
            if max_count_d == max_count_c and max_count_d > len(count_d) / 2 and max_count_c > len(count_c) / 2:
                position = i


    if position:
        return position
    else:
        return -1


if __name__ == "__main__":
    a = [4, 3, 4, 4, 4, 2]
    result = solution(a)
    print(result)
