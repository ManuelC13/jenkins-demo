import pytest
from calculadora import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(10, 4) == 6
    assert restar(0, 5) == -5

def test_multiplicar():
    assert multiplicar(3, 5) == 15
    assert multiplicar(0, 100) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3

def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)
