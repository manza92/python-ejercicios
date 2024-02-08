# def restar( a = 0, b = 0):
#     return a - b
# resultado = restar()
# print(f'Resultar restar: {restar(9,2)}')
#
# def listarNombres(*nombres):
#     for nombre in nombres:
#         print(nombre)
# listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')
# listarNombres('Laura', 'Carlos')

'''Crear una funcion para sumar los valores recibidos de tipo numerico, utilizando argumentos variables *args como parametro de la funcion y regresar como resultado la suma de todos ls valores pasados como argumentos'''

#Definimos nuestra funcion para sumar valores
# def sumar_valores(*args):
#     resultado = 0
#     #iteramos cada elemento
#     for valor in args:
#         #resultado = resultado + valor
#         resultado += valor
#     return resultado
#
# #llamada a la funcion
#
# print(sumar_valores(3,5,9,4,6))

'''Crea una funcion para multiplicar los valores recibido de tipo numerico, utilizando argumentos variables *args como parametro de la funcion y regresar como resultado la multiplicacion de todos los valores pasados como argumentos'''

# #Definicion de la funcion para multiplicar valores
# def multiplicar_valores(*numeros):
#     resultado = 1
#     for numero in numeros:
#         #resultado = resultado * numero
#         resultado *= numero
#     return resultado
# #llamada a la funcion
# print(multiplicar_valores(3,5,15))

# def listarTerminos(**kwargs):
#     for llave, valor in kwargs.items():
#         print(f'{llave}: {valor}')
#
# listarTerminos(IDE='Integrated development Enviroment', PK= 'Primary Key')
# listarTerminos(DBMS= 'Database Management System')
#
# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)
#
# nombres = ['Juan', 'Karla','Guillermo']
# desplegarNombres(nombres)
# desplegarNombres('Carlos')
# desplegarNombres((8,9))
# desplegarNombres([10,11])


'''calcular el factorial'''

#5! = 5 * 4 * 3 * 2 * 1
#5! = 5 * 4 * 3 * 2
#5! = 5 * 4 * 6
#5! = 5 * 24
#5! = 120

# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * factorial(numero-1)
# numero = 8
# resultado = factorial(numero)
# print(f'El factorial de {numero} es {resultado}')

def imprimir(numero):
    #condicion de salida
    if numero > 0:
        #imprimir el valor de
        print(numero)
        #llamar a la funcion con x-1
        imprimir(numero-1)
        #llamar a la funcion con 5
imprimir(9)

