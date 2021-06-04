def solution(n):
    try:
        a = len([i for i in range(1, n + 1) if n % i == 0])
    except TypeError:
        return "Please use integer"
    else:
        return a
    finally:
        print("Here is your result")


if __name__ == "__main__":
    n = 24
    result = solution(n)
    print(result)
