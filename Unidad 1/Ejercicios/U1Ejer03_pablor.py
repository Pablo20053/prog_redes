'''
   Nombre: Juan Pablo López Ramírez
   Grupo: GIR0641
   Descripción: Ejercicio 03 Manejo de colecciones
   Fecha: 03/10/2024
'''
#Escribe la instrucción para agregar una colección vacía con el nombre de tu grupo
GIR0641 = []
#Crear una lista llamada numeros_control 
numeros_control = [1219100524, 1219100537, 1219100543, 1219101033, 1219100484]

#Crear una lista llamada nombres_grupo para almacenar los nombres de los comañeros
nombres_grupo = []

#Escribe una instrucción que imprima todo el contenido de la lista.
print("Números de control:", numeros_control)

#Mediante un for each que itera la lista de los números de control escribe las instrucciones:
for num_control in numeros_control:
    # Solicitar los nombres de los estudiantes de acuerdo al número control
    print("Ingresa el nombre del No. Control", num_control)
    
    # Mediante la función input solicite el nombre
    nombre = input("Ingresa el nombre: ")
    
    # Una vez que se capture el nombre agrega el dato a la colección haciendo corresponder el número de control con el nombre
    nombres_grupo.append(nombre)

# Imprimir el contenido de la colección
print("Nombres de los compañeros:")
for i in range(len(numeros_control)):
    print(f"Número de control {numeros_control[i]}: {nombres_grupo[i]}")

# Escribe un ciclo infinito que busque en la colección un número de control existente donde despliegue el nombre y aborte el ciclo; en caso contrario, deberá de indicar "El número de control no fue encontrado Inténtalo de nuevo"
while True:
    num_control_buscar = int(input("Ingresa el número de control a buscar: "))
    
    if num_control_buscar in numeros_control:
        indice = numeros_control.index(num_control_buscar)
        print(f"El nombre del estudiante con el número de control {num_control_buscar} es: {nombres_grupo[indice]}")
        break
    else:
        print("El número de control no fue encontrado. Inténtalo de nuevo.")
