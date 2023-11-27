#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercicio 1

produtos = []

def inserir_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produto = {"codigo": codigo, "nome": nome, "preco": preco}
    produtos.append(produto)

# Excluir produto
def excluir_produto():
    codigo = input("Digite o código do produto que deseja excluir: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            break

# listar todos os produtos
def listar_produtos():
    produtos.sort(key=lambda x: x['preco'])
    for i, produto in enumerate(produtos):
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']:.2f}")
        if (i + 1) % 10 == 0:
            input("Pressione enter para continuar...")

# Ver o preço de um produto
def consultar_preco():
    codigo = input("Digite o código do produto que deseja consultar: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto é: {produto['preco']:.2f}")
            break

# Função principal
def main():
    while True:
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos com seus respectivos códigos e preços")
        print("4. Consultar o preço de um produto através de seu código.")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            inserir_produto()
        elif opcao == 2:
            excluir_produto()
        elif opcao == 3:
            listar_produtos()
        elif opcao == 4:
            consultar_preco()
        else:
            break

if __name__ == "__main__":
    main()


# In[ ]:




