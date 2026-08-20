def calcular_frete(subtotal: float) -> float:
    if subtotal < 0:
        raise ValueError("O subtotal não pode ser negativo.")
 
    if subtotal >= 200:
        return 0.0
 
    return 20.0
 
 
if __name__ == "__main__":
    print(calcular_frete(199.99))
    print(calcular_frete(200.00))
