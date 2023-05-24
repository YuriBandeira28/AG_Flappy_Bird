import pygame
import os
import random
import time

win_height = 600 #altura
win_width = 1100 #largura
 
#carregando e alterando a escala das imagens
img_cano = pygame.transform.scale(size=(50,400),surface=pygame.image.load(os.path.join('imgs', 'pipe.png')))
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

    #atributos para o pássaro

    def __init__(self, pos_x , pos_y):

        self.pos_x = pos_x
        self.pos_y = pos_y
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

    def move(self):

        #deslocamento
        self.tempo += 1

        deslocamento = 1.5 * (self.tempo**2) + self.velociade * self.tempo

        #restringir o deslocamento
        if deslocamento > 10:
            deslocamento = 10

        elif deslocamento < 0:
            deslocamento -=2

        self.pos_y += deslocamento

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
        

class Pipe:
    
    dist = 130 #de um cano para o outro
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
        self.altura = random.randrange(20, 250)
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
    tela.blit(texto, (win_width - 10 - texto.get_width(), 10)) #desenha o texto

    base.desenhar(tela)
    pygame.display.update()

def start():


    #instanciando as classes e criando variáveis
    birds = [Bird(100, 250)]
    base = Base(500)
    pipes = [Pipe(300),Pipe(500),Pipe(700), Pipe(900), Pipe(1100)]
    tela = pygame.display.set_mode((win_width, win_height))
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(30)

        #fechar a janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            #pulo do pássaro
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for bird in birds:
                        bird.jump()

        #movimentação do pássaro
        for bird in birds:
            bird.move()

        #movimentação do chão
        base.move()

        
        #movimentação dos canos
        add_pipe = False
        remove_pipes = []
        for pipe in pipes:
            for i, bird in enumerate(birds):
                #verifica colisores passaro e cano
                if pipe.colider(bird):
                    birds.pop(i)
                    pygame.quit()
                    
                #verifica se o passaro ja passou do cano
                if not pipe.passou and bird.pos_x > pipe.pos_x:
                    pipe.passou = True
                    add_pipe = True

            pipe.move()
            if pipe.pos_x + pipe.img_top.get_width() < 0:
                remove_pipes.append(pipe)
        
        if add_pipe:
            pontos += 1
            pipes.append(Pipe(1100))
        
        for pipe in remove_pipes:
            pipes.remove(pipe)

        
        for i, bird in enumerate(birds):
            if (bird.pos_y + bird.img.get_height()) > 500 or bird.pos_y < 0:

                birds.pop(i)
                pygame.quit()
                 
        desenhar_tela(tela, birds, pipes, base, pontos)

