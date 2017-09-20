'''10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

第10001个素数
列出前6个素数，它们分别是2、3、5、7、11和13。我们可以看出，第6个素数是13。
第10,001个素数是多少？'''

import math

def func(x):
    m = int(math.sqrt(x)+1)
    for i in range(2,m):
        if x%i==0:
            return 0
    return 1

x = 3
a = 2
while True:
    x += 2
    if func(x):
        a += 1

    if a == 10001:
        break
print(x)
