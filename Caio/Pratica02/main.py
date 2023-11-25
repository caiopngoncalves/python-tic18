import os

ARQUIVO_TAREFAS = "tarefas.txt"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r") as arquivo:
            return [linha.strip() for linha in arquivo.readlines()]
    else:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        arquivo.write("\n".join(tarefas))

def listar_tarefas(tarefas):
    print("Lista de Tarefas:")
    for idx, tarefa in enumerate(tarefas, start=1):
        print(f"Id: {idx} - {tarefa}")

def registrar_tarefa(tarefas, descricao):
    nova_tarefa = f"{len(tarefas) + 1}.{descricao} [ ]"
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa registrada!!!")

def marcar_como_realizada(tarefas, identificador):
    if 1 <= identificador <= len(tarefas):
        tarefa = tarefas.pop(identificador - 1)
        tarefas.insert(0, tarefa.replace("[ ]", "[x]"))
        salvar_tarefas(tarefas)
        print("Tarefa realizada marcada com sucesso!")
    else:
        print("Tarefa não encontrada ou já realizada.")

def editar_tarefa(tarefas, identificador, nova_descricao):
    if 1 <= identificador <= len(tarefas):
        tarefas[identificador - 1] = f"{identificador}.{nova_descricao} {tarefas[identificador - 1][-4:]}"
        salvar_tarefas(tarefas)
        print("Tarefa editada com sucesso!")
    else:
        print("Tarefa não encontrada.")

tarefas = carregar_tarefas()

while True:
    print("\nOpções:")
    print("1. Listar Tarefas")
    print("2. Registrar Nova Tarefa")
    print("3. Marcar Tarefa como Realizada")
    print("4. Editar Tarefa")
    print("5. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        listar_tarefas(tarefas)
    elif escolha == "2":
        descricao = input("Digite a descrição da nova tarefa: ").capitalize()
        registrar_tarefa(tarefas, descricao)
    elif escolha == "3":
        listar_tarefas(tarefas)
        identificador = int(input("Digite o ID da tarefa a ser marcada como realizada: "))
        marcar_como_realizada(tarefas, identificador)
    elif escolha == "4":
        listar_tarefas(tarefas)
        identificador = int(input("Digite o ID da tarefa a ser editada: "))
        nova_descricao = input("Digite a nova descrição da tarefa: ").capitalize()
        editar_tarefa(tarefas, identificador, nova_descricao)
    elif escolha == "5":
        print("Saindo do aplicativo ToDoList. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")