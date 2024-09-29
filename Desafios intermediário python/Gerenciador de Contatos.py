import csv

# Função para adicionar contato
def adicionar_contato(nome, telefone, email):
    with open('contatos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, telefone, email])

# Função para visualizar contatos
def visualizar_contatos():
    with open('contatos.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'Nome: {row[0]}, Telefone: {row[1]}, Email: {row[2]}')

# Adicionar e visualizar exemplo
adicionar_contato('João Silva', '1234-5678', 'joao@email.com')
visualizar_contatos()
