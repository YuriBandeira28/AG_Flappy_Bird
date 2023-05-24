import random
import numpy as np


def define_neuronio():
    pesos = [[0,0], [0,0], [0,0]] #0 - A, 1 - B, 2 -C

    neuronio = {  
       'A': {
              'saida': float(0.00),
              'ativacao': float(0.00),
              'pesos': pesos[0],
              'bias': float(0.0),
              
       }, 
       
       'B': {
              'saida': float(0.00),
              'ativacao': float(0.00),
              'pesos': pesos[1],
              'bias': float(0.0)
       },
       'C': {
              'saida': float(0.00),
              'ativacao': float(0.00),
              'pesos': pesos[2],
              'bias': float(0.0)
       }
}
    peso_a = random.random()
    peso_b = random.random()
    peso_c = random.random()

    neuronio['A']['pesos'] = peso_a
    neuronio['B']['pesos'] = peso_b
    neuronio['C']['pesos'] = peso_c
    
    print(neuronio)
    return neuronio

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def training(distancia_x, distancia_y, neuronio):
                   
    # cálculo da ativação e saída da primeira camada
    neuronio['A']['ativacao'] = neuronio['A']['pesos'][0]*distancia_x + neuronio['A']['pesos'][1]*distancia_y + neuronio['A']['bias']
    neuronio['B']['ativacao'] = neuronio['B']['pesos'][0]*distancia_x + neuronio['B']['pesos'][1]*distancia_y + neuronio['B']['bias']

    neuronio['A']['saida'] = sigmoid(neuronio['A']['ativacao'])
    neuronio['B']['saida'] = sigmoid(neuronio['B']['ativacao'])


    # cálculo da ativação e saída da última camada
    neuronio['C']['ativacao'] = neuronio['C']['pesos'][0]*neuronio['A']['saida'] + neuronio['C']['pesos'][1]*neuronio['B']['saida'] + neuronio['C']['bias']
    neuronio['C']['saida'] = sigmoid(neuronio['C']['ativacao'])
    
    print(neuronio['C']['saida'])
    
