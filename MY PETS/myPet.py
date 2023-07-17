import json
import os.path

veterinarios = [] 
file_path = 'MY PETS/data/veterinarios.json'

def core():
    

def addVeterinario():
   # global veterinarios  # Declarar la variable como global
    nameV = input("Ingrese el nombre: ").upper()
    idV = input("Ingrese la identificación: ").upper()
    titV = input("Ingrese el título: ").upper()
    veterinario = {'id': idV, 'name': nameV, 'Titul': titV}
    veterinarios.append(veterinario)
    
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
        
        existing_data.extend(veterinarios)
     #   veterinarios = existing_data
        
    with open(file_path, 'w') as f:
        json.dump(veterinarios, f, indent=3)
    input('Presione enter para continuar.')
    
def shearVet():    
    shear = input("¿Desea buscar por nombre (N) o por ID (I)? ").upper()
    if (shear == 'N'):
        nombre = input("Ingrese el nombre a buscar: ").upper()
        resultados = [veterinario for veterinario in veterinarios if veterinario['name'] == nombre]
        if resultados:
            for resultado in resultados:
                print(resultado)
            input('desea continuar')
        else:
            input("No se encontraron veterinarios con ese nombre.")
            
    elif (shear == 'I'):
        id = input("Ingrese el ID a buscar: ").upper()
        resultados = [veterinario for veterinario in veterinarios if veterinario['id'] == id]
        if resultados:
            for resultado in resultados:
                print(resultado)
            input('desea continuar')
        else:
            input("No se encontraron veterinarios con ese ID.")
    else:
        input("Opción inválida.")    