import os
import json

veterinarios = [...]

def addVeterinario():
    
    if 
    idV = input('ID  del veterinario: ')
    nameV = input('Nombre del veterinario: ')
    TitulV = input('Titulo del veterinario: ')    
    
    veterinarios.append({
            'id': idV,
            'name': nameV,
            'Titul': TitulV
        })
    print(veterinarios)
    with open('MY PETS/data/veterinarios.json', 'w') as f:
        json.dump(veterinarios, f, indent=3)
    
    input('continuar')
