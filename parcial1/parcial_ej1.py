from list_ import List

from super_heroes_data import superheroes

superheroes = [
    "Iron Man",
    "Hulk",
    "Thor",
    "Black Widow",
    "Hawkeye",
    "Spiderman",
    "Doctor Strange",
    "Capitan America",
    "Black Panther",
    "Wolverine",
    "Deadpool",
    "Scarlet Witch",
    "Vision",
    "Ant Man",
    "Falcon"
]


def buscar_capitan_america(lista, posicion=0):
    if posicion == len(lista):
        return False

    if lista[posicion].lower() == "capitan america":
        return True

    return buscar_capitan_america(lista, posicion + 1)


def listar_superheroes(lista, posicion=0):
    if posicion == len(lista):
        return

    print(lista[posicion])
    listar_superheroes(lista, posicion + 1)


print("Lista de superheroes:")
listar_superheroes(superheroes)

if buscar_capitan_america(superheroes):
    print("Capitan America esta en la lista")
else:
    print("Capitan America no esta en la lista")
