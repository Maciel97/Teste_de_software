import pytest
 
from frete import calcular_frete
 
 
@pytest.mark.parametrize(
    "subtotal, esperado",
    [
        (199.99, 20.0),
        (200.00, 0.0),
        (200.01, 0.0),
    ],
)
def test_calcular_frete_valores_limite(
    subtotal,
    esperado
):
    resultado = calcular_frete(subtotal)
 
    assert resultado == esperado
 
 
def test_subtotal_negativo_deve_gerar_erro():
    with pytest.raises(ValueError, match="subtotal"):
        calcular_frete(-1.0)