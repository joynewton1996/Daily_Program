def array_rotation(a, k):
    print(a)
    for i in range(k):
        step = 1
        while step < len(a):
            temp = a[0]
            a[0] = a[step]
            a[step] = temp
            step += 1
    print("Result", a)


# a = [3,8,9,7,6]
a = [1, 2, 3, 4, 5]
k = 2

array_rotation(a, k)
