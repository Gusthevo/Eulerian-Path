import teste
#import main
import time
import seaborn as sns
import matplotlib.pyplot as plt


def medir_tempo_execucao(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return fim - inicio, resultado

tempos_execucao = []
for i in range(1000):
    tempo, resultado = medir_tempo_execucao(teste.possui_caminho_euleriano, teste.grafo_predefinido)
    tempos_execucao.append(tempo)
    
    print(f"Análise {i+1} realizada.")

# Mostrar o gráfico dos tempos de execução
plt.figure(figsize=(15, 10))
sns.scatterplot(x=range(1, 1001), y=tempos_execucao)
plt.xlabel('Execução')
plt.ylabel('Tempo (segundos)')
plt.title('Tempo de Execução da Verificação de Caminho Euleriano')
plt.show()