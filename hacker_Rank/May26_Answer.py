def solution(a):
    dominator = 0
    dominator_number = 0
    for j in a:
        count = a.count(j)
        if count > len(a) / 2 and count > dominator:
            dominator = count

    if dominator > len(a) / 2:
        return [i for i in range(len(a)) if a[i] == dominator_number]
    else:
        return -1


if __name__ == "__main__":
    a = [3, 4, 3, 2, 3, -1, 3, 3]
    result = solution(a)
    print(result)
