def solution(a):
    east = [car for car in range(len(a)) if a[car] == 0]
    west = [car for car in range(len(a)) if a[car] == 1]
    total = [(e, w) for e in east for w in west if w > e]
    return len(total)


if __name__ == "__main__":
    a = [0, 1, 0, 1, 1]
    result = solution(a)
    print(result)
