def solution(a):
    max_product = 0
    max_triplet = (0, 0, 0)
    n = len(a)
    triplet = [(p, q, r) for p in range(n) for q in range(p, n) for r in range(q, n) if
               0 <= p < q < r < len(a)]
    for p, q, r in triplet:
        product = a[p] * a[q] * a[r]
        if product > max_product:
            max_product = product
            max_triplet = (p, q, r)

    return "triplet " + str(max_triplet) + " is maximal for the product of " + str(max_product)


if __name__ == '__main__':
    a = [-3, 1, 2, -2, 5, 6]
    result = solution(a)
    print(result)
