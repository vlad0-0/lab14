n = int(input())
while n<2:
    n = int(input())
b = ""
a = []
for i in range(n):
    a.append(input())
    if i%2 != 0 and (a[i] < b or b == ""):
        b = a[i]
print(b)
