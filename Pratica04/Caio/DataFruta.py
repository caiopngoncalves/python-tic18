from abc import ABC, abstractmethod
from datetime import date

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
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

    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return self.__dia == outraData.__dia and \
               self.__mes == outraData.__mes and \
               self.__ano == outraData.__ano

    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia < outraData.__dia
        return False

    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia > outraData.__dia
        return False


class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
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
    def __str__(self):
        pass


class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []

    def entradaDeDados(self):
        num_elementos = int(input("Quantos nomes deseja inserir? "))
        for _ in range(num_elementos):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        mediana_index = len(sorted_lista) // 2
        print("Mediana:", sorted_lista[mediana_index])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        for nome in sorted(self.__lista):
            print(nome)

    def iteradorZip(self, outra_lista):
        return zip(self.__lista, outra_lista)

    def iteradorMap(self):
        return map(lambda x: x.upper(), self.__lista)

    def iteradorFilter(self):
        return filter(lambda nome: len(nome) > 5, self.__lista)

    def __str__(self):
        return ', '.join(self.__lista)


class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []

    def entradaDeDados(self):
        num_elementos = int(input("Quantas datas deseja inserir? "))
        for _ in range(num_elementos):
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))
            data = Data(dia, mes, ano)
            self.__lista.append(data)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        mediana_index = len(sorted_lista) // 2
        print("Mediana:", sorted_lista[mediana_index])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        for data in sorted(self.__lista):
            print(data)

    def iteradorZip(self, outra_lista):
        return zip(self.__lista, outra_lista)

    def iteradorMap(self):
        return map(lambda data: date(data.year, data.month, 1), self.__lista)

    def iteradorFilter(self):
        return filter(lambda data: data.year < 2019, self.__lista)

    def __str__(self):
        return ', '.join(str(data) for data in self.__lista)


class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(type(float))
        self.__lista = []

    def entradaDeDados(self):
        num_elementos = int(input("Quantos salários deseja inserir? "))
        for _ in range(num_elementos):
            salario = float(input("Digite um salário: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        mediana_index = len(sorted_lista) // 2
        print("Mediana:", sorted_lista[mediana_index])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        for salario in sorted(self.__lista):
            print(salario)

    def iteradorZip(self, outra_lista):
        return zip(self.__lista, outra_lista)

    def iteradorMap(self):
        return map(lambda salario: salario * 1.1, self.__lista)

    def iteradorFilter(self):
        return filter(lambda salario: salario > 5000, self.__lista)

    def __str__(self):
        return ', '.join(map(str, self.__lista))


class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []

    def entradaDeDados(self):
        num_elementos = int(input("Quantas idades deseja inserir? "))
        for _ in range(num_elementos):
            idade = int(input("Digite uma idade: "))
            self.__lista.append(idade)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        mediana_index = len(sorted_lista) // 2
        print("Mediana:", sorted_lista[mediana_index])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        for idade in sorted(self.__lista):
            print(idade)

    def iteradorZip(self, outra_lista):
        return zip(self.__lista, outra_lista)

    def iteradorMap(self):
        return map(lambda idade: idade + 1, self.__lista)

    def iteradorFilter(self):
        return filter(lambda idade: idade < 30, self.__lista)

    def __str__(self):
        return ', '.join(map(str, self.__lista))


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
        print("___________________")

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

        print("___________________")

    print("\nFim do teste!!!")


if __name__ == "__main__":
    main()
