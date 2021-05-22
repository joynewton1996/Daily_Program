from itertools import product


def solution(a):
    n = len(a)
    triplet = [(p, q, r) for p, q, r in (product(range(n), repeat=3))
               if 0 <= p < q < r < n and a[p] + a[q] > a[r] and a[q] + a[r] > a[p] and a[r] + a[p] > a[q]]
    if triplet > []:
        return 1
    else:
        return 0

    print(triplet)


if __name__ == '__main__':
    a = [10, 2, 5, 1, 8, 20]
    b = [10, 50, 5, 1]
    result = solution(a)
    print(result)
