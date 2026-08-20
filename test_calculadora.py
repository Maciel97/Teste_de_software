import pytest

from Teste_de_software.calculadora import calcular_desconto


@pytest.mark.parametrize(
    "preco, percentual, esperado",
    [
        (200.0, 10.0, 180.0),
        (150.0, 20.0, 120.0),
        (99.90, 0.0, 99.90),
        (100.0, 100.0, 0.0),
    ],
)
def test_calcular_desconto_cenarios_validos(preco, percentual, esperado):
    resultado = calcular_desconto(preco, percentual)
    assert resultado == esperado