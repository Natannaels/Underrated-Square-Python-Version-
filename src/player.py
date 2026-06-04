import pygame
from pygame.locals import *


class Player():
    fps = 60 # "fps" original
    fundo = (0,0,0) #fundo original
    larg_stamina = 100 #quantidade de stamina slow motion
    dash_stamina = 100 #quantidade stamina dash

    #ATRIBUTOS DO PLAYER
    def __init__(self,x,y,largura, altura, veloc=1.6, cor=(255,0,0), mortes = 0, vidas = 10):#propriedades do player

        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.veloc = veloc
        self.cor = cor
        self.mortes = mortes
        self.vidas = vidas

    #MOVIMENTO DO PLAYER
    def move(self, keys):
        
        if keys[pygame.K_LEFT] and self.x > 100 + self.largura:
            self.x -= self.veloc
        if keys[pygame.K_RIGHT] and self.x < 630:
            self.x += self.veloc
        if keys[pygame.K_DOWN] and self.y < 420:
            self.y += self.veloc
        if keys[pygame.K_UP] and self.y > 150 + self.altura:
            self.y -= self.veloc
                                 
    #CARACTERISTICAS ESTETICAS DO PLAYER            
    def draw(self, tela):
        pygame.draw.rect(tela, (139, 0, 0), (self.x-3, self.y-3, self.largura+5, self.altura+5))
        return pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))

    #RESET POS MORTE
    def reset(self):
        self.x = 150
        self.y = 280
        Player.larg_stamina = 100
        Player.dash_stamina = 100

    #MECANICA DASH
    def dash(self,tela):
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_TAB] and keys[pygame.K_RIGHT] and Player.dash_stamina >= 25 and self.x < 630:
            
            if Player.dash_stamina>= 100:
                pygame.mixer.Sound("../Ost/dashsound.wave").play()
            self.x  += 15  
            self.cor=(0, 157, 252)
            Player.dash_stamina -=25
            
        elif keys[pygame.K_TAB] and keys[pygame.K_LEFT] and Player.dash_stamina>= 25 and self.x > 100 + self.largura:
            if Player.dash_stamina >= 100:
                pygame.mixer.Sound("../Ost/dashsound.wave").play()
            self.x  -= 15
            self.cor=(0, 157, 252)
            Player.dash_stamina -=25

        elif keys[pygame.K_TAB] and keys[pygame.K_DOWN] and Player.dash_stamina >= 25 and self.y < 420:
            if Player.dash_stamina >= 100:
                pygame.mixer.Sound("../Ost/dashsound.wave").play()
            self.y += 15
            self.cor=(0, 157, 252)
            Player.dash_stamina -=25

        elif keys[pygame.K_TAB] and keys[pygame.K_UP] and Player.dash_stamina >= 25 and self.y > 150 + self.altura:
            if Player.dash_stamina >= 100:
                pygame.mixer.Sound("../Ost/dashsound.wave").play()
            self.y -= 15 
            self.cor=(0, 157, 252)
            Player.dash_stamina -=25
        
        elif not keys[pygame.K_TAB] and Player.dash_stamina <100:
                Player.dash_stamina += 10

        else : 
            self.cor = (255,0,0) 

    #MECANICA SLOW MOTION
    def slowmotion(self, tela):
        pygame.draw.rect(tela, (255,0,255), (300,50, Player.larg_stamina, 20))
        keys = pygame.key.get_pressed()

        #condicao para usar slow motion
        if keys[pygame.K_a] and Player.larg_stamina>=5 :
            
            if Player.larg_stamina==100 or Player.larg_stamina==10  :
                
                slowsound = pygame.mixer.Sound('../Ost/slowmotion.wave')
                slowsound.play()
            
            Player.larg_stamina -= 2
            self.veloc = 3.5 
            Player.fundo = (127,73,180)
            Player.fps = 8

        #crescimento da stamina apos uso
        elif Player.larg_stamina<100 :

            Player.larg_stamina += 0.1
            self.veloc = 1.6
            Player.fundo = (0,0,0)
            Player.fps = 60