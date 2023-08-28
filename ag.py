import random
import numpy as np

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
    genomas1 = genomas
    genomas = sorted(genomas)
    melhor1 = max(genomas)
    melhores[0] = melhor1
    
    # if  melhores[0] >= melhores[1]:
    #     pai1 =  genomas.index(melhores[0])
    #     melhores[1] = melhores[0]
    # else:
    #     pai1 = genomas.index(melhores[1])
        
    # if np.isclose(a = max(genomas), b = genomas1[-1], atol=3):
    #     pai2 = genomas1.index(genomas1[-1])
    #     pai2 = pai2 - random.randint(0, 10)
    #     pai1 = genomas.index(genomas[random.randrange(0, len(genomas) -1)])
    #     #print("pegou o aproximado")
    #     return pai2, pai1
    # else:
    #     pai2 = genomas.index(genomas[random.randrange(0, len(genomas) -1)])
    #     #print("pegou o aleatorio")
    #     return pai1, pai2
    return genomas.index(melhor1), genomas.index(melhor1)


def cruzamento(rede1, rede2):
    
    pesos = {
        'A': [None, None, None],
        'B': [None, None, None],
        'C': [None, None],
        'D': [None, None],
        'E': [None, None],
        'F': [None, None],
        'G': [None, None],
        'H': [None, None],
        'I': [None, None, None,
              None, None, None],
        'J': [None, None, None,
              None, None, None]
        }
    
    corte_bias = random.randrange(0, len(rede1[0]) - 1)

    bias = rede1[0][:corte_bias] + rede2[0][corte_bias:]
    

    pesos['A'][0] = rede1[1]['A'][0]
    pesos['A'][1] = rede2[1]['A'][1]
    pesos['A'][2] = rede1[1]['A'][2]

    pesos['B'][0] = rede1[1]['B'][0]
    pesos['B'][1] = rede2[1]['B'][1]
    pesos['B'][2] = rede1[1]['B'][2]

    pesos['C'][0] = rede1[1]['C'][0]
    pesos['C'][1] = rede1[1]['C'][1]
    
    pesos['D'][0] = rede2[1]['D'][0]
    pesos['D'][1] = rede2[1]['D'][1]
    
    pesos['E'][0] = rede1[1]['E'][0]
    pesos['E'][1] = rede1[1]['E'][1]

    pesos['F'][0] = rede2[1]['F'][0]
    pesos['F'][1] = rede2[1]['F'][1]

    pesos['G'][0] = rede1[1]['G'][0]
    pesos['G'][1] = rede1[1]['G'][1]

    pesos['H'][0] = rede2[1]['H'][0]
    pesos['H'][1] = rede2[1]['H'][1]

    
    pesos['I'][0] = rede1[1]['J'][0]
    pesos['I'][1] = rede2[1]['J'][1]
    pesos['I'][2] = rede1[1]['J'][2]
    pesos['I'][3] = rede1[1]['J'][3]
    pesos['I'][4] = rede2[1]['J'][4]
    pesos['I'][5] = rede1[1]['J'][5]    



    pesos['J'][0] = rede1[1]['J'][0]
    pesos['J'][1] = rede2[1]['J'][1]
    pesos['J'][2] = rede1[1]['J'][2]
    pesos['J'][3] = rede1[1]['J'][3]
    pesos['J'][4] = rede2[1]['J'][4]
    pesos['J'][5] = rede1[1]['J'][5]



    rede = (bias, pesos)

    #print("fez o cruzamento")
    return rede


def mutacao(rede, tx_mut):

    
    pesos = {
        'A': [None, None, None],
        'B': [None, None, None],
        'C': [None, None],
        'D': [None, None],
        'E': [None, None],
        'F': [None, None],
        'G': [None, None],
        'H': [None, None],
        'I': [None, None, None,
              None, None, None],
        'J': [None, None, None,
              None, None, None]
        }
    bias = []
    
    for b in rede[0]:
        #b = b * tx_mut
        bias.append(b)

    if random.random() < tx_mut:
        pesos['A'][0] = rede[1]['A'][0] + ((rede[1]['A'][0] * tx_mut) +(rede[1]['A'][0] + random.uniform(-1,1)))
        pesos['A'][1] = rede[1]['A'][1] + ((rede[1]['A'][1] * tx_mut) +(rede[1]['A'][1] + random.uniform(-1,1)))
        pesos['A'][2] = rede[1]['A'][2] + ((rede[1]['A'][2] * tx_mut) +(rede[1]['A'][2] + random.uniform(-1,1)))
        pesos['B'][0] = rede[1]['B'][0] + ((rede[1]['B'][0] * tx_mut) +(rede[1]['B'][0] + random.uniform(-1,1)))
        pesos['B'][1] = rede[1]['B'][1] + ((rede[1]['B'][1] * tx_mut) +(rede[1]['B'][1] + random.uniform(-1,1)))
        pesos['B'][2] = rede[1]['B'][2] + ((rede[1]['B'][2] * tx_mut) +(rede[1]['B'][2] + random.uniform(-1,1)))
        pesos['C'][0] = rede[1]['C'][0] + ((rede[1]['C'][0] * tx_mut) +(rede[1]['C'][0] + random.uniform(-1,1)))
        pesos['C'][1] = rede[1]['C'][1] + ((rede[1]['C'][1] * tx_mut) +(rede[1]['C'][1] + random.uniform(-1,1)))
        pesos['D'][0] = rede[1]['D'][0] + ((rede[1]['D'][0] * tx_mut) +(rede[1]['D'][0] + random.uniform(-1,1)))
        pesos['D'][1] = rede[1]['D'][1] + ((rede[1]['D'][1] * tx_mut) +(rede[1]['D'][1] + random.uniform(-1,1)))
        pesos['E'][0] = rede[1]['E'][0] + ((rede[1]['E'][0] * tx_mut) +(rede[1]['E'][0] + random.uniform(-1,1)))
        pesos['E'][1] = rede[1]['E'][1] + ((rede[1]['E'][1] * tx_mut) +(rede[1]['E'][1] + random.uniform(-1,1)))
        pesos['F'][0] = rede[1]['F'][0] + ((rede[1]['F'][0] * tx_mut) +(rede[1]['F'][0] + random.uniform(-1,1)))
        pesos['F'][1] = rede[1]['F'][1] + ((rede[1]['F'][1] * tx_mut) +(rede[1]['F'][1] + random.uniform(-1,1)))
        pesos['G'][0] = rede[1]['G'][0] + ((rede[1]['G'][0] * tx_mut) +(rede[1]['G'][0] + random.uniform(-1,1)))
        pesos['G'][1] = rede[1]['G'][1] + ((rede[1]['G'][1] * tx_mut) +(rede[1]['G'][1] + random.uniform(-1,1)))
        pesos['H'][0] = rede[1]['H'][0] + ((rede[1]['H'][0] * tx_mut) +(rede[1]['H'][0] + random.uniform(-1,1)))
        pesos['H'][1] = rede[1]['H'][1] + ((rede[1]['H'][1] * tx_mut) +(rede[1]['H'][1] + random.uniform(-1,1)))
        pesos['I'][0] = rede[1]['I'][0] + ((rede[1]['I'][0] * tx_mut) +(rede[1]['I'][0] + random.uniform(-1,1)))
        pesos['I'][1] = rede[1]['I'][1] + ((rede[1]['I'][1] * tx_mut) +(rede[1]['I'][1] + random.uniform(-1,1)))
        pesos['I'][2] = rede[1]['I'][2] + ((rede[1]['I'][2] * tx_mut) +(rede[1]['I'][2] + random.uniform(-1,1)))
        pesos['I'][3] = rede[1]['I'][3] + ((rede[1]['I'][3] * tx_mut) +(rede[1]['I'][3] + random.uniform(-1,1)))
        pesos['I'][4] = rede[1]['I'][4] + ((rede[1]['I'][4] * tx_mut) +(rede[1]['I'][4] + random.uniform(-1,1)))
        pesos['I'][5] = rede[1]['I'][5] + ((rede[1]['I'][1] * tx_mut) +(rede[1]['I'][1] + random.uniform(-1,1)))
        pesos['J'][0] = rede[1]['J'][0] + ((rede[1]['J'][0] * tx_mut) +(rede[1]['J'][0] + random.uniform(-1,1)))
        pesos['J'][1] = rede[1]['J'][1] + ((rede[1]['J'][1] * tx_mut) +(rede[1]['J'][1] + random.uniform(-1,1)))
        pesos['J'][2] = rede[1]['J'][2] + ((rede[1]['J'][2] * tx_mut) +(rede[1]['J'][2] + random.uniform(-1,1)))
        pesos['J'][3] = rede[1]['J'][3] + ((rede[1]['J'][3] * tx_mut) +(rede[1]['J'][3] + random.uniform(-1,1)))
        pesos['J'][4] = rede[1]['J'][4] + ((rede[1]['J'][4] * tx_mut) +(rede[1]['J'][4] + random.uniform(-1,1)))
        pesos['J'][5] = rede[1]['J'][5] + ((rede[1]['J'][1] * tx_mut) +(rede[1]['J'][1] + random.uniform(-1,1)))


        #print("sofreu mutação"
        return bias, pesos  
    else:
        return rede[0], rede[1]  


            
            