import random

# Inicialização da população
def inicializar_populacao(tamanho_populacao, tamanho_caminho):
    return [[random.choice(['U', 'D', 'L', 'R']) for _ in range(tamanho_caminho)] for _ in range(tamanho_populacao)]

def calcular_aptidao(individuo, inicio, fim):
    x, y = inicio
    n = len(mapa)
    
    for movimento in individuo:
        x_new, y_new = x, y  # Inicializar x_new e y_new para a posição atual
        if movimento == 'U': x_new = x - 1
        elif movimento == 'D': x_new = x + 1
        elif movimento == 'L': y_new = y - 1
        elif movimento == 'R': y_new = y + 1
        
        # Se o movimento é válido, atualize a posição
        if 0 <= x_new < n and 0 <= y_new < n and mapa[x_new][y_new] != "#":
            x, y = x_new, y_new
            
    # Calcular a distância de Manhattan até o objetivo
    aptidao = abs(fim[0] - x) + abs(fim[1] - y)
    
    return aptidao

def selecionar_por_torneio(populacao, aptidoes, tamanho_torneio):
    # Seleciona 'tamanho_torneio' indivíduos aleatoriamente da população
    competidores = random.sample(list(zip(populacao, aptidoes)), tamanho_torneio)
    
    # Retorna o indivíduo com a melhor (menor) aptidão
    return min(competidores, key=lambda x: x[1])[0]

def cruzar(individuo1, individuo2):
    corte = random.randint(0, len(individuo1))
    filho1 = individuo1[:corte] + individuo2[corte:]
    filho2 = individuo2[:corte] + individuo1[corte:]
    return filho1, filho2

# Mutação
def mutar(individuo, tx_mut):
    for i in range(len(individuo)):
        if random.random() < tx_mut:  # Probabilidade de mutação
            individuo[i] = random.choice(['U', 'D', 'L', 'R'])

def exibir_mapa_final(mapa, caminho=None, inicio=None, fim=None):
    mapa_copia = [linha.copy() for linha in mapa]
    n = len(mapa_copia)
    
    if caminho:
        x, y = inicio
        for movimento in caminho:
            x_new, y_new = x, y
            if movimento == 'U': x_new -= 1
            elif movimento == 'D': x_new += 1
            elif movimento == 'L': y_new -= 1
            elif movimento == 'R': y_new += 1
            
            # Se o movimento é válido, atualize a posição
            if 0 <= x_new < n and 0 <= y_new < n and mapa_copia[x_new][y_new] != "#":
                x, y = x_new, y_new
                mapa_copia[x][y] = "🟨"
                ultimo_validoX = x
                ultimo_validoY = y
        mapa_copia[ultimo_validoX][ultimo_validoY] = "🚹"
    for i, linha in enumerate(mapa_copia):
        for j, celula in enumerate(linha):
            if (i, j) == inicio:
                print("🟨", end="")
            elif (i, j) == fim:
                if (x, y) == fim:  # Se o último movimento terminou na posição de fim
                    print("🚹", end="")
                else:
                    print("🎯", end="")
            elif celula == "-":
                print("⬜", end="")
            elif celula == "#":
                print("⬛", end="")
            elif celula == "🟨":
                print("🟨", end="")
            elif celula == "🚹":
                print("🚹", end="")
        print()
    print()
    print(caminho)
    
# Exibir o mapa
def exibir_mapa(mapa, caminho=None, inicio=None, fim=None):
    mapa_copia = [linha.copy() for linha in mapa]
    if caminho:
        x, y = inicio
        for movimento in caminho:
            if movimento == 'U': x -= 1
            elif movimento == 'D': x += 1
            elif movimento == 'L': y -= 1
            elif movimento == 'R': y += 1
            
            if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa_copia[x][y] == "-":
                mapa_copia[x][y] = "🟨"
                
    for i in range(len(mapa_copia)):
        for j in range(len(mapa_copia[0])):
            if mapa_copia[i][j] == "-":
                mapa_copia[i][j] = "⬜"
            elif mapa_copia[i][j] == "#":
                mapa_copia[i][j] = "⬛"
            elif mapa_copia[i][j] == "O":
                mapa_copia[i][j] = "🚹"
            elif mapa_copia[i][j] == "X":
                mapa_copia[i][j] = "🎯"
                
    for linha in mapa_copia:
        print("".join(linha))
    print()
    
#=====================================
#Representação do mapa
#   
#tam_pop = 20
#tam_caminho = 10
#torneio = 4
#tx_mut = 0.01
#max_geracoes = 100
#inicio = (3, 0)
#fim = (0, 3)
#mapa = [
#    ["-", "-", "-", "X"],
#    ["#", "#", "-", "#"],
#    ["-", "#", "-", "-"],
#    ["O", "-", "-", "-"],
#]


#tam_pop = 10
#tam_caminho = 20
#torneio = 4
#tx_mut = 0.01
#max_geracoes = 100
#inicio = (6, 0)
#fim = (0, 6)
#mapa = [
#   ["-", "-", "-", "-", "-", "#", "X"],
#   ["-", "-", "-", "-", "-", "#", "-"],
#   ["-", "-", "#", "#", "-", "#", "-"],
#   ["-", "-", "-", "#", "-", "#", "-"],
#   ["-", "-", "-", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-", "-"],
#   ["O", "-", "-", "#", "-", "-", "-"]
#]


tam_pop = 20
tam_caminho = 50
torneio = 4
tx_mut = 0.01
max_geracoes = 200
inicio = (14, 0)
fim = (0, 14)
mapa = [
   ["-", "-", "-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-", "#", "X"],
   ["-", "-", "-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-", "#", "-"],
   ["-", "-", "#", "#", "-", "#", "-", "-", "-", "#", "-", "-", "-", "#", "-"],
   ["-", "-", "-", "#", "-", "#", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
   ["-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-"],
   ["-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-"],
   ["-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-"],
   ["-", "-", "-", "-", "-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-"],
   ["-", "-", "-", "-", "-", "#", "-", "-", "-", "#", "#", "#", "-", "#", "#"],
   ["-", "-", "-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-", "-", "-"],
   ["-", "-", "-", "-", "-", "#", "-", "-", "-", "#", "-", "-", "-", "-", "-"],
   ["-", "-", "-", "#", "-", "-", "-", "-", "-", "#", "-", "-", "-", "-", "-"],
   ["-", "-", "-", "#", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
   ["-", "-", "-", "#", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
   ["O", "-", "-", "#", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]



# Inicializa a população
populacao = inicializar_populacao(tam_pop, tam_caminho)
print("População inicial:")
print("==================")
for row in populacao: print(row)

geracao = 0
while geracao < max_geracoes:
    # Calcula a aptidão
    print("\nGeração: ",geracao)
    aptidao = []
    for individuo in populacao:
        aptidao.append(calcular_aptidao(individuo, inicio, fim))
    
    print("Aptidões: ",aptidao)
    melhor_ind = min(aptidao)
    melhor_ind_idx = aptidao.index(melhor_ind)
    print("Melhor Ind.: Apt.=", melhor_ind, "Caminho = ",populacao[melhor_ind_idx])
    if melhor_ind == 0:
        break
    
    # Seleção por torneio
    pai1 = [selecionar_por_torneio(populacao, aptidao, torneio) for _ in range(tam_pop//2)]
    pai2 = [selecionar_por_torneio(populacao, aptidao, torneio) for _ in range(tam_pop//2)]
    
    # Crossover
    filhos = []
    for i in range(0, tam_pop//2):
        filho1, filho2 = cruzar(pai1[i], pai2[i])
        filhos.append(filho1)
        filhos.append(filho2)
    
#   for row in filhos: print(row)
    
    # Mutação
    for individuo in filhos:
        mutar(individuo, tx_mut)
#   print("Mutação")
#   for row in filhos: print(row)
    
    # Substituição
    populacao = filhos.copy()
    geracao += 1

# Exibir o mapa inicial
print("\nMapa Inicial:")
exibir_mapa(mapa)

# Exibir o mapa com o caminho
print("\nMapa com o caminho:")
exibir_mapa_final(mapa, populacao[melhor_ind_idx], inicio, fim)