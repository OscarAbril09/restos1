import os
import myPet

def hgdhfg():
    print('sera?')
if __name__ == '__main__':
    flag = True
    opcion = 0
    while flag:
        os.system('clear')
        print('*'*35)
        print(' ------ WELCOME MYPETS ------- ')
        print('1. Registrar')
        opcion = input('digite opcion: ')
        if (opcion == '1'):
            myPet.addNum()
 