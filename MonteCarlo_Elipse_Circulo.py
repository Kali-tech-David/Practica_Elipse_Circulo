import math
import random
 
 
def punto_aleatorio(a, b):
    
    x = a * (2 * random.random() - 1)
    y = b * (2 * random.random() - 1)
    return x, y
 
 
def en_elipse(x, y, a, b):
    return x * x / (a * a) + y * y / (b * b) <= 1
 
 
def en_circulo(x, y, b):
    return x * x + y * y <= b * b
 
 
def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("  Debe ser un entero positivo.")
        except ValueError:
            print("  Entrada invalida, escriba un numero entero.")
 
 
def main():
    print("=== Area entre elipse y circulo inscrito (Monte Carlo) ===")
    a = leer_entero_positivo("a (semieje en x): ")
    b = leer_entero_positivo("b (semieje en y, a > b): ")
    while a <= b:
        print("  Debe cumplirse a > b.")
        b = leer_entero_positivo("b (semieje en y, a > b): ")
    n = leer_entero_positivo("Cantidad de numeros aleatorios: ")
 
    puntos_elipse = 0
    puntos_circulo = 0
    for _ in range(n):
        x, y = punto_aleatorio(a, b)
        if en_elipse(x, y, a, b):
            puntos_elipse += 1
            if en_circulo(x, y, b):
                puntos_circulo += 1
 

    area_circulo = math.pi * b ** 2
    area_elipse = math.pi * a * b
    dif_formula = area_elipse - area_circulo
 
    print("\n--- Resultados ---")
    print(f"Puntos generados (rectangulo): {n}")
    print(f"Puntos dentro de la elipse   : {puntos_elipse}")
    print(f"Puntos dentro del circulo    : {puntos_circulo}")
 
    if puntos_circulo == 0:
        print("Ningun punto cayo en el circulo; use mas puntos.")
        return
 
    # puntos_elipse / puntos_circulo = area_elipse / area_circulo
    area_elipse_mc = area_circulo * puntos_elipse / puntos_circulo
    dif_mc = area_elipse_mc - area_circulo
 
    print(f"\nDiferencia de areas por formula     : {dif_formula:.4f}")
    print(f"Diferencia de areas por Monte Carlo : {dif_mc:.4f}")
 
    error_pct = (dif_mc - dif_formula) / dif_formula * 100
    if error_pct >= 0:
        print(f"El area de Monte Carlo es {error_pct:.2f}% MAYOR que la de la formula.")
    else:
        print(f"El area de Monte Carlo es {abs(error_pct):.2f}% MENOR que la de la formula.")
 
 
if __name__ == "__main__":
    main()