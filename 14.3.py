n = int(input())
while n<2:
    n = int(input())
b = 0
a = []
c = True
for i in range(n):
    a.append(input())
    if i%2 != 0 and (a[i] < b or c):
        b = a[i]
        c = False
print(b)
