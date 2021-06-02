def solution(a):
    a = list(a)
    n = len(a)
    try:
        stock_price = max(
            [[a[sell] - a[buy]] for buy in range(n) for sell in range(n) if 0 <= buy < sell if (a[sell] - a[buy]) > 0])



    except ValueError:
        yield 0
    else:
        yield stock_price

    finally:
        print("Thanks for trading")


if __name__ == "__main__":
    a = [23171, 21011, 21123, 21366, 21013, 21367]
    b = (23, 21, 18)
    result = solution(a)
    print(next(result))
