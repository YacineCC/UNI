def is_of_order_mult(a,t,n):
    # On va tester les div propres de t
    lim = int(t ** 0.5) + 1
    i = 1
    while i <= lim:
        # Si i | t, on teste a ^ i %n
        if (not t % i) and ((pow(a, i, n) == 1) or (i != 1 and (pow(a, t // i, n) == 1))):
            return False
        i += 1

    # Si on arrive jusqu'ici t est l'ordre de a si a^t % n = 1
    return pow(a, t, n) == 1


print(is_of_order_mult(72,63,83))
print(is_of_order_mult(278180535499608309,3481129377620,1152921504606847517))
print(is_of_order_mult(14,12,37))
