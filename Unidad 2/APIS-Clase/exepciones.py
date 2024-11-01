try: 
    num = int(input("Ingresa tu edad: "))
    res = 1/num
    print(num)
except ValueError as error: #Esta es para cuando se ingresa un string en un campo entero
    print("Estas mal. Ingresa un numero. Entiende, cabrón")
except ZeroDivisionError as divisionZero: #Este es cuando se divide por 0
    print("no la hagas, como vas a dividir entre 0, burrito")
except Exception: #Este maneja todas las exepciones de manera muy general pues
    print("Tienes un error")
finally:
    print("Si no sucede de todas formas me ejecuto")