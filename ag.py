import random
import numpy


class Genoma():
    
    fitness = 0

    def __init__(self):
        pass
        
    def start_população(tamanho):
        genomas = []
        for i in range(tamanho):
            genomas.append(Genoma())
            
        return genomas
    
    
def evolui(melhor_individuo, redes):
    tx_mut = 0.1
    redes_nova = [[],[]]
    
    for rede in redes[melhor_individuo][0]:
        rede = rede * tx_mut
        redes_nova[0].append(rede)
        
    for rede in redes[melhor_individuo][1]:
        add = redes[melhor_individuo][1]
        
        redes_nova[1].append(add)   
                 
melhoresPai1 = [0,0]
melhoresPai2 = [0,0]
def selecao(genomas):

    global melhoresPai1
    global melhoresPai2

    #pai2 = genomas.index(genomas[-1])
    genomas = sorted(genomas, reverse=True)

    # seleciona o melhor pai
    melhorPai1 = genomas[0]
    melhoresPai1[0] = melhorPai1
    if  melhoresPai1[0] >= melhoresPai1[1]:
        pai1 =  genomas.index(melhoresPai1[0])
        melhoresPai1[1] = melhoresPai1[0]
    else:
        pai1 = genomas.index(melhoresPai1[1])

    # seleciona o 2º melhor pai
    
    melhorPai2 = genomas[1]
    melhoresPai2[0] = melhorPai2
    if  melhoresPai1[0] >= melhoresPai2[1]:
        pai2 =  genomas.index(melhoresPai2[0])
        melhoresPai2[1] = melhoresPai2[0]
    else:
        pai2 = genomas.index(melhoresPai2[1])
       
    #pai2 = random.randint(0, len(genomas) - 1)
    
    return pai1, pai2

def cruzamento(rede1, rede2):
    
    pesos = {
        'A': [None, None],
        'B': [None, None],
        'C': [None, None]
        }
    bias = [rede2[0][0], rede1[0][1], rede2[0][2]]

    pesos['A'][0] = rede1[1]['A'][0]
    pesos['A'][1] = rede2[1]['A'][1]
    pesos['B'][0] = rede1[1]['B'][0]
    pesos['B'][1] = rede2[1]['B'][1]
    pesos['C'][0] = rede1[1]['C'][0]
    pesos['C'][1] = rede2[1]['C'][1]

    rede = (bias, pesos)

    print("fez o cruzamento")

    return rede

def mutacao(rede, tx_mut):

    pesos = {
        'A': [None, None],
        'B': [None, None],
        'C': [None, None]
        }
    bias = []
    for b in rede[0]:
       #b = b * tx_mut
        bias.append(b)



    #pesos['A'][0] = rede[1]['A'][0] + ((rede[1]['A'][0] * tx_mut) * random.uniform(-1,1))
    #pesos['A'][1] = rede[1]['A'][1] + ((rede[1]['A'][1] * tx_mut) * random.uniform(-1,1))
    #pesos['B'][0] = rede[1]['B'][0] + ((rede[1]['B'][0] * tx_mut) * random.uniform(-1,1))
    #pesos['B'][1] = rede[1]['B'][1] + ((rede[1]['B'][1] * tx_mut) * random.uniform(-1,1))
    #pesos['C'][0] = rede[1]['C'][0] + ((rede[1]['C'][0] * tx_mut) * random.uniform(-1,1))
    #pesos['C'][1] = rede[1]['C'][1] + ((rede[1]['C'][1] * tx_mut) * random.uniform(-1,1))

    pesos['A'][0] = (rede[1]['A'][0] + ((rede[1]['A'][0] * tx_mut) * random.uniform(0, 2))) * random.choice([-1,1])#rede[1]['A'][0] + ((rede[1]['A'][0] * tx_mut) + random.random())
    pesos['A'][1] = (rede[1]['A'][1] + ((rede[1]['A'][1] * tx_mut) * random.uniform(0, 2))) * random.choice([-1,1])#rede[1]['A'][1] + ((rede[1]['A'][1] * tx_mut) + random.random())
    pesos['B'][0] = (rede[1]['B'][0] + ((rede[1]['B'][0] * tx_mut) * random.uniform(0, 2))) * random.choice([-1,1])#rede[1]['B'][0] + ((rede[1]['B'][0] * tx_mut) + random.random())
    pesos['B'][1] = (rede[1]['B'][1] + ((rede[1]['B'][1] * tx_mut) * random.uniform(0, 2))) * random.choice([-1,1])#rede[1]['B'][1] + ((rede[1]['B'][1] * tx_mut) + random.random())
    pesos['C'][0] = (rede[1]['C'][0] + ((rede[1]['C'][0] * tx_mut) * random.uniform(0, 2))) * random.choice([-1,1])#rede[1]['C'][0] + ((rede[1]['C'][0] * tx_mut) + random.random())
    pesos['C'][1] = (rede[1]['C'][1] + ((rede[1]['C'][1] * tx_mut) * random.uniform(0, 2))) * random.choice([-1,1])#rede[1]['C'][1] + ((rede[1]['C'][1] * tx_mut) + random.random())

    return bias, pesos    

    
        
        