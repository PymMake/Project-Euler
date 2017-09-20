'''Sum square difference
The sum of the squares of the first ten natural numbers is,
12 + 22 + … + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + … + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

平方的和与和的平方之差
前十个自然数的平方的和是
12 + 22 + … + 102 = 385
前十个自然数的和的平方是
(1 + 2 + … + 10)2 = 552 = 3025
因此前十个自然数的平方的和与和的平方之差是 3025 − 385 = 2640。
求前一百个自然数的平方的和与和的平方之差。'''

a = (sum(range(101)))**2 - sum(i**2 for i in range(101))#一行for循环语法
print(a)
