def earliest_time(a, x):
    print(a)
    b = []
    ref = []
    count = 0
    ref = [i for i in range(1, x + 1)]

    for i in range(len(a)):
        if a[i] == x or a[i] <= x:
            for j in range(len(a)):
                if a[i] == a[j] and a[i] not in b:
                    b.append(a[i])
                    seconds = j

    for k in ref:
        if k not in a:
            count += 1

    if count == 0:
        return "seconds " + str(seconds) + "  " + "Number of steps:" + str(b)
    else:
        return -1


if __name__ == '__main__':
    # Call your function here
    a = [1, 2, 3, 2, 4, 5, 3]
    x = 4
    time = earliest_time(a, x)
    print(time)
