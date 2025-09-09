import pytest
from geometria.geometria import classificar_triangulo
import re

def test_triangulo_sem_erro_is():
    a = 3
    b = 5
    c = 3

    resultado = classificar_triangulo(a, b, c)

    assert resultado == ("Isósceles")

def test_triangulo_sem_erro_eq():
    a = 5
    b = 5
    c = 5

    resultado = classificar_triangulo(a, b, c)

    assert resultado == ("Equilátero")

def test_triangulo_sem_erro_es():
    a = 3
    b = 2
    c = 4

    resultado = classificar_triangulo(a, b, c)

    assert resultado == ("Escaleno")





def test_envio_string_a():
    a = "oi"
    b = 5
    c = 3

    mensagem = "Os valores devem ser numéricos."

    with pytest.raises(TypeError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

def test_envio_string_b():
    a = 3
    b = "oi"
    c = 3

    mensagem = "Os valores devem ser numéricos."

    with pytest.raises(TypeError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

def test_envio_string_c():
    a = 3
    b = 5
    c = "oi"

    mensagem = "Os valores devem ser numéricos."

    with pytest.raises(TypeError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

def test_envio_numero_negativo_a():
    a = -4
    b = 5
    c = 3

    mensagem = "Lados devem ser positivos."

    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

def test_envio_numero_negativo_b():
    a = 3
    b = -4
    c = 3

    mensagem = "Lados devem ser positivos."

    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

def test_envio_numero_negativo_c():
    a = 3
    b = 5
    c = -4

    mensagem = "Lados devem ser positivos."

    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

def test_triangulo_ab_menor_que_c():
    a = 2
    b = 2
    c = 5

    mensagem = "Lados não formam um triângulo."

    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

def test_triangulo_ac_menor_que_b():
    a = 2
    b = 5
    c = 2

    mensagem = "Lados não formam um triângulo."

    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

def test_triangulo_bc_menor_que_a():
    a = 5
    b = 2
    c = 2

    mensagem = "Lados não formam um triângulo."

    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)