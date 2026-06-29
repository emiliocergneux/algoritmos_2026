from list_ import List
from stack import Stack
from queue_ import Queue
from super_heroes_data import superheroes


def by_name(h):        
    return h["name"].lower()
def by_real_name(h):    
    return (h["real_name"] or "").lower()
def by_appearance(h):   
    return h["first_appearance"]


def listar_por_nombre(superheroes):
    lista = List()
    for heroe in superheroes:
        lista.append(heroe)
    lista.add_criterion("name", by_name)
    lista.sort_by_criterion("name")
    return lista

print("PERSONAJES ORDENADOS POR NOMBRE")
lista_nombres = listar_por_nombre(superheroes)
for h in lista_nombres:
    print(h["name"])


def encontrar_posicion(lista, nombre):
    lista.add_criterion("name", by_name)
    return lista.search(nombre.lower(), "name")

print("POSICIÓN DE THE THING Y ROCKET RACCOON")
pos_thing  = encontrar_posicion(lista_nombres, "The Thing")
pos_rocket = encontrar_posicion(lista_nombres, "Rocket Raccoon")
print(f"The Thing está en la posición: {pos_thing}")
print(f"Rocket Raccoon está en la posición: {pos_rocket}")


def listar_villanos(superheroes):
    lista = List()
    lista.add_criterion("name", by_name)
    for heroe in superheroes:
        if heroe["is_villain"]:
            lista.append(heroe)
    lista.sort_by_criterion("name")
    return lista

print("LISTA DE VILLANOS")
lista_villanos = listar_villanos(superheroes)
for v in lista_villanos:
    print(v["name"])


def villanos_en_cola(superheroes):
    cola = Queue()
    for heroe in superheroes:
        if heroe["is_villain"]:
            cola.arrive(heroe)

    print("VILLANOS QUE APARECIERON ANTES DE 1980")

    total = cola.size()
    for _ in range(total):
        villano = cola.attention()
        if villano["first_appearance"] < 1980:
            print(f"{villano['name']} - {villano['first_appearance']}")
        cola.arrive(villano) 

    return cola

cola_villanos = villanos_en_cola(superheroes)


def listar_por_inicial(superheroes, iniciales):
    lista = List()
    lista.add_criterion("name", by_name)
    for heroe in superheroes:
        nombre = heroe["name"]
        for inicial in iniciales:
            if nombre.startswith(inicial):
                lista.append(heroe)
                break
    lista.sort_by_criterion("name")
    return lista

print("SUPERHÉROES QUE COMIENZAN CON Bl, G, My, W")
iniciales = ["Bl", "G", "My", "W"]
lista_iniciales = listar_por_inicial(superheroes, iniciales)
for h in lista_iniciales:
    print(h["name"])


def listar_por_nombre_real(superheroes):
    lista = List()
    lista.add_criterion("real_name", by_real_name)
    for heroe in superheroes:
        lista.append(heroe)
    lista.sort_by_criterion("real_name")
    return lista

print("PERSONAJES ORDENADOS POR NOMBRE REAL")
lista_real = listar_por_nombre_real(superheroes)
for h in lista_real:
    print(f"{h['real_name'] or 'Desconocido'} -> {h['name']}")


def listar_por_anio(superheroes):
    pila = Stack()
    ordenados = sorted(superheroes, key=by_appearance, reverse=True)
    for heroe in ordenados:
        pila.push(heroe)
    return pila

print("SUPERHÉROES ORDENADOS POR FECHA DE APARICIÓN")
pila_anios = listar_por_anio(superheroes)
total_pila = pila_anios.size()
for _ in range(total_pila):
    h = pila_anios.pop()
    print(f"{h['first_appearance']} - {h['name']}")


def modificar_nombre_real(superheroes, nombre_buscar, nuevo_nombre):
    for heroe in superheroes:
        if heroe["name"].lower() == nombre_buscar.lower():
            heroe["real_name"] = nuevo_nombre
            print(f"MODIFICACIÓN REALIZADA")
            print(f"Se modificó {nombre_buscar} a: {nuevo_nombre}")
            return True
    print(f"ERROR")
    print(f"No se encontró a {nombre_buscar}")
    return False

modificar_nombre_real(superheroes, "Ant Man", "Scott Lang")

print("Verificando cambio:")
for heroe in superheroes:
    if heroe["name"] == "Ant Man":
        print(f"Ant Man ahora es: {heroe['real_name']}")


def buscar_en_biografia(superheroes, palabras):
    lista = List()
    lista.add_criterion("name", by_name)
    for heroe in superheroes:
        bio = heroe["short_bio"].lower()
        for palabra in palabras:
            if palabra.lower() in bio:
                lista.append(heroe)
                break
    lista.sort_by_criterion("name")
    return lista

print("PERSONAJES CON 'time-traveling' O 'suit' EN BIOGRAFÍA")
palabras_buscar = ["time-traveling", "suit"]
lista_bio = buscar_en_biografia(superheroes, palabras_buscar)
for h in lista_bio:
    print(h["name"])


def eliminar_personajes(superheroes, nombres_a_eliminar):
    eliminados = []
    i = 0
    while i < len(superheroes):
        if superheroes[i]["name"] in nombres_a_eliminar:
            eliminados.append(superheroes.pop(i))
        else:
            i += 1
    return eliminados

print("ELIMINACIÓN DE ELECTRO Y BARON ZEMO")
nombres_eliminar = ["Electro", "Baron Zemo"]
eliminados = eliminar_personajes(superheroes, nombres_eliminar)

if eliminados:
    print("Personajes eliminados:")
    for personaje in eliminados:
        print(f"Nombre: {personaje['name']}")
        print(f"Alias: {personaje['alias']}")
        print(f"Nombre real: {personaje['real_name']}")
        print(f"Biografía: {personaje['short_bio']}")
        print(f"Primera aparición: {personaje['first_appearance']}")
        print(f"Es villano: {personaje['is_villain']}")
        print("-" * 50)
else:
    print("No se encontraron los personajes a eliminar")


def verificar_estructuras():
    print("VERIFICACIÓN FINAL")
    print(f"Total de personajes restantes: {len(superheroes)}")
    print(f"Cantidad de villanos en cola: {cola_villanos.size()}")
    print(f"Cantidad de villanos listados: {lista_villanos.size()}")

verificar_estructuras()