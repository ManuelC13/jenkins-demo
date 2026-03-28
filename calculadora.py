def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", sumar(2, 3))
    print("10 - 4 =", restar(10, 4))
    print("3 x 5 =", multiplicar(3, 5))
    print("10 / 2 =", dividir(10, 2))
