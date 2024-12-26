def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def primeros_n_primos(n):
    primos = []
    num = 2
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos

# Imprimir los primeros 1000 números primos
primos = primeros_n_primos(1000)
for primo in primos:
    print(primo)