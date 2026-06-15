from collections import deque
from dataclasses import dataclass


@dataclass
class Notificacion:
    hora: str
    aplicacion: str
    mensaje: str


def eliminar_facebook(cola_notificaciones):
    cola_aux = deque()

    while len(cola_notificaciones) > 0:
        notificacion = cola_notificaciones.popleft()

        if notificacion.aplicacion != "Facebook":
            cola_aux.append(notificacion)

    while len(cola_aux) > 0:
        cola_notificaciones.append(cola_aux.popleft())


def mostrar_twitter_python(cola_notificaciones):
    cola_aux = deque()
    encontradas = []

    while len(cola_notificaciones) > 0:
        notificacion = cola_notificaciones.popleft()

        if notificacion.aplicacion == "Twitter" and "Python" in notificacion.mensaje:
            print(notificacion)
            encontradas.append(notificacion)

        cola_aux.append(notificacion)

    while len(cola_aux) > 0:
        cola_notificaciones.append(cola_aux.popleft())

    return encontradas


def hora_a_minutos(hora):
    horas, minutos = hora.split(":")
    return int(horas) * 60 + int(minutos)


def contar_notificaciones_entre_horas(cola_notificaciones):
    cola_aux = deque()
    pila_temporal = []

    inicio = hora_a_minutos("11:43")
    fin = hora_a_minutos("15:57")

    while len(cola_notificaciones) > 0:
        notificacion = cola_notificaciones.popleft()
        hora_notificacion = hora_a_minutos(notificacion.hora)

        if inicio <= hora_notificacion <= fin:
            pila_temporal.append(notificacion)

        cola_aux.append(notificacion)

    while len(cola_aux) > 0:
        cola_notificaciones.append(cola_aux.popleft())

    return len(pila_temporal)


if __name__ == "__main__":
    cola_notificaciones = deque([
        Notificacion("10:30", "Facebook", "Nuevo comentario"),
        Notificacion("11:50", "Twitter", "Estoy aprendiendo Python"),
        Notificacion("12:15", "Instagram", "Nuevo seguidor"),
        Notificacion("14:20", "Twitter", "Python es muy usado"),
        Notificacion("16:10", "Facebook", "Nueva reacción"),
    ])

    eliminar_facebook(cola_notificaciones)

    mostrar_twitter_python(cola_notificaciones)

    cantidad = contar_notificaciones_entre_horas(cola_notificaciones)
    print(cantidad)
