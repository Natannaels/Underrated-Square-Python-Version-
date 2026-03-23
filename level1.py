import pygame
import level2
import screen_manager
from player import Player
from enemy import DeathSphere
from campo import Campo

def alterna_level():
    pygame.init()

    pygame.display.set_caption("Underrated_Game")#titulo

    #caracteristicas da tela e inicializaçao
    largura_tela = 800
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    font = pygame.font.Font('fontpixel.ttf',15)

    fail_sound = pygame.mixer.Sound('Ost/failsound.wave')
    music = pygame.mixer.music.load('Ost/music1.wave')
    pygame.mixer.music.play(-1)

    #Objetos do jogo
    relogio = pygame.time.Clock()
    player = Player(150, 280, 10, 10 )
    enemy = DeathSphere(270, 200, 45, 45)
    enemy2 = DeathSphere(270, 390, 45, 45)
    enemy4 = DeathSphere(480, 295, 45, 45 )

    #Campos verdes de inicio e fim
    campoInicio = Campo(110,250,100,70,(112,128,144))
    campoFim = Campo(540,160,100,70,(173,255,47))

    #Desenho da borda branca
    size = (550,290)#tamanho da borda branca
    borda = pygame.Surface(size)#superficie borda branca
    pygame.draw.rect(borda, (255, 255, 255), borda.get_rect(), 7)  # desenha da borda

    #Atualizaçoes de tela
    def update():
        keys = pygame.key.get_pressed()
        player.move(keys)
        enemy.move(270,480)
        enemy2.move(270, 480)
        enemy4.move(270, 480)
      
        if player.draw(tela).collidelist([enemy.draw(tela), enemy2.draw(tela), enemy4.draw(tela)]) != -1:#teste de colisao
            fail_sound.play()
            pygame.time.delay(100)
            player.reset()
            player.mortes +=1
            player.vidas -=1        
          
        if player.draw(tela).collidelist([campoFim.draw(tela)]) != -1:
            next_level_sound = pygame.mixer.music.load('Ost/nextlevel.wave')
            pygame.mixer.music.play()
            pygame.time.delay(700)
            level2.alterna_level()
                   
    #desenhos dos objetos
    def draw():
        tela.fill(Player.fundo)
        tela.blit(borda, (100,150))
        campoInicio.draw(tela)
        campoFim.draw(tela)
        player.draw(tela)
        enemy.draw(tela)
        enemy2.draw(tela)
        enemy4.draw(tela)
        
        
        nivelAtual = font.render("NIVEL: " +str(1), False, (255,255,0))
        tela.blit(nivelAtual,(50,50))

        contVidas = font.render("VIDAS: " +str(player.vidas), False, (255,0,0))
        tela.blit(contVidas,(550,50))
      
        #DESENHO DAS BARRAS DE HABILIDADE
        contorno = pygame.Surface((108, 28))
        pygame.draw.rect(contorno, (255, 255, 255), contorno.get_rect(), 2)  

        #BARRA SLOW MOTION
        tela.blit(contorno, (297,45))
        slowmotion_stm = font.render("S: ", False, (255,0,255))
        tela.blit(slowmotion_stm,(255,50))
        #pygame.draw.rect(tela, (255,0,255), (300,50, Player.larg_stamina, 20))

        #BARRA DASH
        tela.blit(contorno, (297,87))
        dash_stm = font.render("D: ", False, (0, 157, 252))
        tela.blit(dash_stm,(255,90))
        #pygame.draw.rect(tela, (0, 157, 252), (300,90, Player.dash_stamina, 20))
        
        pygame.display.update()
    
    def level1():
        while True:

            relogio.tick(Player.fps)
            tela.fill((Player.fundo))
            #player.dash(tela)
            #player.slowmotion(tela)
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    exit()

            update()
            draw()

            if player.vidas==0:
                player.mortes-=4
                screen_manager.game_over()  
    level1()
