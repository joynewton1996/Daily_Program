def sort(a):
    for i in range(len(a) - 1):
        for j in range(i, len(a) - 1):
            if a[i] > a[j + 1]:
                temp = a[i]
                a[i] = a[j + 1]
                a[j + 1] = temp

    return a


def solution(a):
    b = sort(a)
    step = 0
    while step < len(b) - 2:
        if b[step] != b[step + 1]:
            return b[step]
        step += 2


if __name__ == '__main__':
    # Call the fumction
    a = [9, 3, 9, 3, 9, 7, 9]
    print(solution(a))
    # print(sort(a))
