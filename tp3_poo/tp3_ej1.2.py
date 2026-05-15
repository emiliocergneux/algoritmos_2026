import math

class Entero:
    def __init__(self, numero: int):
        self.__numero = numero

    def get_numero(self) -> int:
        return self.__numero

    def set_numero(self, numero: int):
        self.__numero = numero

    def cuadrado(self) -> int:
        return self.__numero * self.__numero

    def es_par(self) -> bool:
        return self.__numero % 2 == 0

    def es_impar(self) -> bool:
        return self.__numero % 2 != 0

    def factorial(self) -> int:
        if self.__numero < 0:
            return -1
        resultado = 1
        for i in range(2, self.__numero + 1):
            resultado *= i
        return resultado

    def es_primo(self) -> bool:
        if self.__numero < 2:
            return False
        for i in range(2, int(math.sqrt(self.__numero)) + 1):
            if self.__numero % i == 0:
                return False
        return True


def main():
    numero = int(input("Ingrese un número entero: "))
    entero = Entero(numero)

    print(f"=== Resultados para el número: {entero.get_numero()} ===")
    print(f"Cuadrado: {entero.cuadrado()}")

    if entero.es_par():
        print("El número ES par.")
    else:
        print("El número NO es par.")

    if entero.es_impar():
        print("El número ES impar.")
    else:
        print("El número NO es impar.")

    resultado_factorial = entero.factorial()
    if resultado_factorial == -1:
        print("Factorial: No se puede calcular (número negativo).")
    else:
        print(f"Factorial: {resultado_factorial}")

    if entero.es_primo():
        print("El número ES primo.")
    else:
        print("El número NO es primo.")


if __name__ == "__main__":
    main()