for numero in range(5):
    print(numero, numero * 'hola mundo')



buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre el numero")



for char in "Ultimate Python":
    print(char)