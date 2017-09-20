L = [2,3,5,]
num = 2+3+5
for x in range(7,2000000,2):
    a = 1
    for i in L:
        if i**2 > x:#代替开根
            break
        if x % i == 0:
            a = 0
            break
    if a:#必须要加
        num += x
        L.append(x)

print(num)