def array_rotation(a, k):
    print(a)
    for i in range(k):
        step = 1
        while step < len(a):
            temp = a[0]
            a[0] = a[step]
            a[step] = temp
            step += 1
    return a


a = [1, 2, 3, 4, 5]
k = 2

result = array_rotation(a, k)

print(result)
