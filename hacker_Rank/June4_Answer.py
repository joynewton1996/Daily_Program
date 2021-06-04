def solution(a, k_flag):
    n = len(a)
    a_dict = {p: a[p] for p in range(n) if 0 < p < n - 1 if a[p - 1] < a[p] > a[p + 1]}
    peak_max = sorted(a_dict.values())
    flag_point = peak_max[-k_flag:]
    try:

        if k_flag <= len(flag_point):
            flag = [key for flag in flag_point for key in a_dict if a_dict[key] == flag]
            return sorted(flag[-k_flag:])
    except IndexError:
        print("Index error")
    else:
        print(f"maximum flag required is {len(flag_point)} " )
    finally:
        print("Thanks for climbling the hill")


if __name__ == "__main__":
    a = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    k_flag = 3
    result = solution(a, k_flag)
    print(result)
