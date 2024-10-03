def eval_poly(P,b):
    result = 0
    for i in range(-1, -len(P), -1):
        result += P[i]
        result *= b
    return result + P[i - 1]


print(eval_poly([4, 5, 3], 2))
