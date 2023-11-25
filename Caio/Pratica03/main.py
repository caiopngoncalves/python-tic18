def inserir_produto(produtos):
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto (começando com letra maiúscula): ")
    preco = float(input("Digite o preço do produto (com duas casas decimais): "))
    preco_formatado = f"{preco:.2f}"

    produtos.append({"codigo": codigo, "nome": nome, "preco": preco_formatado})
    print("Produto inserido com sucesso!")

def excluir_produto(produtos):
    codigo = input("Digite o código do produto a ser excluído: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return

    print("Produto não encontrado.")

def listar_produtos(produtos):
    print("Lista de Produtos:")
    for produto in produtos:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}")

def consultar_preco(produtos):
    codigo = input("Digite o código do produto para consultar o preço: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto {produto['nome']} é: {produto['preco']}")
            return

    print("Produto não encontrado.")

def main():
    produtos = []

    while True:
        print("\nMenu de Opções:")
        print("1. Inserir Produto")
        print("2. Excluir Produto")
        print("3. Listar Produtos")
        print("4. Consultar Preço")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            inserir_produto(produtos)
        elif escolha == "2":
            excluir_produto(produtos)
        elif escolha == "3":
            listar_produtos(produtos)
        elif escolha == "4":
            consultar_preco(produtos)
        elif escolha == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()