#4.3.1.6 LABORATORIO: Un año bisiesto: escribiendo tus propias funciones
''' Nombre: JUan Pablo López Ramírez
    Descripcion: Tu tarea es escribir y probar una función que toma un argumento 
    (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.
    Fecha: 02 de octubre

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False
''

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("fallido")
'''

#4.3.1.7 LABORATORIO: ¿Cuántos días?: escribiendo y utilizando tus propias funciones
''' Nombre: JUan Pablo López Ramírez
    Descripcion: Tu tarea es escribir y probar una función que toma 
    dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado 
    (mientras que solo febrero es sensible al valor year, tu función debería ser universal).
    Fecha: 02 de octubre

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False

def days_in_month(year, month):
	if month < 1 or month > 12:
		return None
	dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	aux = dias[month - 1]
	if month == 2 and is_year_leap(year):
		aux = 29
	return aux

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
'''
#4.3.1.8 LABORATORIO: Día del año: escribiendo y utilizando tus propias funciones
''' Nombre: JUan Pablo López Ramírez
    Descripcion: Tu tarea es escribir y probar una función que toma 
    tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera 
    de los argumentos no es válido.
    Fecha: 02 de octubre

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False

def days_in_month(year, month):
	if month < 1 or month > 12:
		return None
	dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	aux = dias[month - 1]
	if month == 2 and is_year_leap(year):
		aux = 29
	return aux

def day_of_year(year, month, day):
    if day > 31 or day < 1 and month < 1 or month > 12:
        return None
    else:
        dias = days_in_month(year, month)
        return dias - day

print(day_of_year(2000, 11, 20))
'''

#4.3.1.9 LABORATORIO: Números primos: ¿Cómo encontrarlos?
''' Nombre: JUan Pablo López Ramírez
    Descripcion: Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.
    Fecha: 02 de octubre

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
	if is_prime(i + 1):
		print(i + 1, end=" ")
print()
'''

#4.3.1.10 LAB: Convirtiendo el consumo de combustible
''' Nombre: JUan Pablo López Ramírez
    Descripcion: Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.
    Fecha: 02 de octubre

def liters_100km_to_miles_gallon(liters):
    galones = liters / 3.785
    millas = 100 / 1.609
    return millas / galones

def miles_gallon_to_liters_100km(miles):
    litros = 3.785
    km = miles * 1609.344 / 1000 / 100
    return litros / km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
'''

#4.7.2.1 PROYECTO: TIC-TAC-TOE
''' Nombre: JUan Pablo López Ramírez
    Descripcion: Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario.
    Fecha: 02 de octubre

from random import randrange

def MostrarTablero(tablero):
    for fila in tablero:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print(f"|   {fila[0]}   |   {fila[1]}   |   {fila[2]}   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def IngresarMovimiento(tablero):
    movimiento = int(input("Ingresa tu movimiento "))
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == movimiento:
                tablero[fila][columna] = 'O'
                return

def GenerarListaDeCamposLibres(tablero):
    campos_libres = []
    for fila in range(3):
        for columna in range(3):
            if isinstance(tablero[fila][columna], int):
                campos_libres.append((fila, columna))
    return campos_libres

def ComprobarVictoria(tablero, signo):
    for fila in tablero:
        if fila.count(signo) == 3:
            return True
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == signo:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == signo:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == signo:
        return True
    return False

def MovimientoMaquina(tablero):
    campos_libres = GenerarListaDeCamposLibres(tablero)
    movimiento = randrange(len(campos_libres))
    fila, columna = campos_libres[movimiento]
    tablero[fila][columna] = 'X'

# Inicializamos el tablero
tablero = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

# Ciclo del juego
while True:
    MostrarTablero(tablero)
    IngresarMovimiento(tablero)
    if ComprobarVictoria(tablero, 'O'):
        MostrarTablero(tablero)
        print("¡Has Ganado!")
        break
    MovimientoMaquina(tablero)
    if ComprobarVictoria(tablero, 'X'):
        MostrarTablero(tablero)
        print("La máquina ha ganado.")
        break
    if len(GenerarListaDeCamposLibres(tablero)) == 0:
        MostrarTablero(tablero)
        print("Es un empate.")
        break
'''