import pytest
 
from pedido import calcular_total_pedido
 
 
@pytest.mark.parametrize(
    "preco, desconto, quantidade, esperado",
    [
        (100.0, 10.0, 1, 110.0),
        (100.0, 10.0, 3, 270.0),
        (50.0, 0.0, 3, 170.0),
        (50.0, 0.0, 4, 200.0),
    ],
)
def test_calcular_total_pedido_integracao(
    preco,
    desconto,
    quantidade,
    esperado
):
    resultado = calcular_total_pedido(
        preco,
        desconto,
        quantidade
    )
 
    assert resultado == esperado
 
 
@pytest.mark.parametrize(
    "quantidade",
    [0, -1],
)
def test_quantidade_invalida_deve_gerar_erro(
    quantidade
):
    with pytest.raises(ValueError, match="quantidade"):
        calcular_total_pedido(
            100.0,
            10.0,
            quantidade
        )