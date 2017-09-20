'''Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.

特殊毕达哥拉斯三元组
毕达哥拉斯三元组是三个自然数a < b < c组成的集合，并满足
a2 + b2 = c2
例如，32 + 42 = 9 + 16 = 25 = 52。
有且只有一个毕达哥拉斯三元组满足 a + b + c = 1000。求这个三元组的乘积abc。
'''

for a in range(3,335):
    for b in range(a,501):
        c = 1000 - a -b
        if a**2 + b**2 == c**2:
            print(a*b*c,a,b,c)
            break
