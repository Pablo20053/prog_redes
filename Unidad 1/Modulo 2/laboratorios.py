''' Nombre: Juan Pablo López Ramírez
    Descripcion: Uso de print
'''
#2.1.1.6 LABORATORIO: La función print()
'''
print("Fundamentos","Programación","en", sep="***", end="...")
print("Python")
'''



''' Nombre: Juan Pablo López Ramírez
    Descripcion: Flecha
'''
#2.1.1.19 LABORATORIO: Dando formato a la salida
'''print("     *\n","   * *\n","  *   *\n"," *     *\n","***   ***\n","  *   *\n","  *   *\n","  *****")
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)'''


''' Nombre: Juan Pablo López Ramírez
    Descripcion: El uso del escape "\" en cadenas
'''
#2.2.1.11 LABORATORIO: Literales de Python - Cadenas
'''print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")'''



''' Nombre: Juan Pablo López Ramírez
    Descripcion: Uso de variables 
'''
#2.4.1.7 LABORATORIO: Variables
'''
juan=3
maria=5
adan=6
juan=int(juan)
maria=int(maria)
adan=int(adan)
print(juan,",",+maria,",",+adan)
total_manzanas=juan+maria+adan
print(total_manzanas)
'''



''' Nombre: Juan Pablo López Ramírez
    Descripcion: Convertir millas a kilometros 
'''
#2.4.1.9 LABORATORIO: Variables, un sencillo convertidor
'''kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
'''



''' Nombre: Juan Pablo López Ramírez
    Descripcion: Evaluar una expresion usando diferentes operadores y expresiones
'''
#2.4.1.10 LABORATORIO: Operadores y expresiones
'''x =  -1
x = float(x)
y=(3*x**3)-(2*x**2)+3*x-1
print("y =", y)'''



''' Nombre: Juan Pablo López Ramírez
    Descripcion: Calcular cuantos segundos tiene un cierto numero de horas
'''
#2.5.1.2 LABORATORIO: Comentarios
'''
# este programa calcula los segundos en cierto número de horas determinadas 
# este programa fue escrito hace dos días

a = 2 # número de horas
seconds = 3600 # número de segundos en una hora

print("Horas: ", a) #imprime el numero de horas
print("Segundos en Horas: ", a * seconds) # se imprime el numero de segundos en determinado numero de horas

#aquí también se debe de imprimir un "Adiós", pero el programador no tuvo tiempo de escribirlo jaja
#este el es fin del programa que calcula el numero de segundos en 2 horas
'''



''' Nombre: Juan Pablo López Ramírez
    Descripcion: Ingresar 2 numeros y ejecutar las 4 operaciones basicas
'''
#2.6.1.9 LABORATORIO: Entradas y salidas simples
'''a=2.0 # ingresa un valor flotante para la variable a aquí
b=3.0 # ingresa un valor flotante para la variable b aquí

# muestra el resultado de la suma aquí 
print(a+b)
# muestra el resultado de la resta aquí
print(a-b)
# muestra el resultado de la multiplicación aquí
print(a*b)
# muestra el resultado de la división aquí
print(a/b)

print("\n¡Eso es todo, banda!")
'''



''' Nombre: Juan Pablo López Ramírez
    Descripcion: Ejecutar una formula usando correctamente la jerarquia de operadores
'''
#2.6.1.10 LABORATORIO: Operadores y expresiones
'''x = float(input("Ingrese el valor para x: "))

# Escribe tu código aquí.
y=(1/(x+(1/(x+(1/(x+(1/x)))))))
print("y =", y)
'''



''' Nombre: Juan Pablo López Ramírez
    Descripcion: Mostrar la hora de salida de un evento segun una hora y los minutos de duracion
'''
#2.6.1.11 LABORATORIO: Operadores y expresiones
'''def calcular_hora_final(hora_inicio, minutos_inicio, duracion_minutos):
  # Calcular los minutos totales
  minutos_totales = minutos_inicio + duracion_minutos

  # Ajustar los minutos para que estén entre 0 y 59
  horas_extra, minutos_final = divmod(minutos_totales, 60)

  # Calcular la hora final, ajustando para las 24 horas
  hora_final = (hora_inicio + horas_extra) % 24

  return hora_final, minutos_final

# Pedimos al usuario los datos de entrada
hora_inicio = int(input("Ingrese la hora de inicio (0-23): "))
minutos_inicio = int(input("Ingrese los minutos de inicio (0-59): "))
duracion_minutos = int(input("Ingrese la duración del evento en minutos: "))

# Calculamos la hora final
hora_final, minutos_final = calcular_hora_final(hora_inicio, minutos_inicio, duracion_minutos)

# Imprimimos el resultado
print("La hora final es:", hora_final, ":", minutos_final)'''