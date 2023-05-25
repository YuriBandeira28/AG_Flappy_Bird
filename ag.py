import random
import numpy

def evolui(melhor_individuo, redes):
    tx_mut = 0.1
    redes_nova = [[],[]]
    
    for rede in redes[melhor_individuo][0]:
        rede = rede * tx_mut
        redes_nova[0].append(rede)
        
    for rede in redes[melhor_individuo][1]:
        add = redes[melhor_individuo][1]
        
        redes_nova[1].append(add)   
             
    print(redes_nova)
    
melhores = [0,0]
def selecao(genomas):

    global melhores
    genomas = sorted(genomas)
    melhor = max(genomas)
    
    melhores[0] = melhor
    if  melhores[0] > melhores[1]:
        melhores[1] = melhores[0]
        melhor =  genomas.index(melhores[0])
    else:
        melhor = genomas.index(melhores[1])

    print("melhores - ", )
    
    return melhor
def cruzamento(melhor):
    pass

def mutacao(rede, tx_mut):
    pesos = {
        'A': [None, None],
        'B': [None, None],
        'C': [None, None]
        }
    bias = []
    for b in rede[0]:
        b = b * tx_mut
        bias.append(b)
    pesos['A'][0] = (rede[1]['A'][0] * tx_mut) + rede[1]['A'][0]
    pesos['A'][1] = (rede[1]['A'][1] * tx_mut) + rede[1]['A'][1]
    
    pesos['B'][0] = (rede[1]['B'][0] * tx_mut) + rede[1]['B'][0]
    pesos['B'][1] = (rede[1]['B'][1] * tx_mut) + rede[1]['B'][1]
    
    pesos['C'][0] = (rede[1]['C'][0] * tx_mut) + rede[1]['C'][0]
    pesos['C'][1] = (rede[1]['C'][1] * tx_mut) + rede[1]['C'][1]

    
    return bias, pesos    
    
    
        
        