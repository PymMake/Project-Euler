'''What is the greatest product of four adjacent numbers in the same direction (up, down, left,
 right, or diagonally) in the 20×20 grid?

在这个20×20方阵中，四个在同一方向（从下至上、从上至下、从右至左、从左至右或者对角线）上相邻的数的乘
积最大是多少？'''

num = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
num1 = num.replace('\n',' ')
#每行20个数=40+20=60个字符  总共60*20-1=1199
#行line 列column 斜oblique
L = []
for x in range(0,20):
    for i in range(x*60+0,x*60+59,3):
        a = int(num1[i:i+2])
        L.append(a)
#到这里把所有数放入list：L中

L1 = []

line = 0
for x1 in range(0,20):
    for i1 in range(x1*20+0,x1*20+17):
        line = L[i1]*L[i1+1]*L[i1+2]*L[i1+3]
        L1.append(line)

column = 0
for i2 in range(0,340):#不是341从0开始计数
    column = L[i2]*L[i2+20]*L[i2+40]*L[i2+60]
    L1.append(column)

oblique1 = 0
for x3 in range(0,17):
    for i3 in range(x3*20+0,x3*20+17):
        oblique1 = L[i3]*L[i3+21]*L[i3+42]*L[i3+63]
        L1.append(oblique1)

oblique2 = 0
for x4 in range(0,17):
    for i4 in range(x4*20+3,x4*20+21):
        oblique2 = L[i4]*L[i4+19]*L[i4+38]*L[i4+57]
        L1.append(oblique2)
