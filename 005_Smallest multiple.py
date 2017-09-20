'''Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

最小倍数
2520是最小的能够被1到10整除的数。
最小的能够被1到20整除的正数是多少？'''

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
