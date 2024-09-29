import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Criar a tabela de tarefas
c.execute('''CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, tarefa TEXT, status TEXT)''')
conn.commit()

# Função para adicionar tarefa
def adicionar_tarefa(tarefa):
    c.execute("INSERT INTO tarefas (tarefa, status) VALUES (?, 'pendente')", (tarefa,))
    conn.commit()

# Função para visualizar tarefas
def visualizar_tarefas():
    c.execute("SELECT * FROM tarefas")
    return c.fetchall()

# Adicionar e visualizar exemplo
adicionar_tarefa('Estudar Python')
print(visualizar_tarefas())

#como rodar: python todo_list.py
