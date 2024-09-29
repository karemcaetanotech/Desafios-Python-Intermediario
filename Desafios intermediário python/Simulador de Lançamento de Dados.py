import random
import matplotlib.pyplot as plt

# Simular lançamentos de dados
resultados = [random.randint(1, 6) for _ in range(1000)]

# Plotar histograma
plt.hist(resultados, bins=6, edgecolor='black')
plt.title('Distribuição dos Lançamentos de Dados')
plt.xlabel('Resultado')
plt.ylabel('Frequência')
plt.show()

#como rodar: python simulador_dados.py
