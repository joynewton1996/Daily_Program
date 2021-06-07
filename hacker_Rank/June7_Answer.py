from itertools import islice
from algorithm import Algo

obj = Algo()


def solutuin(a):
    n = len(a)
    peak_max = obj.peak_flag(a)
    print(peak_max)
    d = []
    for i in range(1, n):
        print("iteration for i", i)
        div = n // i
        if div > 2:
            print("div", div)
            end = div
            start = 0

            for j in range(1, i + 1):
                print("iteration for j", j)
                b = (a[start:end])
                start = end
                end = end + div
                peak_b = obj.peak_flag(b)
                if peak_max.intersection(peak_b):
                    d.append(i)
                else:
                    break
    print(len((set(d))))
    print(d)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    result = solutuin(a)
