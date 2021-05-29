def solution(a):
    dict_dominator = {}
    dict_dominator = { key:a.count(key) for key in a }
    max_count = max(dict_dominator.values())
    if max_count > len(a) / 2:
        return [i for i in range(len(a)) if dict_dominator[a[i]] == max_count]

    else:
        return -1


if __name__ == "__main__":
    a = [3, 4, 3, 2, 3, -1, 3, 3]
    result = solution(a)
    print(result)
