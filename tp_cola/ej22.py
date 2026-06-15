from collections import deque
from dataclasses import dataclass


@dataclass
class PersonajeMCU:
    nombre_personaje: str
    nombre_superheroe: str
    genero: str


def buscar_personaje_capitana_marvel(cola_personajes):
    cola_aux = deque()
    resultado = None

    while len(cola_personajes) > 0:
        personaje = cola_personajes.popleft()

        if personaje.nombre_superheroe == "Capitana Marvel":
            resultado = personaje.nombre_personaje

        cola_aux.append(personaje)

    while len(cola_aux) > 0:
        cola_personajes.append(cola_aux.popleft())

    return resultado


def mostrar_superheroes_femeninos(cola_personajes):
    cola_aux = deque()
    superheroes = []

    while len(cola_personajes) > 0:
        personaje = cola_personajes.popleft()

        if personaje.genero == "F":
            print(personaje.nombre_superheroe)
            superheroes.append(personaje.nombre_superheroe)

        cola_aux.append(personaje)

    while len(cola_aux) > 0:
        cola_personajes.append(cola_aux.popleft())

    return superheroes


def mostrar_personajes_masculinos(cola_personajes):
    cola_aux = deque()
    personajes = []

    while len(cola_personajes) > 0:
        personaje = cola_personajes.popleft()

        if personaje.genero == "M":
            print(personaje.nombre_personaje)
            personajes.append(personaje.nombre_personaje)

        cola_aux.append(personaje)

    while len(cola_aux) > 0:
        cola_personajes.append(cola_aux.popleft())

    return personajes


def buscar_superheroe_scott_lang(cola_personajes):
    cola_aux = deque()
    resultado = None

    while len(cola_personajes) > 0:
        personaje = cola_personajes.popleft()

        if personaje.nombre_personaje == "Scott Lang":
            resultado = personaje.nombre_superheroe

        cola_aux.append(personaje)

    while len(cola_aux) > 0:
        cola_personajes.append(cola_aux.popleft())

    return resultado


def mostrar_datos_con_letra_s(cola_personajes):
    cola_aux = deque()
    encontrados = []

    while len(cola_personajes) > 0:
        personaje = cola_personajes.popleft()

        if personaje.nombre_personaje.startswith("S") or personaje.nombre_superheroe.startswith("S"):
            print(personaje)
            encontrados.append(personaje)

        cola_aux.append(personaje)

    while len(cola_aux) > 0:
        cola_personajes.append(cola_aux.popleft())

    return encontrados


def buscar_carol_danvers(cola_personajes):
    cola_aux = deque()
    resultado = None

    while len(cola_personajes) > 0:
        personaje = cola_personajes.popleft()

        if personaje.nombre_personaje == "Carol Danvers":
            resultado = personaje.nombre_superheroe

        cola_aux.append(personaje)

    while len(cola_aux) > 0:
        cola_personajes.append(cola_aux.popleft())

    return resultado


if __name__ == "__main__":
    cola_personajes = deque([
        PersonajeMCU("Tony Stark", "Iron Man", "M"),
        PersonajeMCU("Steve Rogers", "Capitán América", "M"),
        PersonajeMCU("Natasha Romanoff", "Black Widow", "F"),
        PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"),
        PersonajeMCU("Scott Lang", "Ant-Man", "M"),
        PersonajeMCU("Stephen Strange", "Doctor Strange", "M"),
        PersonajeMCU("Wanda Maximoff", "Scarlet Witch", "F"),
    ])

    print(buscar_personaje_capitana_marvel(cola_personajes))

    mostrar_superheroes_femeninos(cola_personajes)

    mostrar_personajes_masculinos(cola_personajes)

    print(buscar_superheroe_scott_lang(cola_personajes))

    mostrar_datos_con_letra_s(cola_personajes)

    superheroe = buscar_carol_danvers(cola_personajes)

    if superheroe is not None:
        print("Carol Danvers se encuentra en la cola")
        print(superheroe)
    else:
        print("Carol Danvers no se encuentra en la cola")
