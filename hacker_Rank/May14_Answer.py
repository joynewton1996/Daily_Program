from algorithm import Algo

obj = Algo()


def solution(a):
    n = len(a)
    pairs = [(p, q) for p in range(n) for q in range(p + 1, n - 1)]
    minvalue = sum(a[0:1])
    for p, q in pairs:
        Sum = sum(a[p:q + 1])
        avg = Sum / (q - p + 1)
        if avg < minvalue:
            minvalue = avg
            minvalue_list = p
    return (minvalue_list)


if __name__ == '__main__':
    a = [4, 2, 2, 5, 1, 5, 8]
    result = solution(a)
    print(result)
