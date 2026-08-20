def calcular_desconto(preco: float, percentual: float) -> float:
    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")
 
    if percentual < 0 or percentual > 100:
        raise ValueError("O percentual deve estar entre 0 e 100.")
 
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
 
    return round(preco_final, 2)
 
 
if __name__ == "__main__":
    resultado = calcular_desconto(100.0, 10.0)
    print(f"Preço final: R$ {resultado:.2f}")
