def solution(l1, l2):
    a = ""
    b = ""
    l1 = [str(i) for i in l1]
    l2 = [str(i) for i in l2]
    a = str(int(a.join(l1)) + int(b.join(l2)))
    a = [int(i) for i in a]
    a.reverse()
    return a




if __name__ == "__main__":
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    l3 = [2,4,3]
    l4 = [5,6,4]
    result = solution(l1, l2)
    print(result)
