def solution(string):
    bracket = {"{": "}", "[": "]", "(": ")"}
    element = []
    count = len(string)/2
    if len(string) % 2 != 0:
        print("odd")
        return 0

    for char in string:
        if char in bracket.keys():
            element.append(char)
        elif char in bracket.values():
            if char == bracket[element.pop()]:
                count -= 1
            else:
                return 0

    if count == 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    string = "{[()()]}"
    result = solution(string)
    print(result)
