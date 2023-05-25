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

def rede_neural():
    
    bias = [random.random(), random.random(), random.random()]
    
    pesos = {
        'A': [random.random(), random.random()],
        'B': [random.random(), random.random()],
        'C': [random.random(), random.random()]
    }
    
    return bias, pesos
        
def calcula_ativacao(dist_x, dist_y, bias, pesos):
    
    ativaçãoA= pesos['A'][0] * dist_x + pesos['A'][1] * dist_y + bias[0]
    ativaçãoB = pesos['B'][0] *dist_x + pesos['B'][1] * dist_y + bias[1]

    saidaA = sigmoid(ativaçãoA)
    saidaB = sigmoid(ativaçãoB)

    ativaçãoC = pesos['C'][0] * saidaA + pesos['C'][1] *saidaB + bias[2]
    # saidaC = sigmoid(ativaçãoC)
    return ativaçãoC


def evolui(melhor_individuo, birds, genomas, redes):
    print(redes[melhor_individuo][1])





