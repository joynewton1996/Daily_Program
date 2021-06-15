def solutuion(string):
    print(string)
    n = len(string)
    if n > 1:
        s1 = [string[i:j] for i in range(0, n) for j in range(i + 1, n + 1)]
        string = [i for i in s1 if i == i[::-1]]
        print(string)
    elif n == 1:
        print(string)


if __name__ == "__main__":
    string = ["babad", "cbbd", "a", "ac"]
    for i in string:
        result = solutuion(i)
