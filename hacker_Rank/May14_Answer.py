from algorithm import Algo

obj = Algo()


def solution(a):
    print(a)
    n = len(a)
    pairs = [[p, q] for p in range(n) for q in range(p + 1, n - 1)]
    print(pairs)
    minvalue = 0
    minvalue_list = []
    minvalue = sum(a[0:1]) / (1 - 1 + 1)
    for p, q in pairs:
        # print(a[p:q])
        print("iteration",p ,"vs ", q)
        Sum = sum(a[p:q+1])
        print("sum", Sum)
        avg = Sum/(q-p+1)
        print("avg" , avg)
        if avg < minvalue:
            minvalue = avg
            minvalue_list=[p,q]
    return (minvalue , "min" , minvalue_list)





    # a = float(sum(a[p:q])/q-p+1)
    # print(a)

        # print(pairs)
        # total = [item for item in pairs]
        # print(total)

        # for p in range(1):
        #     for q in range(1, n - 1):
        #         if 0 <= p < q < n:
        #             print("P", p, "vs", q, "q")
        #             total = [a[item] for item in range(p, q + 1)]
        #             avg = sum(total)/(q-p+1)
        #             print(avg)

        # print("item" , item)
        # sum = a[item] + sum
        # print("sum", sum)

        # avg = sum / (q - p + 1)
        # print("avg", avg)

        # master.append(avg)
        # print("Master", master)
        # sum = 0

        # master = obj.min_value(master)
        # return master

if __name__ == '__main__':
    a = [4, 2, 2, 5, 1, 5, 8]
    result = solution(a)
