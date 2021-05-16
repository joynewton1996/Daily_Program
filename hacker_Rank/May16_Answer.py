def solution(a):
    east = [car for car in range(len(a)) if a[car] == 0]
    print(east)
    west = [car for car in range(len(a)) if a[car] == 1]
    print(west)
    total = [(e, w) for e in east for w in west]
    print(total)


if __name__ == "__main__":
    a = [0, 1, 0, 1, 1]
    result = solution(a)
