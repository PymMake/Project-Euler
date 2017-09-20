'''Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

素数的和
所有小于10的素数的和是2 + 3 + 5 + 7 = 17。
求所有小于两百万的素数的和。'''

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
