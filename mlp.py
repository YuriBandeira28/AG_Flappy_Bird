import random
import numpy as np

dados = {
       'or': [[0.0, 0.0, 0.0],
           [0.0, 1.0, 1.0],
           [1.0, 0.0, 1.0],
           [1.0, 1.0, 1.0]],
    
       'and': [[0.0, 0.0, 0.0],
           [0.0, 1.0, 0.0],
           [1.0, 0.0, 0.0],
           [1.0, 1.0, 1.0]],
    
       'xor': [[0.0, 0.0, 0.0],
           [0.0, 1.0, 1.0],
           [1.0, 0.0, 1.0],
           [1.0, 1.0, 0.0]],

       'nand' : [[0.0, 0.0, 1.0],
           [0.0, 1.0, 1.0],
           [1.0, 0.0, 1.0],
           [1.0, 1.0, 0.0]]
}

neuronios = {  
       'A': {
              'erro': float(0.00),
              'saida': float(0.00),
              'ativacao': float(0.00)
       }, 
       
       'B': {
              'erro': float(0.00),
              'saida': float(0.00),
              'ativacao': float(0.00)
       },
       
       'C': {
              'erro': float(0.00),
              'saida': float(0.00),
              'ativacao': float(0.00)
       }
}

bias = [1.0, 1.0, 1.0] #a, b, c


pesos_A = list([random.uniform(-1.2,1.2), random.uniform(-1.2, 1.2)])
pesos_B = list([random.uniform(-1.2,1.2), random.uniform(-1.2, 1.2)])
pesos_C = list([random.uniform(-1.2,1.2), random.uniform(-1.2, 1.2)]) # 0=A, 1=B

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def treinamento(entrada, max_iter, tx_aprend):
       sair = 0
       erroGlobal = 0
       it = 0
       j = 0
       global neuronios
       global bias
       global pesos_A
       global pesos_B
       global pesos_C

       while it <= max_iter and sair == 0:
              quadErro = 0

              for i in range(len(entrada)):
                    
                     # cálculo da ativação e saída da primeira camada
                     neuronios['A']['ativacao'] = pesos_A[0]*entrada[i][0] + pesos_A[1]*entrada[i][1] + bias[0]
                     neuronios['B']['ativacao'] = pesos_B[0]*entrada[i][0] + pesos_B[1]*entrada[i][1] + bias[1]

                     neuronios['A']['saida'] = sigmoid(neuronios['A']['ativacao'])
                     neuronios['B']['saida'] = sigmoid(neuronios['B']['ativacao'])


                     # cálculo da ativação e saída da última camada
                     neuronios['C']['ativacao'] = pesos_C[0]*neuronios['A']['saida'] + pesos_C[1]*neuronios['B']['saida'] + bias[2]
                     neuronios['C']['saida'] = sigmoid(neuronios['C']['ativacao'])


                     # cálculo do erro na saída da rede
                     erroGlobal = entrada[i][2] - neuronios['C']['saida']

                     #quadErro = quadErro + (erroGlobal**2)

                     # cálculo do erro local da última camada
                     neuronios['C']['erro'] = erroGlobal *  neuronios['C']['saida'] * (1- neuronios['C']['saida'])

                     # cálculo do erro local da primeira camada
                     neuronios['A']['erro'] = neuronios['A']['saida']*(1- neuronios['A']['saida']) * pesos_C[0]*neuronios['C']['erro']
                     neuronios['B']['erro'] = neuronios['B']['saida']*(1- neuronios['B']['saida']) * pesos_C[1]*neuronios['C']['erro']

                     
                     # Ajuste dos pesos nas unidades intermediárias (Neurônio A)
                     bias[0] = bias[0] + (tx_aprend * neuronios['A']['erro'] * bias[0])
                     pesos_A[0] = pesos_A[0] + (tx_aprend * neuronios['A']['erro'] * entrada[i][0])
                     pesos_A[1] = pesos_A[1] + (tx_aprend * neuronios['A']['erro'] * entrada[i][1])

                     # Ajuste dos pesos nas unidades intermediárias (Neurônio B)
                     bias[1] = bias[1] + (tx_aprend * neuronios['B']['erro'] * bias[1])
                     pesos_B[0] = pesos_B[0] + (tx_aprend * neuronios['B']['erro'] * entrada[i][0])
                     pesos_B[1] = pesos_B[1] + (tx_aprend * neuronios['B']['erro'] * entrada[i][1])

                     # ajuste dos pesos e bias da última camada 
                     bias[2] = bias[2] + (tx_aprend * neuronios['C']['erro'] * bias[2])
                     pesos_C[0] = pesos_C[0] + (tx_aprend * neuronios['C']['erro'] * neuronios['A']['saida'])
                     pesos_C[1] = pesos_C[1] + (tx_aprend * neuronios['C']['erro'] * neuronios['B']['saida'])

              j+=1   
              if j >4:
                     j = 0 
                     quadErro = quadErro + (erroGlobal * erroGlobal)
                     if quadErro <= 0.001:
                            sair = 1
                            print("treinamento ok!")
                     else:
                            sair = 0
                            quadErro = 0
              else:
                     quadErro = quadErro + (erroGlobal * erroGlobal)
              
              print("quad erro - ", quadErro)
              it = it+1


def use():
       op = 'S'

       while op == 'S':
              entrada_user1 = int(input("Insira um valor para entrada (0 ou 1)- "))
              entrada_user2 = int(input("Insira outro valor para entrada (0 ou 1)- "))

              neuronios['A']['ativacao'] = bias[0] + pesos_A[0] * entrada_user1 + pesos_A[1] * entrada_user2
              neuronios['B']['ativacao'] = bias[1] + pesos_B[0] * entrada_user1 + pesos_B[1] * entrada_user2

              neuronios['A']['saida'] = sigmoid(neuronios['A']['ativacao'])
              neuronios['B']['saida'] = sigmoid(neuronios['B']['ativacao'])

              neuronios['C']['ativacao'] = bias[2] + pesos_C[0] * neuronios['A']['saida'] + pesos_C[1] * neuronios['B']['saida']
              neuronios['C']['saida'] = sigmoid(neuronios['C']['ativacao'])

              saida_use = neuronios['C']['saida']

              if saida_use < 0.5:
                     saida_use = 0
              else:
                     saida_use = 1

              print("Entrada 1 - ", entrada_user1)
              print("Entrada 2 - ", entrada_user2)
              print("Saída  - ", saida_use)
              
              op = str(input('Deseja Continuar, S ou N - ')).upper()   

    

chave = str(input("Insira uma tabela para treino: XOR, OR, AND, NAND - ")).lower()
n_iter = int(input("Insira o número máxmo de iterações - "))
tx_aprend = float(input("Insira a taxa de aprendizado para a rede - "))
ent = dados[chave]

treinamento(ent, n_iter, tx_aprend)
use()