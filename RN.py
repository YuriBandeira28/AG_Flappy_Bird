import random
pesos = [0 , 0]
bias = 0

def treino():
    som_erro = 1
    erro = 0.0
    iteracao = 1
   
    
    max_itter = 50
    saida = 0
    tx_learn = 1.00

    global pesos
    global bias

    while iteracao < max_itter:
        som_erro = 0
        for i in range(len(matriz_treino_and)):
            saida = pesos[0] * matriz_treino_and[i][0] + pesos[1] * matriz_treino_and[i][1] + bias
            if saida >= 0:
                saida = 1
            else:
                saida = 0
            erro = matriz_treino_and[i][2] - saida

            pesos[0] = pesos[0] + tx_learn*erro*matriz_treino_and[i][0]
            pesos[1] = pesos[1] + tx_learn*erro*matriz_treino_and[i][1]
            bias = bias + tx_learn*erro
            
            if erro != 0:
                som_erro = som_erro + 1
        iteracao +=1
        if som_erro == 0:
            print('Treino OK!')
        else:
            print("Erro no treino")


    
def usage():
   
    saida = int(0)
    opcao = 'S'
    while opcao == "S":

        entrada_1 = int(input("insira um valor de entrada (1 ou 0)"))
        entrada_2 = int(input("insira outro valor de entrada (1 ou 0)"))

        """if entrada_1 != 0 or entrada_1 != 1 or entrada_2 != 0 or entrada_2 != 1: 
            print("Valor incorreto, por favor, insira somente 1 ou 0")
            continue"""
        
        saida = pesos[0]* entrada_1 + pesos[1] * entrada_2 + bias
        if saida >= 0:
            saida = 1
        else:
            saida = 0

        print("Entrada 1 - ", entrada_1)
        print("Entrada 2 - ", entrada_2)
        print("Saída  - ", saida)

        opcao = str(input("Quer continuar? (S ou N)")).upper()


treino()
usage()

