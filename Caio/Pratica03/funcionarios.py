def reajusta_dez_porcento(empregados):
    for empregado in empregados:
        salario_atual = empregado["salario"]
        novo_salario = salario_atual * 1.1  # Reajuste de 10%
        empregado["salario"] = round(novo_salario, 2)

def ler_arquivo_empregados(nome_arquivo):
    empregados = []

    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(",")
                empregado = {
                    "nome": dados[0],
                    "sobrenome": dados[1],
                    "ano_nascimento": int(dados[2]),
                    "RG": dados[3],
                    "ano_admissao": int(dados[4]),
                    "salario": float(dados[5])
                }
                empregados.append(empregado)
        return empregados
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

def main():
    nome_arquivo = "empregados.txt"
    
    empregados = ler_arquivo_empregados(nome_arquivo)

    print("Antes do reajuste:")
    for empregado in empregados:
        print(empregado)

    reajusta_dez_porcento(empregados)

    print("\nDepois do reajuste:")
    for empregado in empregados:
        print(empregado)

if __name__ == "__main__":
    main()
