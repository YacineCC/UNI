def poids(n):
    return bin(n).count("1")


def prod_mat_vec_F2(M, V):
    result = 0

    for i, m in enumerate(reversed(M)):
        bit = poids(m & V) & 1
        result = result ^ (bit << i)

    return result


def test_prod_mat_vec_F2():
    assert prod_mat_vec_F2([9, 15, 5], 7) == 6
