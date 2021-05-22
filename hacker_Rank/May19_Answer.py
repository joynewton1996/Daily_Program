def solution(a):
    count = 0
    n = len(a)
    for j in range(n):
        list_j = [j for j in range((-a[j] + j), (a[j] + j + 1))]
        # print(f"list_j {j}", list_j)
        for k in range(j+1,n):
            list_k = [k for k in range((-a[k] + k), (a[k] + k + 1))]
            if set(list_j).intersection(list_k):
                print(f"disc {j} intersect disk {k}")

                count += 1


    return count

if __name__ == "__main__":
    a = [1, 5, 2, 1, 4, 0]
    result = solution(a)
    print(result)
