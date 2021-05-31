def solution(a):
    n = len(a)
    print(a)
    max_slice = 0
    triplet = [(x, y, z) for x in range(n) for y in range(n) for z in range(n) if 0 <= x < y < z < n]
    for x, y, z in triplet:
        double_slice = sum(a[x + 1:y] + (a[y + 1:z]))
        if double_slice > max_slice:
            max_slice = double_slice

    return max_slice


if __name__ == "__main__":
    a = [3, 2, 6, -1, 4, 5, -1, 2]
    result = solution(a)
