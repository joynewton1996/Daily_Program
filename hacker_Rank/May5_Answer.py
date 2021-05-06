def earliest_time(a, x):
    print(a)
    b = []
    for i in range(len(a)):
        if 1 <= a[i] <= x:
            for j in range(len(a)):
                if a[i] == a[j] and a[i] not in b:
                    b.append(a[i])
                    seconds = j

    print("fianl", b)
    return "seconds " + str(seconds) + "  " + "Number of steps:" + str(b)


if __name__ == '__main__':
    # Call your function here
    a = [1, 3, 1, 4, 2, 3, 5, 4]
    x = 2
    time = earliest_time(a, x)
    print(time)
