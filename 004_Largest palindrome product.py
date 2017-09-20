'''Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

最大回文乘积
回文数就是从前往后和从后往前读都一样的数。由两个2位数相乘得到的最大回文乘积是 9009 = 91 × 99。
找出由两个3位数相乘得到的最大回文乘积。'''
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
