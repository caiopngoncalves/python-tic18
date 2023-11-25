import sys

a = 10
b = 3

# Adição
soma = a + b 

# Subtração
subtracao = a - b 

# Multiplicação
multiplicacao = a * b

# Divisão (retorna um número de ponto flutuante)
divisao = a / b  

# Divisão inteira
divisao_inteira = a // b 

# Resto da divisão
resto_divisao = a % b  

# Potência
potencia = a ** b  

a = 10
b = 3

# Adição
a += b 

# Subtração
a -= b 

# Multiplicação
a *= b

# Divisão
a /= b 

# Divisão inteira
a //= b 

# Resto da divisão
a %= b 

# Potência
a **= b 

# Fatorial de 30
fatorial_30 = 1
for i in range(1, 31):
    fatorial_30 *= i

print("Fatorial de 30 em Python:", fatorial_30)

maior_valor_int_C_CPP = 2**31 - 1

print("Maior valor inteiro em C/C++ (signed int):", maior_valor_int_C_CPP)

# Atribuição de valor a uma variável
num = 5
novo_num = num + 3

print("Original:", num)
print("Novo:", novo_num)

# Atribuição de valor a uma variável
num = 5
soma = num + 3

print("Original:", num)
print("Soma:", soma)

# Imprime o caractere e seu código numérico
for i in range(10):
    print(f"'{chr(ord('0') + i)}' - {ord('0') + i}")
    
# Imprime o caractere e seus códigos numéricos em decimal, octal e hexadecimal
for i in range(10):
   
    char = chr(ord('0') + i)
    decimal_code = ord(char)
    octal_code = oct(decimal_code)
    hexadecimal_code = hex(decimal_code)

    
    print(f"'{char}' - Decimal: {decimal_code}, Octal: {octal_code}, Hexadecimal: {hexadecimal_code}")
 
 
# Solicita e imprime o caractere e seus códigos numéricos em decimal, octal e hexadecimal   
caractere = input("Digite um caractere: ")

decimal_code = ord(caractere)
octal_code = oct(decimal_code)
hexadecimal_code = hex(decimal_code)

print(f"'{caractere}' - Decimal: {decimal_code}, Octal: {octal_code}, Hexadecimal: {hexadecimal_code}")

# Em Python, os caracteres especiais, como 'ç' e 'ã', são tratados como caracteres Unicode. 
# Python suporta Unicode, o que permite representar uma ampla variedade de caracteres, 
# incluindo caracteres acentuados, especiais e de outros idiomas.


# Exercício 4: Manipulação de variáveis de tipo string e explorando os métodos da classe.
nome_completo = "João da Silva"

espaco_separador = nome_completo.find(' ')
nome = nome_completo[:espaco_separador]
sobrenome = nome_completo[espaco_separador + 1:]

ordem_alfabetica = sorted([nome, sobrenome])

tamanho_nome = len(nome)
tamanho_sobrenome = len(sobrenome)

e_palindromo = nome == nome[::-1]

print("Nome Completo:", nome_completo)
print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Ordem Alfabética:", ordem_alfabetica)
print("Quantidade de Caracteres (Nome):", tamanho_nome)
print("Quantidade de Caracteres (Sobrenome):", tamanho_sobrenome)
print("É Palíndromo:", e_palindromo)

# Operadores Aritméticos
a = 5.0
b = 2.0

soma = a + b       # Soma
subtracao = a - b  # Subtração
multiplicacao = a * b  # Multiplicação
divisao = a / b    # Divisão
resto_divisao = a % b  # Resto da divisão
potencia = a ** b  # Potência

# Operadores Aritméticos Compostos
a += b  # Adição
a -= b  # Subtração
a *= b  # Multiplicação
a /= b  # Divisão
a **= b  # Potência

maior_potencia_de_2 = sys.float_info.max_exp
menor_potencia_de_2 = sys.float_info.min_exp

print("Maior Potência de 2:", maior_potencia_de_2)
print("Menor Potência de 2:", menor_potencia_de_2)

num = 3.14

print("Número Original:", num)
print("Parte Inteira:", num.__int__())
print("Arredondado:", num.__round__(2))
print("Transformado em String:", num.__str__())