# crea una funcion que calcule el numero de columna de una hoja exel
# teniendo en cuenta su nombre.
#- Las columnas se designan por letra de la "A" a la "Z".
#- Ej: A = 1, Z = 26, AA = 27, CA = 79.

import string

def calculate_column_number(column_name: str)-> int:
    
    column_number = 0
    
    alphabet = list(string.ascii_uppercase)
    
    for letter in column_name.upper():
        column_number = (column_number * len(alphabet)) + (alphabet.index(letter) + 1)
    
    return column_number

print(calculate_column_number("A"))
print(calculate_column_number("Z"))
print(calculate_column_number("AA"))
print(calculate_column_number("CA"))
print(calculate_column_number("ZZZ"))