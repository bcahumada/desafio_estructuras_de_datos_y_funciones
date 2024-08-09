# Contexto:

# Este código sirve para:

# Leer un archivo, 
# Contar los caracteres y
# Contar las palabras únicas.

# Se proporcionará un texto de prueba contenido en el archivo  lorem_ipsum.txt.

# Para ejecutar el programa se debe utilizar el siguiente comando:
# python word_count.py lorem_ipsum.txt

#####################################################################################



import sys

def main():
    # Verificación de argumentos 
    if len(sys.argv) != 2:
        print("Uso: python word_count.py <ruta_del_archivo>")
        sys.exit(1)

    # Nombre del archivo del argumento 1
    archivo = sys.argv[1]

    try:
        # Lectura del archivo
        with open(archivo, "r") as file:
            texto = file.read()

        # Cuenta de caracteres distintos
        caracteres_distintos = len(set(texto))

        # Conteo de palabras distintas
        n_palabras = texto.split()  
        n_palabras_distintas = len(set(n_palabras))

        # Resultados/Output
        print(f"El número de caracteres distintos es: {caracteres_distintos}")
        print(f"El número de palabras distintas es: {n_palabras_distintas}")

    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")
        sys.exit(1)

if __name__ == "__main__":
    main()
