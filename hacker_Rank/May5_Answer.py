def earliest_time(a, x):
    print(a)
    b = []

    for i in range(len(a)):
        if a[i] == x or a[i] <= x:
            for j in range(len(a)):
                if a[i] == a[j] and a[i] not in b:
                    b.append(a[i])
                    seconds = j
    if x in b:
        return "seconds " + str(seconds) + "  " + "Number of steps:" + str(b)
    else:
        return -1


if __name__ == '__main__':
    # Call your function here
    a = [1, 3, 1, 4, 2, 3, 5, 4]
    x = 3
    time = earliest_time(a, x)
    print(time)
