import math
def lcm(a,b):
    return a*b//math.gcd(a,b)#gcd 求两数的最大公约数
#两数的积除以最大公约数就是最小公倍数
n = 3
m = lcm(n-1,n)
while n <= 20:
    m = lcm(m,n)
    n += 1
print(m)