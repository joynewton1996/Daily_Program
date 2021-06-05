def solution(a):
    n = len(a)
    try:
        peak_max = set(sorted([a[p] for p in range(n) if 0 < p < n - 1 if a[p - 1] < a[p] > a[p + 1]]))
    except IndexError:
        return ("Index error")
    else:
        return (f"maximum flag required is {len(peak_max)} ")
    finally:
        print("Thanks for climbling the hill")


if __name__ == "__main__":
    a = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    result = solution(a)
    print(result)
