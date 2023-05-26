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
    melhor1 = max(genomas)
    
    melhores[0] = melhor1
    if  melhores[0] > melhores[1]:
        melhores[1] = melhores[0]
        melhor =  genomas.index(melhores[0])
    else:
        melhor = genomas.index(melhores[1])
    

    print(f"melhor - {genomas[melhor]} \n")
    
    return melhor


def mutacao(rede, tx_mut, geração, melhores_redes):

    print(f"REDE ANTES DA MUTAÇÃO {rede} \n")
    if melhores_redes != []:
        pesos = {
            'A': [None, None],
            'B': [None, None],
            'C': [None, None]
            }
        bias = []
        for b in rede[0]:
            b = b * tx_mut
            bias.append(b)

        if geração <= 5:
            pesos['A'][0] = rede[1]['A'][0] - ((rede[1]['A'][0] * 0.5) * tx_mut)
            pesos['A'][1] = rede[1]['A'][1] - ((rede[1]['A'][1] * 0.5) * tx_mut)
            pesos['B'][0] = rede[1]['B'][0] - ((rede[1]['B'][0] * 0.5) * tx_mut)
            pesos['B'][1] = rede[1]['B'][1] - ((rede[1]['B'][1] * 0.5) * tx_mut)
            pesos['C'][0] = rede[1]['C'][0] - ((rede[1]['C'][0] * 0.5) * tx_mut)
            pesos['C'][1] = rede[1]['C'][1] - ((rede[1]['C'][1] * 0.5) * tx_mut)
        else:
            print("entrou aqui")
            pesos['A'][0] = rede[1]['A'][0] - ((rede[1]['A'][0] * 0.5) * (tx_mut * random.random()) - random.uniform(-1,1))
            pesos['A'][1] = rede[1]['A'][1] - ((rede[1]['A'][1] * 0.5) * (tx_mut * random.random()) - random.uniform(-1,1))
            pesos['B'][0] = rede[1]['B'][0] - ((rede[1]['B'][0] * 0.5) * (tx_mut * random.random()) - random.uniform(-1,1))
            pesos['B'][1] = rede[1]['B'][1] - ((rede[1]['B'][1] * 0.5) * (tx_mut * random.random()) - random.uniform(-1,1))
            pesos['C'][0] = rede[1]['C'][0] - ((rede[1]['C'][0] * 0.5) * (tx_mut * random.random()) - random.uniform(-1,1))
            pesos['C'][1] = rede[1]['C'][1] - ((rede[1]['C'][1] * 0.5) * (tx_mut * random.random()) - random.uniform(-1,1))

        print(pesos)
        
        return bias, pesos    
    
    
        
        