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
                 
melhores = [0,0]
def selecao(genomas):

    global melhores
    genomas = sorted(genomas)
    melhor1 = max(genomas)
    melhores[0] = melhor1
    
    if  melhores[0] >= melhores[1]:
        melhor =  genomas.index(melhores[0])
        melhores[1] = melhores[0]
    else:
        melhor = genomas.index(melhores[1])
    
    return melhor


def mutacao(rede, tx_mut):

    
    pesos = {
        'A': [None, None, None],
        'B': [None, None, None],
        'C': [None, None],
        'D': [None, None],
        'E': [None, None],
        'F': [None, None, None],
        'G': [None, None, None]
        }
    bias = []
    
    for b in rede[0]:
        #b = b * tx_mut
        bias.append(b)

    pesos['A'][0] = rede[1]['A'][0] + ((rede[1]['A'][0] * tx_mut) * random.uniform(-1,1))
    pesos['A'][1] = rede[1]['A'][1] + ((rede[1]['A'][1] * tx_mut) * random.uniform(-1,1))
    pesos['A'][2] = rede[1]['A'][2] + ((rede[1]['A'][2] * tx_mut) * random.uniform(-1,1))

    pesos['B'][0] = rede[1]['B'][0] + ((rede[1]['B'][0] * tx_mut) * random.uniform(-1,1))
    pesos['B'][1] = rede[1]['B'][1] + ((rede[1]['B'][1] * tx_mut) * random.uniform(-1,1))
    pesos['B'][2] = rede[1]['B'][2] + ((rede[1]['B'][2] * tx_mut) * random.uniform(-1,1))

    pesos['C'][0] = rede[1]['C'][0] + ((rede[1]['C'][0] * tx_mut) * random.uniform(-1,1))
    pesos['C'][1] = rede[1]['C'][1] + ((rede[1]['C'][1] * tx_mut) * random.uniform(-1,1))
    pesos['D'][0] = rede[1]['D'][0] + ((rede[1]['D'][0] * tx_mut) * random.uniform(-1,1))
    pesos['D'][1] = rede[1]['D'][1] + ((rede[1]['D'][1] * tx_mut) * random.uniform(-1,1))
    pesos['E'][0] = rede[1]['E'][0] + ((rede[1]['E'][0] * tx_mut) * random.uniform(-1,1))
    pesos['E'][1] = rede[1]['E'][1] + ((rede[1]['E'][1] * tx_mut) * random.uniform(-1,1))
    pesos['F'][0] = rede[1]['F'][0] + ((rede[1]['F'][0] * tx_mut) * random.uniform(-1,1))
    pesos['F'][1] = rede[1]['F'][1] + ((rede[1]['F'][1] * tx_mut) * random.uniform(-1,1))
    pesos['F'][2] = rede[1]['F'][2] + ((rede[1]['F'][2] * tx_mut) * random.uniform(-1,1))
    pesos['G'][0] = rede[1]['G'][0] + ((rede[1]['G'][0] * tx_mut) * random.uniform(-1,1))
    pesos['G'][1] = rede[1]['G'][1] + ((rede[1]['G'][1] * tx_mut) * random.uniform(-1,1))
    pesos['G'][2] = rede[1]['G'][2] + ((rede[1]['G'][2] * tx_mut) * random.uniform(-1,1))
    print("sofreu mutação")
    return bias, pesos    

    
        
        