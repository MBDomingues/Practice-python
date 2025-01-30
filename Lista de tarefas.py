# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Função para visualizar todas as tarefas
def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

# Função para remover uma tarefa
def remover_tarefa():
    ver_tarefas()
    try:
        num_tarefa = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= num_tarefa < len(tarefas):
            tarefa_removida = tarefas.pop(num_tarefa)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Menu principal
def menu():
    while True:
        print("\n--- Lista de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Ver Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            ver_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    menu()