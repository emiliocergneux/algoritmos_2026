from abc import ABC, abstractmethod


class ICalculable(ABC):

    @abstractmethod
    def calcular_costo(self, peso):
        pass


class IRastreable(ABC):

    @abstractmethod
    def rastrear_paquete_satelital(self):
        pass


class IExportable(ABC):

    @abstractmethod
    def generar_reporte_aduana(self):
        pass

class CorreoLocalOCA(ICalculable):

    def calcular_costo(self, peso):
        return peso * 15.0