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
    
    #melhorPai2 = genomas[1]
    #melhoresPai2[0] = melhorPai2
    #if  melhoresPai2[0] >= melhoresPai2[1]:
    #    pai2 =  genomas.index(melhoresPai2[0])
    #    melhoresPai2[1] = melhoresPai2[0]
    #else:
    #    pai2 = genomas.index(melhoresPai2[1])
       
    pai2 = random.randint(0, len(genomas) - 1)
    
    return pai1, pai2

def cruzamento(rede1, rede2):
    
    pesos = {
        'A': [None, None],
        'B': [None, None],
        'C': [None, None],
        'D': [None, None],
        'E': [None, None],
        'F': [None, None, None],
        'G': [None, None, None]
        }
    bias = [rede2[0][0], rede1[0][1], 
            rede2[0][2], rede2[0][3],
            rede2[0][4],rede2[0][5], 
            rede2[0][6]]

    pesos['A'][0] = rede1[1]['A'][0]
    pesos['A'][1] = rede2[1]['A'][1]
    
    pesos['B'][0] = rede1[1]['B'][0]
    pesos['B'][1] = rede2[1]['B'][1]
    
    pesos['C'][0] = rede1[1]['C'][0]
    pesos['C'][1] = rede2[1]['C'][1]
    
    pesos['D'][0] = rede1[1]['D'][0]
    pesos['D'][1] = rede2[1]['D'][1]
    
    pesos['E'][0] = rede1[1]['E'][0]
    pesos['E'][1] = rede2[1]['E'][1]
    
    pesos['F'][0] = rede1[1]['F'][0]
    pesos['F'][1] = rede2[1]['F'][1]
    pesos['F'][2] = rede1[1]['F'][2]
    
    
    pesos['G'][0] = rede1[1]['G'][0]
    pesos['G'][1] = rede2[1]['G'][1]
    pesos['G'][2] = rede1[1]['G'][2]
    
    rede = (bias, pesos)

    print("fez o cruzamento")

    return rede

def mutacao(rede, tx_mut):

    pesos = {
        'A': [None, None],
        'B': [None, None],
        'C': [None, None],
        'D': [None, None],
        'E': [None, None],
        'F': [None, None, None],
        'G': [None, None, None]
        }
    bias = []
    for b in rede[0]:
        b = (b + (b * tx_mut)) * random.choice([-1,1])
        bias.append(b)


    #pesos['A'][0] = rede[1]['A'][0] + ((rede[1]['A'][0] * tx_mut) * random.uniform(-1,1))
    #pesos['A'][1] = rede[1]['A'][1] + ((rede[1]['A'][1] * tx_mut) * random.uniform(-1,1))
    #pesos['B'][0] = rede[1]['B'][0] + ((rede[1]['B'][0] * tx_mut) * random.uniform(-1,1))
    #pesos['B'][1] = rede[1]['B'][1] + ((rede[1]['B'][1] * tx_mut) * random.uniform(-1,1))
    #pesos['C'][0] = rede[1]['C'][0] + ((rede[1]['C'][0] * tx_mut) * random.uniform(-1,1))
    #pesos['C'][1] = rede[1]['C'][1] + ((rede[1]['C'][1] * tx_mut) * random.uniform(-1,1))

    pesos['A'][0] = (rede[1]['A'][0] + (((rede[1]['A'][0] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['A'][0] + ((rede[1]['A'][0] * tx_mut) + random.random())
    pesos['A'][1] = (rede[1]['A'][1] + (((rede[1]['A'][1] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['A'][1] + ((rede[1]['A'][1] * tx_mut) + random.random())
    pesos['B'][0] = (rede[1]['B'][0] + (((rede[1]['B'][0] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['B'][0] + ((rede[1]['B'][0] * tx_mut) + random.random())
    pesos['B'][1] = (rede[1]['B'][1] + (((rede[1]['B'][1] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['B'][1] + ((rede[1]['B'][1] * tx_mut) + random.random())
    pesos['C'][0] = (rede[1]['C'][0] + (((rede[1]['C'][0] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['C'][0] + ((rede[1]['C'][0] * tx_mut) + random.random())
    pesos['C'][1] = (rede[1]['C'][1] + (((rede[1]['C'][1] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['C'][1] + ((rede[1]['C'][1] * tx_mut) + random.random())
    pesos['D'][0] = (rede[1]['D'][0] + (((rede[1]['D'][0] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['A'][0] + ((rede[1]['A'][0] * tx_mut) + random.random())
    pesos['D'][1] = (rede[1]['D'][1] + (((rede[1]['D'][1] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['A'][1] + ((rede[1]['A'][1] * tx_mut) + random.random())
    pesos['E'][0] = (rede[1]['E'][0] + (((rede[1]['E'][0] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['B'][0] + ((rede[1]['B'][0] * tx_mut) + random.random())
    pesos['E'][1] = (rede[1]['E'][1] + (((rede[1]['E'][1] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['B'][1] + ((rede[1]['B'][1] * tx_mut) + random.random())
    pesos['F'][0] = (rede[1]['F'][0] + (((rede[1]['F'][0] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['C'][0] + ((rede[1]['C'][0] * tx_mut) + random.random())
    pesos['F'][1] = (rede[1]['F'][1] + (((rede[1]['F'][1] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['C'][1] + ((rede[1]['C'][1] * tx_mut) + random.random())
    pesos['F'][2] = (rede[1]['F'][2] + (((rede[1]['F'][2] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['A'][0] + ((rede[1]['A'][0] * tx_mut) + random.random())
    pesos['G'][0] = (rede[1]['G'][0] + (((rede[1]['G'][0] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['A'][1] + ((rede[1]['A'][1] * tx_mut) + random.random())
    pesos['G'][1] = (rede[1]['G'][1] + (((rede[1]['G'][1] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['B'][0] + ((rede[1]['B'][0] * tx_mut) + random.random())
    pesos['G'][2] = (rede[1]['G'][2] + (((rede[1]['G'][2] * tx_mut) * random.choice([-1,1])) * random.uniform(-1, 1))) * random.choice([-1,1])#rede[1]['B'][1] + ((rede[1]['B'][1] * tx_mut) + random.random())

    return bias, pesos    

    
        
        