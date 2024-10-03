def eval_poly_F2(P,b):
    result = 0
    for i in range(-1, -len(P), -1):
        result = result ^ P[i]
        result = result & b
    return result ^ P[i - 1]

print(eval_poly_F2([1,1,1,0,0,1], 1))
