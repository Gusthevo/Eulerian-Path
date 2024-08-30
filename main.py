import estatisticas

def criar_grafo():
    # Captura a quantidade de vértices
    num_vertices = int(input("Digite a quantidade de vértices do grafo: "))
    
    # Inicializa um dicionário vazio para representar o grafo
    grafo = {}

    # Captura as arestas do grafo
    for i in range(num_vertices):
        vertice = input(f"Digite o vértice {i+1}: ")
        arestas = input(f"Digite a qual(is) vértice(s) o vértice {vertice} está conectado, separadas por espaço: ").split()
        
        # Inicializa lista de adjacências vazia para o vértice se ainda não existir
        if vertice not in grafo:
            grafo[vertice] = []
        
        # Adiciona as arestas bidirecionais
        for aresta in arestas:
            grafo[vertice].append(aresta)
            
            # Garante que também adicionamos a aresta de volta para grafos não direcionados
            if aresta not in grafo:
                grafo[aresta] = []
            if vertice not in grafo[aresta]:
                grafo[aresta].append(vertice)

    return grafo

    # Verifica se o grafo possui caminho euleriano
def possui_caminho_euleriano(grafo):
    # Verifica se o grafo é conexo
    if not e_conexo(grafo):
        print("O grafo não é conexo, verifique e tente novamente.")
        return criar_grafo
    
    # Conta vértices de grau ímpar
    vertices_impares = sum(1 for v in grafo if len(grafo[v]) % 2 != 0)
    
    # Um caminho euleriano requer 0 ou 2 vértices de grau ímpar
    return vertices_impares == 0 or vertices_impares == 2

#Realiza a busca em profundidade com algumas verificações.
def busca_profundidade(grafo, inicio, visitado):
    pilha = [inicio]
    while pilha:
        no = pilha.pop()
        if no not in visitado:
            visitado.add(no)
            pilha.extend(grafo[no])

def e_conexo(grafo):
    if not grafo:
        return True
    
    visitado = set()
    busca_profundidade(grafo, next(iter(grafo)), visitado)
    
    # Verifica se todos os vértices foram visitados
    return len(visitado) == len(grafo)



# Exemplo de uso
print("Criando e iniciando um grafo!")
grafo = criar_grafo()

print("\nVerificando se o grafo possui um caminho euleriano :")
print(possui_caminho_euleriano(grafo))
estatistica = estatisticas

