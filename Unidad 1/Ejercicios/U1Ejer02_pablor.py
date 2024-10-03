'''
   Nombre: Juan Pablo López Ramírez
   Grupo: GIR0641
   Descripción: Ejercicio 02 Crear una lista de nombres y realizar operaciones básicas
   Fecha: 03/10/2024
'''
#Crea una lista con cuatro de tus mejores compañeros del grupo: Francisco, Pedro, Juan, Fernando
nombres = ["Francisco", "Pedro", "Juan", "Fernando"]
#Escribe la instrucción para desplegar el tamaño de la lista a través de la leyenda “El tamaño de la lista es”.
print("El tamaño de la lista es:", len(nombres))
#6. Escribe la instrucción para imprimir el contenido de la lista a través de la leyenda “El contenido de la lista es ”
print("El contenido de la lista es:", nombres)
#Cambiar el segundo elemento de la lista por “Joaquín”
nombres[1] = "Joaquín"
#Agrega un elemento más a la lista con el nombre “Luis Miguel”, utiliza la instrucción: nombres.append()
nombres.append("Luis Miguel")
#Elimina el tercer elemento de la lista.
del nombres[2]
#Despliega la lista en orden inverso y separados con un carácter cada nombre
print(nombres[::-1], sep =" ")
