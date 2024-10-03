def ord(a,n):

    x = a
    y = n

    while y != 0:

        x,y = y,x % y

    return (n)//(x)

k = 10
for i in range(0,k):
    print(ord(i,k),i)
