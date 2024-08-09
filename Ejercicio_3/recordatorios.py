# Contexto:

# El siguiente código de programa incluye una serie de eventos que se desea recordar.
# El programa permite agregar, editar, eliminar, ordenar y finalmente mostrar los eventos.

# Para ejecutar el programa se debe utilizar el siguiente comando:
# python recordatorios.py

######################################################################################################

# Lista recordatorios
recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada, es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

# 1. Agregue un evento el 2 de febrero de 2021 a las 6 de la mañana para "Empezar el año".
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

# 2. Editar el evento del 15 de julio, ya que no es feriado. Cambiar la fecha al 16 de julio.
for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'

# 3. Porque se debe trabajar, eliminar el evento del día del trabajo.
recordatorios = [evento for evento in recordatorios if evento[0] != '2021-05-01']

# 4. Agregar cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Orden cronológico
recordatorios.sort()

# Output
print(recordatorios)
