from itertools import product


def solution(a):
    max_product = 0
    max_triplet = (0, 0, 0)
    n = len(a)
    triplet = tuple(product(range(n), repeat=3))
    product_sum = max([(a[p]*a[q]*a[r]) for p,q,r in triplet if 0 <= p < q < r < len(a)])
    return (product_sum)


if __name__ == '__main__':
    a = [-3, 1, 2, -2, 5, 6]
    result = solution(a)
    print(result)
