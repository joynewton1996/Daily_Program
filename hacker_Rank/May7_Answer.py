from algorithm import Algo
obj = Algo()

def solution(N, a):
    # a = [3, 4, 4, 6, 1, 4, 4]'

    counter = [0 for _ in range(1, N + 1)]
    x = []
    for i in range(0, len(a)):
        # print("a["+str(i)+"]" + " = " + str(a[i]))
        if 1 <= a[i] <= N:
            value = a[i]
            counter[value - 1] += 1
        elif a[i] > N:
            counter = [obj.max_value(counter) for j in range(1, N + 1)]
    return counter



if __name__ == '__main__':
    a = [3, 4, 4, 6, 1, 4, 4]
    N = 5
    value_of_the_counter = solution(N, a)
    print(value_of_the_counter)
    # x = [1,4,3,2]
    # print("max_value" , max_value(x))
