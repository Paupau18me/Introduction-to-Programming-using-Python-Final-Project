def nums():
    n1 = int(input('\t\t\t1er numero: '))
    n2 = int(input('\t\t\t2do numero: '))
    return n1,n2
def suma():
    n1,n2 = nums()
    print('\n\t\t\t\t'+str(n1),'+',str(n2),'=',str(n1+n2))

def resta():
    n1,n2 = nums()
    print('\n\t\t\t\t'+str(n1),'-',str(n2),'=',str(n1-n2))

def prod():
    n1,n2 = nums()
    print('\n\t\t\t\t'+str(n1),'*',str(n2),'=',str(n1*n2))

def div():
    n1,n2 = nums()
    print('\n\t\t\t\t'+str(n1),'/',str(n2),'=',str(n1/n2))

sw = True

while sw is True:
    print('''
         _______________________________________
        |                                       |
        |              CALCULADORA              |
        |                                       |
        |    1. Suma                            |
        |    2. Resta                           |
        |    3. Multiplicación                  |
        |    4. Division                        |
        |    5. Salir                           |
        |                                       |
        |_______________________________________|         
    ''')

    case = int(input('\t\t\tIngrese la opción: '))

    if case == 1:
        suma()
    elif case == 2:
        resta()
    elif case == 3:
        prod()
    elif case == 4:
        div()
    elif case == 5:
        print('\n\t\t\tPrograma finalizado :D')
        sw = False
    else:
        print('\t\t\t¡Opcion no disponible! :c')