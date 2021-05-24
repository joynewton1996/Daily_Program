def solution(a):
    count = 0
    n = len(a)
    for j in range(n):
        disc_j = set(range((-a[j] + j), (a[j] + j + 1)))
        for k in range(j + 1, n):
            disk_k = set(range((-a[k] + k), (a[k] + k + 1)))
            if disc_j.intersection(disk_k):
                count += 1

    return count


if __name__ == "__main__":
    a = [1, 5, 2, 1, 4, 0]
    result = solution(a)
    print(result)
