def solution(n):

    perimeter = min([(2 * ((n // i) + i)) for i in range(1, n) if n % i == 0])
    return perimeter

if __name__ == "__main__":
    a = 30
    result = solution(a)
    print(result)
