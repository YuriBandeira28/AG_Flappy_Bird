import random
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class Genoma():
    
    fitness = 0

    def __init__(self):
        pass
        
    def start_população(tamanho):
        genomas = []
        for i in range(tamanho):
            genomas.append(Genoma())
            
        return genomas

def rede_neural(pesos = None):
    
    bias = [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)]
    
    if pesos == None:
        
        pesos = {
            'A': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)],
            'B': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)],
            'C': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)]
        }
        #pesos = {
        #'A': [random.uniform(0, 1), random.uniform(0, 1)],
        #'B': [random.uniform(0, 1), random.uniform(0, 1)],
        #'C': [random.uniform(0, 1), random.uniform(0, 1)]
        #}
       
    else:
        pesos = pesos
        
    
    return bias, pesos
        
def calcula_ativacao(dist_x, dist_y, bias, pesos):
    
    ativaçãoA= pesos['A'][0] * dist_x + pesos['A'][1] * dist_y + bias[0]
    ativaçãoB = pesos['B'][0] *dist_x + pesos['B'][1] * dist_y + bias[1]

    saidaA = sigmoid(ativaçãoA)
    saidaB = sigmoid(ativaçãoB)

    ativaçãoC = pesos['C'][0] * saidaA + pesos['C'][1] *saidaB + bias[2]
    # saidaC = sigmoid(ativaçãoC)
    return ativaçãoC






