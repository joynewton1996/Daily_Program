def array_rotation(a, k):
    result = []
    print(a)
    step = 1
    for i in range(k):
        step = 1
        print("for_loop:" + str(i), a)
        while step < len(a):
            temp = a[0]
            a[0] = a[(0+step)]
            a[(0+step)] = temp
            print("while_loop:" + str(step) , a)
            step += 1

        # # while step < len(a)-2:
        #     # print(a)
        #     step_temp = a[0]
        #     a[0] = a[step + 2]
        #     a[step + 2] = step_temp
        #     step += 1
        #     print("loop" ,a)

    print("Result_list", a)




# a = [3,8,9,7,6]
a = [1,2,3,4,5]
k = 1


array_rotation(a, k)
