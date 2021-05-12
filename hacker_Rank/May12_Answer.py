def solution(a, b, k):
    if a<=b:
        a = list(range(a, b + 1))
        count = [number for number in a if number % k == 0]
        return len(count)
    else:
        return "error"


if __name__ == '__main__':
    a = 6
    b = 11
    k = 2
    result = solution(a, b, k)
    print(result)
