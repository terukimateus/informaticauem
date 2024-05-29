def soma(n: int) -> int:
    ''''''

    if n == 0:
        return 0
    return n + soma(n-1)

print(soma(5))
print(soma(2))
print(soma(4))