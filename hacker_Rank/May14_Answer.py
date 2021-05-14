from algorithm import Algo

obj = Algo()


def solution(a):
    print(a)
    n = len(a)
    sum = 0
    master = []
    for p in range(n):
        for q in range(1, n - 1):
            if 0 <= p < q < n:
                print("P", p, "vs", q, "q")
                for item in range(p, q + 1):
                    # print("item" , item)
                    sum = a[item] + sum
                print("sum", sum)

                avg = sum / (q - p + 1)
                print("avg", avg)

                master.append(avg)
                print("Master", master)
                sum = 0

    master = obj.min_value(master)
    return master


if __name__ == '__main__':
    a = [4, 2, 2, 5, 1, 5, 8]
    result = solution(a)
    print(result)
