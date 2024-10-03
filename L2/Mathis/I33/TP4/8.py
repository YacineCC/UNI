def hammingweight(n):
    poids = 0
    while n != 0:
        poids += n & 1
        n = n >> 1
    return poids


def test(n):
    print(f"n: {bin(n)[2:]}, n - 1: {bin(n - 1)[2:]} et n & (n - 1): {bin(n & (n - 1))[2:]}, poids: {hammingweight(n)}, t: {hammingweight(n & (n - 1)) + 1}")



def testHamming(n):
    if n == 0:
        return 1
    return testHamming(n & (n - 1)) + 1


def hammingweight2(n):
    tmp = n & (n - 1)
    result = 1
    while tmp != 0:
        result += 1
        tmp = tmp & (tmp - 1)
    return result

for i in range(1, 11):
    test(i)
    print()
    print(hammingweight2(i))
