def minimum2(L):
    mini1 = L[1]
    mini2 = L[0]
    tab = []
    for i in L:

        if i < mini1 :
            mini2 = mini1
            mini1 = i
        elif(i < mini2 and i != mini1):
            mini2 = i
    return mini2



print(minimum2([8, 12, 13, 16, 17, 18, -6, -5, -1]))
print(minimum2([0, 3, 4, 6, 7, 9, 13, -15, -11, -6]))
print(minimum2([6, 9, -17, -13, -9, -7, -5, -1]))
print(minimum2([-19, 15, 17, -10, -5, -4]))
print(minimum2([1, 6, -14, 19, -13, -9, -7]))
print(minimum2([16, -15, 12, 15]))
print(minimum2([1, 4, 5, 11, -18, -15, -9]))
print(minimum2([2, 8, 9, 11, 12, 13, 14, 15]))
print(minimum2([0, 3, 6, 8, 12, -20, -18, -8, -1]))
print(minimum2([6, -20, 17, 19, -9, -6]))
"""-5
-11
-13
-10
-13
12
-15
8
-18
-9"""
