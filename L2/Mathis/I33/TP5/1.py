def multbyalpha(b,f):
    result = b << 1
    if len(bin(result)[2:]) >= len(bin(f)[2:]):
        result = result ^ f

    return result

print(multbyalpha(3, 13))
print(multbyalpha(3,47))
print(multbyalpha(28,37))
