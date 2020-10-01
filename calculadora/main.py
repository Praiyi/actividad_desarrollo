from procedimientos import *

while(True):

    a = 0
    b = 0 
    resultado = 0
    print ("""
    __________Hola-esta-es-tu-calculadora__________

    Usted quiere:

    a) Sumar 
    b) Restar
    c) Multiplicar
    d) Dividir

    """)
    op= input("->")

    if op == 'a' or op == 'A':
        
        resultado = Suma()
        print("Su resultado es: ", resultado)
        
        pass

    else:
        print('Opcion invalida')