def solution(a):
    n = len(a)
    try:
        slice_sum = max([sum(a[p:q]) for p in range(len(a)) for q in range(len(a)) if 0 <= p <= q <= n])

    except IndexError:
        return ("Index_Error caught")
    else:

        return f"slice_sum of the list is : {slice_sum}"
    finally:
        print ("Your work completed")



if __name__ == "__main__":
    a = [3, 2, -6, 4, 0]
    result = solution(a)
    print(result)
