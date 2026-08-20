from calculadora import calcular_desconto
from frete import calcular_frete
 
 
def calcular_total_pedido(
    preco: float,
    percentual_desconto: float,
    quantidade: int
) -> float:
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
 
    preco_com_desconto = calcular_desconto(
        preco,
        percentual_desconto
    )
 
    subtotal = preco_com_desconto * quantidade
    frete = calcular_frete(subtotal)
    total = subtotal + frete
 
    return round(total, 2)
 
 
if __name__ == "__main__":
    total = calcular_total_pedido(
        preco=100.0,
        percentual_desconto=10.0,
        quantidade=1
    )
    print(f"Total do pedido: R$ {total:.2f}")