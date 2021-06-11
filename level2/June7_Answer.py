# Method 1
def solution1(string):
    sub = set(string)
    return len(sub)

# Method 2
def solution2(string):
    j = ""
    for i in string:
        if i not in j:
            j = j+i
    return len(j)




if __name__=="__main__":
    string =  "abcabcbb"
    result1 = solution1(string)
    result2 = solution2(string)
    print(result1)
    print(result2)