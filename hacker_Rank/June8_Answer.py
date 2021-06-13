def solutuion(a):
    result = []
    for i in range(len(a)):
        stack = []
        stack = [a[j] for j in range(len(a)) if a[i] % a[j] != 0]
        result.append(len(stack))
    return result

if __name__=="__main__":
    a = [3,1,2,3,6]
    result = solutuion(a)
    print(result)