import pytest
from geometria.geometria import classificar_triangulo
import re

def test_triangulo_sem_erro():
    a = 3
    b = 5
    c = 3

    resultado = classificar_triangulo(a, b, c)

    assert resultado == ("Isósceles")

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