import math

class Entero:
    def __init__(self, numero: int):
        self.__numero = numero

    def get_numero(self) -> int:
        return self.__numero

    def set_numero(self, numero: int):
        self.__numero = numero

    def cuadrado(self) -> int:
        """Calcula el cuadrado del número"""
        return self.__numero * self.__numero

    def es_par(self) -> bool:
        """Retorna True si el número es par"""
        return self.__numero % 2 == 0

    def es_impar(self) -> bool:
        """Retorna True si el número es impar"""
        return self.__numero % 2 != 0

    def factorial(self) -> int:
        """Calcula el factorial del número (retorna -1 si es negativo)"""
        if self.__numero < 0:
            return -1
        resultado = 1
        for i in range(2, self.__numero + 1):
            resultado *= i
        return resultado

    def es_primo(self) -> bool:
        """Retorna True si el número es primo"""
        if self.__numero < 2:
            return False
        for i in range(2, int(math.sqrt(self.__numero)) + 1):
            if self.__numero % i == 0:
                return False
        return True