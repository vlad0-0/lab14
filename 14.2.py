n = int(input("Введите длину последовательности,\nисследуемой на признаки арифметической прогрессии: "))
while n < 2:
     = int(input("Длина последовательности не может быть меньше двух. Введите заново: "))
a = []
b = True
for i in range(n):
    a.append(int(input()))
if n == 2:
    print(a[1]-a[0])
else:
    for i in range(n-2):
        if a[i]-a[i+1] != a[i+1]-a[i+2]:
            print(0)
            b = False
            break
    if b:
        print(a[1]-a[0])
