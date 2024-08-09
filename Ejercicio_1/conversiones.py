# Contexto:

# Este script realiza conversiones de divisas:
# Toma como argumentos las tasas de conversión de cada moneda y el valor en pesos chilenos que se quiere convertir. 
# Los resultados se muestran con un decimal.

# Para ejecutar el programa se debe utilizar el siguiente comando:
# python conversiones.py 0.0046 0.093 0.0013 10000

######################################################################################################

import sys

def main():
    # Verificación de argumentos 
    if len(sys.argv) != 5:
        print("Uso: python conversiones.py <tasa_sol> <tasa_peso_argentino> <tasa_dolar_americano> <valor_peso_chileno>")
        sys.exit(1)

    # Tipo de dato
    tasa_sol = float(sys.argv[1])
    tasa_peso_argentino = float(sys.argv[2])
    tasa_dolar_americano = float(sys.argv[3])
    valor_peso_chileno = float(sys.argv[4])

    # Cálculo y resultado de las conversiones
    a_soles = valor_peso_chileno * tasa_sol
    a_peso_argentino = valor_peso_chileno * tasa_peso_argentino
    a_dolar_americano = valor_peso_chileno * tasa_dolar_americano

    # Output
    print(f"Los {valor_peso_chileno} pesos chilenos equivalen a:")
    print(f"{a_soles:.1f} Soles")
    print(f"{a_peso_argentino:.1f} Pesos Argentinos")
    print(f"{a_dolar_americano:.1f} Dólares americanos")

if __name__ == "__main__":
    main()
