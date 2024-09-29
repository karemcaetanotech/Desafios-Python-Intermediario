tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada.")

def remover_tarefa(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' removida.")
    else:
        print(f"Tarefa '{tarefa}' não encontrada.")

def listar_tarefas():
    if tarefas:
        print("Suas tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa na lista.")

while True:
    print("\n1. Adicionar Tarefa\n2. Remover Tarefa\n3. Listar Tarefas\n4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa

#como rodar: python jogo_da_velha.py
