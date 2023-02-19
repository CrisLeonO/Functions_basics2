'''Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento).
# Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]'''


def contar(num=int(input("Digite un numero mayor a 0: "))):
    list = []

    for x in range(num, -1, -1):
        list.append(x)
    return list


print(contar())
# -----------------------------------------------------------------------------------
print('*' * 20)

# Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
# Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2


def imprimir(num1=int(input('Digite un primer numero: ')), num2=int(input('Digite un segundo numero: '))):
    list = [num1, num2]
    print(list[0])
    return list[1]


print(imprimir())

# --------------------------------------------------------------------------------------------------------------------------------------------------
print('*' * 20)
'''Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)'''


def longitud():
    list = [5, 6, 7, 8, 9]
    x = len(list)
    y = x + list[0]
    return y


print(longitud())
print('*' * 20)
# ----------------------------------------------------------------------------------------------------------------------------------
'''Valores mayores que el segundo:
escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor.
Imprime cuántos valores son
luego devuelve la lista nueva.
Si la lista tiene menos de 2 elementos, has que la función devuelva False

Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False'''


def mayores():
    list1 = [5, 2, 3, 2, 1, 6]
    list2 = []

    if len(list1) < 2:
        return False

    for x in range(0, len(list1)):
        if list1[x] > list1[1]:
            list2.append(list1[x])
    print(len(list2))
    return list2


print(mayores())
print('*' * 20)

'''Esta longitud, ese valor: 
escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.

Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]'''


def longitud(size, value):
    long = []

    for x in range(0, size):
        long.append(value)
    return long


print(longitud(4, 6))
print(longitud(3, 2))
