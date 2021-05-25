def solution(a, b):
    pairs = {key[i]: values[i] for i in range(len(a))}
    print(pairs)
    fish = list(a)
    fish_start = a[b.index(1)]
    start = b.index(1) + 1
    print(fish_start)
    end = len(a)
    for i in range(start, end):
        print(f"iteration {i}")
        if b[i] == 0:

            if fish_start > a[i]:
                fish.remove(a[i])

            elif fish_start < a[i]:
                fish.remove(fish_start)
                fish_start = a[i]

        else:
            fish_start = a[i]

    print("fish left in 1st loop", fish)
    for j in range(len(fish) - 1):
        if fish[j] > fish[j + 1]:
            fish.remove(fish[j + 1])

        elif fish[j] < fish[j - 1]:
            fish.remove(fish[j])
            fish[j] = a[j - 1]
    print("fish left in the 2nd loop", fish)
    return (len(fish))


if __name__ == "__main__":
    key = [4, 3, 2, 1, 5]
    values = [0, 1, 0, 0, 0]
    a = [6, 3, 2, 1, 5]
    b = [1, 0, 0, 0, 0]
    c = [4, 3, 2, 1, 5]
    d = [1, 1, 0, 0, 0]
    e = [6, 3, 2, 1, 5]
    f = [1, 1, 0, 0, 0]
    result = solution(c,d )
    print(result)
