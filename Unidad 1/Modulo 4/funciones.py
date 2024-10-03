def greeting(name, edad):
    return "Hi " + str(name) + " tienes " + str(diasVividos(edad)) + " dias "
    

def diasVividos(year):
    return year*365

print(greeting("Jhon",50))
