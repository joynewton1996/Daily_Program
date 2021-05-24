def solution(a, b):
    pairs = {key[i]: values[i] for i in range(len(a))}
    print(pairs)
    fish = list(a)
    start = b.index(1)
    end = len(a)
    max_fish = a[start]

    for i in range(start, end):
        if fish[start] > a[i]:
            fish.pop(a[i])
        elif fish[start] < a[i]:
            fish.pop(fish[start])
            max_fish = a[i]
    print(fish)
    return (len(fish))


if __name__ == "__main__":
    key = [4, 3, 2, 1, 5]
    values = [0, 1, 0, 0, 0]
    result = solution(key, values)
    print(result)
