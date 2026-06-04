import pygame

pygame.init()

#caracteristicas da tela e inicializaçao
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
font = pygame.font.Font('fontpixel.ttf',20)

#tela de inicializacao do jogo
def tela_inicial():     
        campoImage = pygame.image.load('../telas/startmenu.png')
        Start_sound = pygame.mixer.Sound('../Ost/start_sound1.wave')
        while True:
            tela.blit(campoImage, (0,0))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                Start_sound.play()
                pygame.time.delay(900)                          
                main_menu()
        return tela_inicial()

#tela do menu principal
def main_menu():
        cursor = Cursor(200, 340, 20,20)
        pygame.mixer.music.load('../Ost/thefiregone.wave')
        pygame.mixer.music.play(-1)
        campoImage = pygame.image.load('../telas/load_start.png')
        
        while True:
            tela.blit(campoImage, (0,0))
            '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
             '''       
            cursor.move()
            cursor.draw(tela)
            
            iniciar = font.render("INICIAR", False, (255,255,255))
            tela.blit(iniciar,(240,340))

            controles= font.render("CONTROLES", False, (255,255,255))
            tela.blit(controles,(240,390))

            sair = font.render("SAIR", False, (255,255,255))
            tela.blit(sair,(240,440))

            pygame.display.update()

            
        return main_menu()

#tela de loadind (desnecessaria, porem legal)
def load_screen():
        campoImage = pygame.image.load('../telas/load_start.png')
        load = 0

        while True:
            pygame.time.delay(50)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            tela.blit(campoImage, (0,0))
            pygame.draw.rect(tela, (255,255,0), (250,500, load, 30))
            load += 20
              
            pygame.display.update()
            if load >= 300 :
                pygame.mixer.music.stop()
                import level1 as level1                              #evito importaçao circular
                level1.alterna_level()
        return load_screen()

#tela de descricao dos controles
def tela_controles():
        campoImage = pygame.image.load('../telas/telacontroles.png')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            tela.blit(campoImage, (0,0))
            pygame.display.update()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:           
                main_menu()
        return tela_controles()

#TELA DE GAME OVER
def game_over():
        Start_sound = pygame.mixer.Sound('../Ost/start_sound1.wave')
        music = pygame.mixer.music.load('../Ost/sonicgameover.wave')
        pygame.mixer.music.play()
        campoImage = pygame.image.load('../telas/gameover.png')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            tela.blit(campoImage, (0,0))
            pygame.display.update()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                pygame.mixer.music.stop()
                Start_sound.play()
                import level1 as level1                              #evito importaçao circular
                level1.alterna_level()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:  
                Start_sound.play()         
                main_menu()
        return game_over()

#tela de nova habilidade adiquirida 1
def habilidade1():
        Start_sound = pygame.mixer.Sound('../Ost/start_sound1.wave')
        music = pygame.mixer.music.load('../Ost/thefiregone.wave')
        pygame.mixer.music.play()
        campoImage = pygame.image.load('../telas/habilidade1.png')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            tela.blit(campoImage, (0,0))
            pygame.display.update()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                pygame.mixer.music.stop()
                Start_sound.play() 
                import level3 as level3                              #evito importaçao circular
                level3.alterna_level()
        return habilidade1()

#tela de nova habilidade adiquirida 2
def habilidade2():
        Start_sound = pygame.mixer.Sound('../Ost/start_sound1.wave')
        music = pygame.mixer.music.load('../Ost/thefiregone.wave')
        pygame.mixer.music.play()
        campoImage = pygame.image.load('../telas/habilidade2.png')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            tela.blit(campoImage, (0,0))
            pygame.display.update()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                pygame.mixer.music.stop()
                Start_sound.play() 
                import level5 as level5                              #evito importaçao circular
                level5.alterna_level()
        return habilidade1()

#FIM DA PARTIDA 
def fim():     
        campoImage = pygame.image.load('../telas/fim.png')
        Start_sound = pygame.mixer.Sound('../Ost/start_sound1.wave')

        while True:
            tela.blit(campoImage, (0,0))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                Start_sound.play()
                pygame.time.delay(900)                          
                tela_inicial()
        return fim()

#CURSOR DO MENU
class Cursor():

    def __init__(self,x,y,largura, altura, cor=(255,0,0)):

        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def move(self):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                #controle do cursor
                if event.key == pygame.K_UP and self.y > 340 + self.altura :
                    self.y = self.y-50   

                if event.key == pygame.K_DOWN and self.y < 420:
                    self.y = self.y+50 

                #verifica a posicao do cursor e se apertou espaco
                if self.y == 340 and event.key == pygame.K_SPACE :
                    import screen_manager as screen_manager
                    screen_manager.load_screen()
                    
                if self.y == 390 and event.key == pygame.K_SPACE :
                    import screen_manager as screen_manager
                    screen_manager.tela_controles()

                if self.y == 440 and event.key == pygame.K_SPACE :
                    exit()
               
            if event.type == pygame.QUIT:
                    exit()
                              
    def draw(self, tela):
        pygame.draw.rect(tela, (139, 0, 0), (self.x-2, self.y-2, self.largura+4, self.altura+4))
        return pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))
 