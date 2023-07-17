import os
import myPet

if __name__ == '__main__':
    flag = True
    opcion = 0
    while flag:
       # os.system('clear')
        print('*'*35)
        print(' ------ WELCOME MYPETS ------- ')
        print('1. GESTION DE VETERINARIO')
        opcion = input('digite opcion: ')
        if (opcion == '1'):
            os.system('clear')
            print(""""GESTION VETERINARIO
    1. Agregar veterinario
    2. Buscar veterinario
    3. Mostrar información de un veterinario
    4. Volver al menú principal""")
            opcionV = input('digite opcion: ')
            if (opcionV == '1'):
                os.system('clear')
                myPet.addVeterinario()
            elif (opcionV == '2'):
                myPet.shearVet()
 