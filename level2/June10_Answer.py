def solution(dividend,divisor):
    count = 0
    if dividend > 0 :
        while dividend > abs(divisor):
            dividend = (dividend)-abs(divisor)
            count += 1
        if divisor > 0:
            return (count)
        else:
            return (count * (-1))

    else:
        return (dividend)

if __name__=="__main__":
    dividend = 7
    divisor = 2
    result = solution(dividend,divisor)
    print(result)

