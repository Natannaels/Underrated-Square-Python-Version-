import pygame              

# BARRA OBSTACULO
class DeathBar:
    def __init__(self,x,y,largura, altura, veloc=3.5, cor=(31,66,98),right = True):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.veloc = veloc
        self.cor = cor
        self.right = right

        self.move_direction = self.veloc
        self.move_counter = 0

    def draw(self, tela):
        return pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura)) 

    #Movimento na horizontal
    def move(self, limite_x1, limite_x2):
        if self.x < limite_x1 or self.x > limite_x2: #se a posicao do inimigo for maior que o limite
            self.right = not self.right              #o argumento right é negado e ele nao continua
        if self.right:                               # enquanto righ for true ele se movimenta para direita
            self.x += self.veloc
        else:                                        # se nao ele movimenta para esquerda
            self.x -= self.veloc

    def move2(self, limite_y1, limite_y2):
        if self.y < limite_y1 or self.y > limite_y2: 
            self.right = not self.right             
        if self.right:                               
            self.y += self.veloc
        else:                                        
            self.y -= self.veloc
            
            
#ESFERA
class DeathSphere:
    def __init__(self,x,y,largura, altura, veloc=2.5, cor=(255,0,0),right = True, x_veloc = 10, y_veloc = 10):#propriedades do inimigo
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.veloc = veloc
        self.cor = cor
        self.right = right
        self.x_veloc = x_veloc 
        self.y_veloc = y_veloc

    def draw(self, tela):
        return pygame.draw.circle(tela, self.cor, (self.x, self.y), self.largura, self.altura)
        
    #Movimento na horizontal
    def move(self, limite_x1, limite_x2):
        if self.x < limite_x1 or self.x > limite_x2: #se a posicao do inimigo for maior que o limite
            self.right = not self.right              #o argumento right é negado e ele nao continua
        if self.right:                               # enquanto righ for true ele se movimenta para direita
            self.x += self.veloc
        else:                                        # se nao ele movimenta para esquerda
            self.x -= self.veloc
    #movimento na vertical
    def move2(self, limite_y1, limite_y2):
        if self.y < limite_y1 or self.y > limite_y2: #se a posicao do inimigo for maior que o limite
            self.right = not self.right              #o argumento right é negado e ele nao continua
        if self.right:                               # enquanto righ for true ele se movimenta para direita
            self.y += self.veloc
        else:                                        # se nao ele movimenta para esquerda
            self.y -= self.veloc
            
    #movimento ricochete
    def move3(self):
        self.x += self.x_veloc
        self.y += self.y_veloc
        
        if self.x >= 630 or self.x <= 100 :
            self.x_veloc *= -1
        if self.y >= 420 or self.y <= 150 :
            self.y_veloc *= -1
    
