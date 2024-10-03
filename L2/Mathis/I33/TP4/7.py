def hammingweight(n):
    poids = 0
    while n != 0:
        poids += n & 1
        n = n >> 1
    return poids


print(hammingweight(25))
