def ord(a,p):
    # On parcourt tous les entiers <= sqrt(p)
    # car 1 <= ord(a) <= p et ord(a) | p - 1.
    # Les diviseurs de p - 1 sont tous inférieurs à sqrt(p - 1)
    # sauf p - 1 lui même
    if a == 1: return 1
    lim = int((p - 1) ** 0.5) + 1
    i = 2

    candidats = [p - 1]
    while i <= lim:
        # On regarde s'il divise p - 1
        if (not (p - 1) % i):
            # si oui on regarde si a ^ i = 1 ou si
            # a ^ (p - 1) / i = 1
            tmp = (p - 1) // i
            if pow(a, i, p) == 1 and i not in candidats: candidats.append(i)
            if pow(a, tmp, p) == 1 and tmp not in candidats: candidats.append(tmp)

        i += 1

    # Si on arrive jusque là, a est d'ordre p - 1
    return min(candidats)

print(ord(13,17))
