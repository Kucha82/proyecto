print("=========")
print("conversor")
print("========= \n")

print("Menu de opciones: \n")
print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero. \n")

opcion= int(input("Cual es tu opcion deseada?: "))

if opcion == 1:
    print("\n Conversor de numero a palabra. \n")
    opcion_uno = int(input("Cual es el numero que desea convertir a palabra?: "))
    if opcion_uno ==1:
        print("El numero es UNO")
    elif opcion_uno == 2:
        print("El numero es DOS")
    elif opcion_uno == 3:
        print("El numero es TRES")
    elif opcion_uno == 4:
        print("El numero es CUATRO")
    elif opcion_uno == 5:
        print("El numero es CINCO")
    else:
        print("El numero seleccionado no esta registrado.")
        
        
elif opcion ==2:
    print("\n Conversor de palabra a numero. \n")
    opcion_dos= input(" Cual es la palabra que desea convertir a numero?: ")
    opcion_dos = opcion_dos.lower()
    
    if opcion_dos== "uno":
        print("EL numero es '1'")
    elif opcion_dos== "dos":
        print("EL numero es '2'")
    elif opcion_dos== "tres":
          print("EL numero es '3'")
    elif opcion_dos== "cuatro":
          print("EL numero es '4'")
    elif opcion_dos== "cinco":
          print("EL numero es '5'")
    else:
        print("el numero no esta registrado")
        

else:
    print(" opcion no disponible.")

print("Fin.")
