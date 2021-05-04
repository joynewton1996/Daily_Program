a = 20
b = 4
multiply = 1

while (b * multiply) < a:
    multiply += 1
print(multiply)

a = [40, 20, 10, 80, 60]
temp = 0
 for i in a:
     if a[i] > a[i+1]:
         temp = a[i+1]
         a[i+1] = a[i]
         a[i] = temp
