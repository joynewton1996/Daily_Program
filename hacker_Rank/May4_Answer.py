def array_rotation(a, k):
    result = []
    print(a)
    step = 0
    for i in range(k):
        print("ref", a)
        print(i)
        temp = a[0]
        a[0] = a[(0+1)]
        a[(0+1)] = temp
        print("fist_loop:", a)
        step = 0

        while step < len(a)-2:
            # print(a)
            step_temp = a[0]
            a[0] = a[step + 2]
            a[step + 2] = step_temp
            step += 1
            print("loop" ,a)

    print("final", a)




a = [3,8,9,7,6]
k = 3


array_rotation(a, k)
