import random
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def rede_neural(pesos = None):
    
    bias = [random.uniform(-1.2,1.2), # 0 - neuronio A
            random.uniform(-1.2,1.2), # 1 - neuronio B
            random.uniform(-1.2,1.2), # 2 - neuronio C
            random.uniform(-1.2,1.2), # 3 - neuronio D
            random.uniform(-1.2,1.2), # 4 - neuronio E
            random.uniform(-1.2,1.2), # 5 - neuronio F
            random.uniform(-1.2,1.2)] # 6 - neuronio G
    
    
    if pesos == None:
        
        pesos = {
            'A': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)],
            'B': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)],
            'C': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)],
            'D': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)],
            'E': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)],
            'F': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)],
            'G': [random.uniform(-1.2,1.2), random.uniform(-1.2,1.2), random.uniform(-1.2,1.2)]
        }
        
    else:
        pesos = pesos
    
    return bias, pesos
        
def calcula_ativacao(dist_x, dist_y, bias, pesos):
    
    #neuronios de entrada
    ativacaoA= pesos['A'][0] * dist_x + pesos['A'][1] * dist_y + bias[0]
    ativacaoB = pesos['B'][0] *dist_x + pesos['B'][1] * dist_y + bias[1]

    saidaA = sigmoid(ativacaoA)
    saidaB = sigmoid(ativacaoB)

    #neuronios intermediários
    ativacaoC = pesos['C'][0] * saidaA + pesos['C'][1] *saidaB + bias[2]
    ativacaoD = pesos['D'][0] * saidaA + pesos['D'][1] *saidaB + bias[3]
    ativacaoE = pesos['E'][0] * saidaA + pesos['E'][1] *saidaB + bias[4]
    
    saidaC = sigmoid(ativacaoC)
    saidaD = sigmoid(ativacaoD)
    saidaE = sigmoid(ativacaoE)

    #neuronios de saída
    ativacaoF = pesos['F'][0] * saidaC + pesos['F'][1] *saidaD + saidaE * pesos['F'][2] + bias[5]
    ativacaoG = pesos['G'][0] * saidaC + pesos['G'][1] *saidaD + saidaE * pesos['G'][2] + bias[6]
    
    saidaF = sigmoid(ativacaoF)    
    saidaG = sigmoid(ativacaoG)
    
    #saída
    return saidaF, saidaG






