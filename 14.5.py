n = int(input())
while n < 2:
    n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
def pair(n):
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                yield i, j
for i, j in pair(n):
    if a[i] == a[j]:
        print(i, j)
        break
else:
    print(0)
