import pygame
import os
import random
import rede_neural
import ag


ia_jogando = True
geracao = 0


win_height = 600 #altura
win_width = 1100 #largura
 


#carregando e alterando a escala das imagens
img_cano = pygame.transform.scale(size=(50,400),surface=pygame.image.load(os.path.join('imgs', 'pipe.png')))
img_cano_pequeno = pygame.transform.scale(size=(50,400),surface=pygame.image.load(os.path.join('imgs', 'pipeP.png')))
img_fundo = pygame.transform.scale(size=(275, 600), surface=pygame.image.load(os.path.join('imgs', 'bg.png')))
img_chao = pygame.transform.scale(size=(1100, 170),surface=pygame.image.load(os.path.join('imgs', 'base.png')))

imgs_brid = [
    pygame.image.load(os.path.join('imgs', 'bird1.png')),
    pygame.image.load(os.path.join('imgs', 'bird2.png')),
    pygame.image.load(os.path.join('imgs', 'bird3.png'))
]

#texto pontuação
pygame.font.init()
fontes = pygame.font.SysFont('arial', 50)


#classes para definir os objetos (que se movem na tela)

class Bird:
    #constantes para o pássro
    imgs = imgs_brid
    
    #animações de animaçao
    rotacao_max = 25
    velocidade_rotacao = 20
    temp_animacao = 5
    recarga_dash = 250
    dash_disponivel = False

    #atributos para o pássaro

    def __init__(self, pos_x , pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dashe = False
        self.dash_duracao = 40
        self.angulo = 0
        self.velociade = 0
        self.altura = self.pos_y
        self.tempo = 0
        self.cont_img = 0
        self.img = self.imgs[0]

    def jump (self):
        
        self.velociade = -8.9 
        self.tempo = 0
        self.altura = self.pos_y

    def dash(self):
        self.dashe = True

    def move(self):

        #deslocamento
        self.tempo += 1

        deslocamento = 1.5 * (self.tempo**2) + self.velociade * self.tempo

        #restringir o deslocamento
        if deslocamento > 10:
            deslocamento = 10

        elif deslocamento < 0:
            deslocamento -=2

        if not self.dashe:
            self.pos_y += deslocamento
        else:
            if self.dash_duracao > 0:
                self.dash_duracao -=1
            else:
                self.dash_duracao = 30
                self.dashe = False
            

        #angulo do pássaro
        if deslocamento < 0 or self.pos_y < (self.altura + 50):
            if self.angulo < self.rotacao_max:
                self.angulo = self.rotacao_max
        else: 
            if self.angulo > -90:
                self.angulo -=self.velocidade_rotacao

    def desenhar(self, tela):
        #definir imagem do pássaro a ser usada (bird1, bird2 ou bird3)
        self.cont_img += 1

        if self.cont_img > self.temp_animacao:
            self.img = self.imgs[0]

        elif self.cont_img < self.temp_animacao*2:
            self.img = self.imgs[1]

        elif self.cont_img < self.temp_animacao*3:
            self.img = self.imgs[2]

        elif self.cont_img < self.temp_animacao*4:
            self.img = self.imgs[1]

        elif self.cont_img >= self.temp_animacao*4 + 1:
            self.img = self.imgs[0]
            self.cont_img = 0

        #ajustes de animações
        if self.angulo <= -75:

            self.img = self.imgs[1]
            self.cont_img = self.temp_animacao*2

        #desenhar a imagem
        img_rotacionada = pygame.transform.rotate(self.img, self.angulo)
        pos_centro_img = self.img.get_rect(topleft = (self.pos_x, self.pos_y)).center
        retangulo = img_rotacionada.get_rect(center=pos_centro_img)
        tela.blit(img_rotacionada, retangulo.topleft)

    def get_mask(self):
        #define uma máscara para o pássaro (melhorando o sistema de colisão)
        return pygame.mask.from_surface(self.img)
    
class PipePequeno:
    
    dist = 60 #de um cano para o outro
    vel_move = 4

    def __init__(self, pos_x):
        self.pos_x = pos_x
        self.altura = 0
        self.pos_top = 0
        self.pos_base = 0
        self.img_top = pygame.transform.flip(img_cano_pequeno, False, True)
        self.img_base = img_cano_pequeno

        self.passou = False
        self.define_altura()

    def define_altura(self):
        self.altura = random.randrange(40, 400)
        self.pos_top  = self.altura - self.img_top.get_height()
        self.pos_base = self.altura + self.dist

    def move(self):
        self.pos_x -= self.vel_move


    def desenhar(self, tela):
        #desenha os canos
        tela.blit(self.img_base, (self.pos_x, self.pos_base))
        tela.blit(self.img_top, (self.pos_x, self.pos_top))
    
    def colider(self, bird):

        bird_mask= bird.get_mask()
        top_mask = pygame.mask.from_surface(self.img_top)
        base_mask = pygame.mask.from_surface(self.img_base)

        distancia_top = (round(self.pos_x) - round(bird.pos_x), round(self.pos_top) - round(bird.pos_y))
        distancia_base = (round(self.pos_x) - round(bird.pos_x), round(self.pos_base) - round(bird.pos_y))

        base_point_colider = bird_mask.overlap(base_mask, distancia_base)
        top_point_colider = bird_mask.overlap(top_mask, distancia_top)

        if base_point_colider or top_point_colider:
            return True
        else:
            return False
        
class Pipe:
    
    dist = 120 #de um cano para o outro
    vel_move = 4

    def __init__(self, pos_x):
        self.pos_x = pos_x
        self.altura = 0
        self.pos_top = 0
        self.pos_base = 0
        self.img_top = pygame.transform.flip(img_cano, False, True)
        self.img_base = img_cano

        self.passou = False
        self.define_altura()

    def define_altura(self):
        self.altura = random.randrange(20, 300)
        self.pos_top  = self.altura - self.img_top.get_height()
        self.pos_base = self.altura + self.dist

    def move(self):
        self.pos_x -= self.vel_move


    def desenhar(self, tela):
        #desenha os canos
        tela.blit(self.img_base, (self.pos_x, self.pos_base))
        tela.blit(self.img_top, (self.pos_x, self.pos_top))
    
    def colider(self, bird):

        bird_mask= bird.get_mask()
        top_mask = pygame.mask.from_surface(self.img_top)
        base_mask = pygame.mask.from_surface(self.img_base)

        distancia_top = (round(self.pos_x) - round(bird.pos_x), round(self.pos_top) - round(bird.pos_y))
        distancia_base = (round(self.pos_x) - round(bird.pos_x), round(self.pos_base) - round(bird.pos_y))

        base_point_colider = bird_mask.overlap(base_mask, distancia_base)
        top_point_colider = bird_mask.overlap(top_mask, distancia_top)

        if base_point_colider or top_point_colider:
            return True
        else:
            return False
        
class Base:

    velocidade = 5
    lalrgura = img_chao.get_width()
    img = img_chao

    def __init__(self, pos_y):
        self.pos_y = pos_y
        self.x1 = 0
        self.x2 = self.lalrgura

    def move(self):
        self.x1 -= self.velocidade
        self.x2 -= self.velocidade
        
        if self.x1 + self.lalrgura < 0:
            self.x1 = self.x2 + self.lalrgura

        if self.x2 + self.lalrgura < 0:
            self.x2 = self.x1 + self.lalrgura

    def desenhar(self, tela):
        tela.blit(self.img, (self.x1, self.pos_y))
        tela.blit(self.img, (self.x2, self.pos_y))
        
class Fundo:

    velocidade = 4
    lalrgura = img_fundo.get_width()
    img = img_fundo

    def __init__(self, pos_y):
        self.pos_y = pos_y
        self.x1 = 0
        self.x2 = self.lalrgura

    def move(self):
        self.x1 -= self.velocidade
        self.x2 -= self.velocidade
        
        if self.x1 + self.lalrgura < 0:
            self.x1 = self.x2 + self.lalrgura

        if self.x2 + self.lalrgura < 0:
            self.x2 = self.x1 + self.lalrgura

    def desenhar(self, tela):
        tela.blit(self.img, (self.x1, self.pos_y))
        tela.blit(self.img, (self.x2, self.pos_y))

def desenhar_tela(tela, birds, pipes, base, pontos):

    tela.blit(img_fundo, (0, 0)) #desenhar fundo
    tela.blit(img_fundo, (275, 0)) #desenhar fundo
    tela.blit(img_fundo, (550, 0)) #desenhar fundo
    tela.blit(img_fundo, (825, 0)) #desenhar fundo

    for bird in birds:
        bird.desenhar(tela) #desenhar pássaros
    
    for pipe in pipes:
        pipe.desenhar(tela) #desenhar canos
    
    texto = fontes.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    if ia_jogando:
        texto2 = fontes.render(f"Geração: {geracao}", 1, (255, 255, 255))
        tela.blit(texto2, (0, 10)) #desenha o texto
        texto3 = fontes.render(f"Pássaros: {len(birds)}", 1, (255, 255, 255))
        tela.blit(texto3, (0, 60)) #desenha o texto

    tela.blit(texto, (win_width - 10 - texto.get_width(), 10)) #desenha o texto

    base.desenhar(tela)
    pygame.display.update()

list_genomas_reserva = []
redes_reserva = []
melhores_redes = []
geracao_consecutiva = 0

def start(genomas, redes_atualizadas):
    Pipe.vel_move = 4

    global geracao
    geracao +=1

    #instanciando as classes e criando variáveis
    if ia_jogando:
        redes = []
        list_genomas = []
        birds = []
        tx_mut = 0.03
        global list_genomas_reserva
        global redes_reserva
        global melhores_redes
        global geracao_consecutiva
        x = 40
        for genoma in genomas:
            #rede = neat.nn.FeedForwardNetwork.create(genoma, config)
            if redes_atualizadas == None:
                rede = rede_neural.rede_neural()
            else:
                rede = ag.mutacao(redes_atualizadas, tx_mut)
            redes.append(rede)
            rede = None
            genoma.fitness = 0 
            list_genomas.append(genoma)
            birds.append(Bird(x, 350))
            x +=2
                
        for rede in redes:
            #print(rede[1])
            pass

    else:
        birds = [Bird(100, 400)]
    base = Base(500)
    pipes = [Pipe(300),Pipe(500),Pipe(700), Pipe(900), Pipe(1100)]
    tela = pygame.display.set_mode((win_width, win_height))
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    desce = True
    contador_desce = 0
    contador_cano = 0
    

    while rodando:
        
        for bird in birds:
            if not bird.dash_disponivel:
                bird.recarga_dash -=1

            if bird.recarga_dash == 0:
                bird.dash_disponivel = True
                bird.recarga_dash = 250

        relogio.tick(30)
        #fechar a janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            #pulo do pássaro
            if not ia_jogando:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for bird in birds:
                            bird.jump()
                    if event.key == pygame.K_z:
                        for bird in birds:
                            if bird.dash_disponivel:
                                bird.dash()
                                bird.dash_disponivel = False
    
        indice_pipe = 0
        if len(birds) > 0:
            for bird in birds:
                if len(pipes) > 1 and birds[0].pos_x > (pipes[0].pos_x + pipes[0].img_top.get_width()):
                    indice_pipe = 1
        else:
            rodando = False
            break

        contador_cano +=1
        #movimentação do pássaro
        ##AQUI RECEBE INFO E DECIDE SE PULA OU NAO
        for i, bird in enumerate(birds):
            bird.move()

            list_genomas[i].fitness +=0.1

            #output = redes[i].activate((bird.pos_y, abs(bird.pos_y - pipes[indice_pipe].altura), abs(bird.pos_y - pipes[indice_pipe].pos_base)))
            output = rede_neural.calcula_ativacao(dist_x=(bird.pos_y - pipes[indice_pipe].altura), 
                                                     dist_y=abs(bird.pos_y - pipes[indice_pipe].pos_base),
                                                     bias=redes[i][0],
                                                     pesos=redes[i][1])
            if output > 0.6:
                bird.jump()
            elif output >0.3 and output <=0.6:
                if bird.dash_disponivel:
                    bird.dash()
                    bird.dash_disponivel = False
            
        #movimentação do chão
        base.move()

        
        #movimentação dos canos
        add_pipe = False
        remove_pipes = []

        for pipe in pipes:
            for i, bird in enumerate(birds):
                #verifica colisores passaro e cano
                if pipe.colider(bird):
                    if ia_jogando:
                        birds.pop(i)
                        
                        list_genomas[i].fitness -=1
                        list_genomas_reserva.append(list_genomas[i].fitness)
                        list_genomas.pop(i)
                        
                        redes_reserva.append(redes[i])
                        redes.pop(i)
                    else:
                        birds.pop(i)
                    
                #verifica se o passaro ja passou do cano
                if not pipe.passou and (bird.pos_x > pipe.pos_x):
                    pipe.passou = True
                    # aumenta velocidade
                    #Pipe.vel_move+=0.2
                    #if Pipe.vel_move >= 10:
                    #    Pipe.vel_move = 10
                    add_pipe = True
                    

            #if desce: 
            #    contador_desce +=1
#
            #    pipe.pos_base +=1
            #    pipe.pos_top +=1
            #    if contador_desce == 170:
            #        contador_desce = 0
            #        desce = False
            #else:
            #    contador_desce +=1
#
            #    pipe.pos_base -=1
            #    pipe.pos_top -=1
            #    if contador_desce == 170:
            #        contador_desce = 0
            #        desce = True
            
            

            pipe.move()
            if pipe.pos_x + pipe.img_top.get_width() < 0:
                remove_pipes.append(pipe)
        
        if add_pipe:
            pontos += 1
            if contador_cano >= 300:
                contador_cano = 0
                pipes.append(PipePequeno(1100))
                print("cano pequeno")
            else:
                pipes.append(Pipe(1100))
            
            if ia_jogando:
                for genoma in list_genomas:
                    genoma.fitness +=5
        
        for pipe in remove_pipes:
            pipes.remove(pipe)

        
        for i, bird in enumerate(birds):
            if (bird.pos_y + bird.img.get_height()) > 500 or bird.pos_y < 0:
                birds.pop(i)
                if ia_jogando:
                    list_genomas.pop(i)
                    redes.pop(i)
        
        for i, bird in enumerate(birds):
            #print("nuero de passaros -", len(birds))
            #print(f"passaro {i} pontuou:", list_genomas[i].fitness) 
            pass
        if birds == []:
            rede_nova = None
            for i, rede in enumerate(redes_reserva):
                #print(f"rede {i} - ",redes_reserva[i][1])
                pass
            if len(list_genomas_reserva) > 1 and len(redes_reserva) > 1:
                
                #if len(melhores_redes) >4:
                #    melhores_redes_aux = melhores_redes[len(melhores_redes) -1]
                #    melhores_redes.clear()
                #    melhores_redes.append(melhores_redes_aux)
                
                pai1, pai2 = ag.selecao(list_genomas_reserva)

                rede_nova = ag.cruzamento(redes_reserva[pai1], redes_reserva[pai2])

                #if random.random() < tx_mut:    
                
                with open("melhor_rede.txt", "w") as mr:
                    mr.write(str(rede_nova))

                #melhores_redes.append(rede_nova)
            
                #list_genomas_reserva.clear()
                #redes_reserva.clear()
                
            rodar(rede_nova)  
        desenhar_tela(tela, birds, pipes, base, pontos)
            
        

def rodar(rede):

    
    if ia_jogando:
        populacao = rede_neural.Genoma.start_população(30)
        start(genomas=populacao, redes_atualizadas = rede)
    else:
        start(None, None)
