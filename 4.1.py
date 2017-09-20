L = []
for a in range(100,1000):
    for b in range(100,1000):
        num = a*b
        c = list(str(num))
        d = c[:]#拷贝 不能 ‘ = ’
        c.reverse()#翻转列表，只能是列表
        if d == c:
            L.append(num)


print(max(L))#最后一个并不是最大的
