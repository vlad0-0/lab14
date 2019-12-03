n = int(input())
while n < 3:
    n = int(input())
for i in range(n):
    a.append(float(input()))
for i in range(n-2, 0, -1):
    if a[i]<a[i+1]>a[i+2]:
        print(a[i+1])
        break

