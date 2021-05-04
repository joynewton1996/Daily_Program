list = []
for _ in range(int(input())):
    name = input()
    marks = float(input())
    list.append([name, marks])

l1 = []
print(list)

for i in range(0, len(list)):
    for j in range(len(list) - i - 1):
        if (list[j][1] > list[j + 1][1]):
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
low_score = list[1][1]
for name, marks in list:
    if low_score == marks:
        l1.append(name)

for i in range(len(l1) - 1):
    if l1[i] > l1[i + 1]:
        temp = l1[i]
        l1[i] = l1[i + 1]
        l1[i + 1] = temp

print(list)
print(l1)
