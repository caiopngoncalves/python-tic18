from abc import ABC, abstractmethod
from datetime import date

class Data:
    def _init_(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano

    def _str_(self):
        return "{}/{}/{}".format(self._dia, self.mes, self._ano)

    def _eq_(self, outraData):
        return self._dia == outraData._dia and \
               self._mes == outraData._mes and \
               self._ano == outraData._ano

    def _lt_(self, outraData):
        if self._ano < outraData._ano:
            return True
        elif self._ano == outraData._ano:
            if self._mes < outraData._mes:
                return True
            elif self._mes == outraData._mes:
                return self._dia < outraData._dia
        return False

    def _gt_(self, outraData):
        if self._ano > outraData._ano:
            return True
        elif self._ano == outraData._ano:
            if self._mes > outraData._mes:
                return True
            elif self._mes == outraData._mes:
                return self._dia > outraData._dia
        return False


class AnaliseDados(ABC):
    @abstractmethod
    def _init_(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

    @abstractmethod
    def iteradorZip(self, outra_lista):
        pass

    @abstractmethod
    def iteradorMap(self):
        pass

    @abstractmethod
    def iteradorFilter(self):
        pass

    @abstractmethod
    def _str_(self):
        pass


class ListaNomes(AnaliseDados):
    # ... (código da classe ListaNomes fornecido)

    def iteradorZip(self, outra_lista):
        return zip(self.__lista, outra_lista)

    def iteradorMap(self):
        return map(lambda x: x.upper(), self.__lista)

    def iteradorFilter(self):
        return filter(lambda nome: len(nome) > 5, self.__lista)


class ListaDatas(AnaliseDados):
    # ... (código da classe ListaDatas fornecido)

    def iteradorZip(self, outra_lista):
        return zip(self.__lista, outra_lista)

    def iteradorMap(self):
        return map(lambda data: date(data.year, data.month, 1), self.__lista)

    def iteradorFilter(self):
        return filter(lambda data: data.year < 2019, self.__lista)


class ListaSalarios(AnaliseDados):
    # ... (código da classe ListaSalarios fornecido)

    def iteradorZip(self, outra_lista):
        return zip(self.__lista, outra_lista)

    def iteradorMap(self):
        return map(lambda salario: salario * 1.1, self.__lista)

    def iteradorFilter(self):
        return filter(lambda salario: salario > 5000, self.__lista)


class ListaIdades(AnaliseDados):
    # ... (código da classe ListaIdades fornecido)

    def iteradorZip(self, outra_lista):
        return zip(self.__lista, outra_lista)

    def iteradorMap(self):
        return map(lambda idade: idade + 1, self.__lista)

    def iteradorFilter(self):
        return filter(lambda idade: idade < 30, self.__lista)


def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        lista.listarEmOrdem()
        print("_______")

        # Demonstração de iteradores
        print("\nIterador zip:")
        outra_lista = ["A", "B", "C"]
        for item in lista.iteradorZip(outra_lista):
            print(item)

        print("\nIterador map:")
        for item in lista.iteradorMap():
            print(item)

        print("\nIterador filter:")
        for item in lista.iteradorFilter():
            print(item)

        print("_______")

    print("\nFim do teste!!!")


if _name_ == "_main_":
    main()