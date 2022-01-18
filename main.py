import pygame
from sys import exit
from pygame.locals import *
from pygame.transform import flip
import random
from pygame import mixer

'''
Gostaríamos de dar créditos ao canal "Coding With Russ",
pois nos ajudou no inicio com muitos algoritmos e serviu de base para a continuação do projeto.

https://www.youtube.com/watch?v=Ongc4EVqRjo&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu - Esta é a playlist

'''

'''
Caso queira diminuir a dificuldade do boss, na linha 911 isso é possivel,
alterando o valor para 1, fazendo-o morrer com 1 hit (colocar um numero > 10 resultará em um bug).
Mas recomendamos a experiência completa, apesar de muito dificil
'''
##### settings
pygame.init()
volume = 0.3
screen_width = 1344
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Megaman')
clock = pygame.time.Clock()
scroll = [0, 0]
#####
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.image = pygame.image.load('assets/Bullet/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        self.shoot = False
        
    def update(self):   
        self.rect.x += ((self.direction * self.speed)* -1)
        if self.rect.right < 0 or self.rect.left > screen_width:
            self.rect.x = -10
            self.rect.y = -10
            self.kill()
            
        
    
        

######## mundo
background = pygame.image.load('assets/sky.png').convert()
background = pygame.transform.scale(background, (5376, 768))
tile_size = 48
class Mundo():
    def __init__(self, data):
        self.tile_list = []
        self.tile_list2 = []
        self.porta = []
        self.porta_backup = []
        self.cooldown = 0
        self.fechar = False
        self.fim = False
        self.restart = []
        

        # load images
        def image_(arquivo):
            return pygame.image.load('assets/assets/'+arquivo+'.png').convert()

        row_count = 0

        def tile_(valor, image):
            if elem == valor:
                img = image
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                img_rect.y = row_count * tile_size
                tile = (img, img_rect)
                self.tile_list.append(tile)
            return
        def tile__(valor, image):
            if elem == valor:
                img = image
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                img_rect.y = row_count * tile_size
                tile = (img, img_rect)
                self.tile_list2.append(tile)
            return
        def porta(valor, image):
            if elem == valor:
                img = image
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                img_rect.y = row_count * tile_size
                tile = (img, img_rect)
                self.porta.append(tile)
                self.restart.append(tile)
            return

        for linha in data:
            col_count = 0
            for elem in linha:
                tile_(4, image_('plataforma'))
                tile_(5, image_('plataforma1'))
                tile_(6, image_('plataforma2'))
                tile_(10, image_('estrada0'))
                tile_(11, image_('estrada1'))
                tile_(12, image_('estrada2'))
                tile_(16, image_('estrada3'))
                tile_(18, image_('estrada5'))
                porta(8,image_('entrada'))
                tile__(41,image_('bloco_verde'))
                tile__(35,image_('bloco_verde_preto'))
                tile__(29, image_('cabo_esquerdo'))
                tile__(19,image_('bola0'))
                tile__(20,image_('bola1'))
                tile__(21,image_('bola2'))
                tile__(22,image_('bola3'))
                tile__(28,image_('bola4'))
                tile__(34,image_('bola5'))
                tile__(40,image_('bola6'))
                tile__(39,image_('bola7'))
                tile__(38,image_('bola8'))
                tile__(37,image_('bola9'))
                tile__(31,image_('bola10'))
                tile__(25,image_('bola11'))
                tile__(26,image_('bola_pequena0'))
                tile__(27,image_('bola_pequena1'))
                tile__(33,image_('bola_pequena2'))
                tile__(32,image_('bola_pequena3'))
                tile__(30,image_('cabo_direito'))
                tile__(17,image_('estrada4'))
                tile__(36,image_('bola_meio'))
                tile__(23,image_('cabo_pequeno_esquerdo'))
                tile__(24,image_('cabo_pequeno_direito'))
                tile__(1,image_('preto'))
                
                
                
                

                col_count += 1
            row_count += 1

    def draw(self):
        
            
        for tile in self.tile_list:
            screen.blit(tile[0], (tile[1][0]- scroll[0], tile[1][1] - scroll[1]))
        for tile in self.tile_list2:
            screen.blit(tile[0], (tile[1][0]- scroll[0], tile[1][1] - scroll[1]))
        for tile in self.porta:
            screen.blit(tile[0], (tile[1][0]- scroll[0], tile[1][1] - scroll[1]))
        if jogador.cutscene and self.fim == False:
            self.cooldown += 1
            if self.cooldown == 200:
                self.cooldown = 0
                jogador.cutscene = False
                jogador.andar_sozinho = True
                
            if self.cooldown == 80 or self.cooldown == 160:
                jogador.boss_gate.play()
                self.porta_backup.append(self.porta[-1])
                self.porta.pop()
                self.porta_backup.append(self.porta[-1])
                self.porta.pop()
        if self.fechar:
            self.fim = True
            jogador.cutscene = True
            pygame.mixer.music.unload()
            jogador.andar_sozinho = False
            self.cooldown += 1
            if self.cooldown == 80 or self.cooldown == 160:
                jogador.boss_gate.play()
                self.tile_list.append(self.porta_backup[-1])
                self.porta_backup.pop()
                self.tile_list.append(self.porta_backup[-1])
                self.porta_backup.pop()
            if self.cooldown == 200:
                jogador.cutscene = False
                self.fechar = False
            
            
world_data = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,16,18,5,5,5,5,16,17,17,18,5,5,5,5,5,5,5,5,16,17,17,18,5,5,5,5,16,18],
    [2,2,2,2,2,2,19,20,21,22,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,16,18,5,5,5,5,16,17,17,18,5,5,5,5,5,5,5,5,16,17,17,18,5,5,5,5,16,18],
    [2,2,2,2,2,2,25,36,36,28,2,2,2,2,2,2,2,19,20,21,22,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,19,20,21,22,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,16,18,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,16,18],
    [2,2,2,2,2,2,31,36,36,34,2,2,2,2,2,2,2,25,36,36,28,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,25,36,36,28,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,19,20,21,22,2,2,2,2,16,18,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,18],
    [2,2,2,2,2,2,37,38,39,40,2,2,19,20,21,22,2,31,36,36,34,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,31,36,36,34,2,2,19,20,21,22,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,25,36,36,28,2,2,2,2,16,18,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,18],
    [19,20,21,22,2,2,2,29,30,2,2,2,25,36,36,28,2,37,38,39,40,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,37,38,39,40,2,2,25,36,36,28,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,19,20,21,22,2,2,31,36,36,34,2,2,2,2,16,18,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,18],
    [25,36,36,28,2,2,2,29,30,2,2,2,31,36,36,34,2,2,29,30,19,20,21,22,2,10,11,11,12,2,2,2,2,19,20,21,22,2,2,29,30,2,2,2,31,36,36,34,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,25,36,36,28,2,2,37,38,39,40,2,2,2,2,16,18,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,18],
    [31,36,36,34,2,2,2,29,30,2,2,2,37,38,39,40,2,2,29,30,25,36,36,28,2,16,17,17,18,2,2,2,2,25,36,36,28,2,2,29,30,2,2,2,37,38,39,40,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,31,36,36,34,2,2,2,29,30,2,2,2,2,2,16,18,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,18],
    [37,38,39,40,2,2,2,29,30,26,27,2,2,29,30,2,2,2,29,30,31,4,5,5,5,16,17,17,18,5,6,2,2,31,36,36,34,2,2,29,30,26,27,2,2,29,30,2,2,2,2,10,12,2,2,2,2,2,2,2,10,12,2,2,2,2,2,2,10,12,2,2,2,2,2,2,10,12,2,2,2,2,37,38,39,40,2,2,2,29,30,2,2,2,2,2,16,18,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,18],
    [2,29,30,2,2,26,27,29,30,32,33,26,27,29,30,2,2,2,29,30,37,4,5,5,5,16,17,17,18,2,2,2,2,37,38,39,40,26,27,29,30,32,33,26,27,29,30,2,2,2,2,16,18,2,2,2,2,2,2,2,16,18,2,2,2,2,2,2,16,18,2,2,2,2,2,2,16,18,2,2,2,2,2,29,30,2,10,12,2,29,30,26,27,26,27,2,16,18,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,18],
    [2,29,30,2,2,32,33,29,30,23,24,32,33,29,30,2,2,4,5,5,5,5,5,5,5,16,17,17,18,5,5,5,6,2,29,30,2,32,33,29,30,23,24,32,33,29,30,2,2,4,5,16,18,2,2,2,2,4,5,5,16,18,2,2,2,2,4,5,16,18,2,2,2,2,4,5,16,18,2,2,2,2,2,29,4,5,16,18,2,29,30,32,33,32,33,2,8,8,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,18],
    [2,29,30,2,2,23,24,29,30,23,24,23,24,29,30,2,2,2,29,30,2,29,30,2,2,16,17,17,18,5,5,5,6,2,29,30,2,23,24,29,30,23,24,23,24,29,30,2,2,4,5,16,18,2,2,2,2,2,2,2,16,18,2,2,2,2,4,5,16,18,2,2,2,2,2,2,16,18,2,2,2,2,2,29,30,2,16,18,2,29,30,23,24,23,24,2,8,8,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,18],
    [5,5,5,5,5,10,11,11,12,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,16,17,17,18,5,5,5,5,5,5,5,5,10,11,11,12,5,5,5,5,5,5,5,5,5,5,16,18,2,2,4,5,5,5,5,16,18,2,2,4,5,5,5,16,18,2,2,4,5,5,5,16,18,2,2,4,5,5,5,5,5,16,18,5,5,5,5,5,5,5,5,10,12,5,5,5,5,10,11,11,12,5,5,5,5,5,5,5,5,10,11,11,12,5,5,5,5,16,18],
    [2,29,30,2,2,16,17,17,18,23,24,23,24,29,30,2,2,2,29,30,2,29,30,2,2,16,17,17,18,2,2,2,2,2,29,30,2,16,17,17,18,23,24,23,24,29,30,2,2,2,2,16,18,2,2,4,5,5,5,5,16,18,2,2,2,2,2,2,16,18,2,2,4,5,5,5,16,18,2,2,2,2,2,29,30,2,16,18,5,5,5,5,5,5,5,5,16,18,5,5,5,5,16,17,17,18,5,5,5,5,5,5,5,5,16,17,17,18,5,5,5,5,16,18],
    [5,5,5,5,5,16,17,17,18,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,16,17,17,18,5,5,5,5,5,5,5,5,16,17,17,18,5,5,5,5,5,5,5,5,5,5,16,18,2,2,2,2,2,2,2,16,18,2,2,4,5,5,5,16,18,2,2,2,2,2,2,16,18,2,2,4,5,5,5,5,5,16,18,5,5,5,5,5,5,5,5,16,18,5,5,5,5,16,17,17,18,5,5,5,5,5,5,5,5,16,17,17,18,5,5,5,5,16,18],
    [2,29,30,2,2,16,17,17,18,23,24,23,24,29,30,2,2,2,29,30,2,29,30,2,2,16,17,17,18,2,2,2,2,2,29,30,2,16,17,17,18,23,24,23,24,29,30,2,2,2,2,16,18,2,2,2,2,2,2,2,16,18,2,2,2,2,2,2,16,18,2,2,2,2,2,2,16,18,2,2,2,2,2,29,30,2,16,18,5,5,5,5,5,5,5,5,16,18,5,5,5,5,16,17,17,18,5,5,5,5,5,5,5,5,16,17,17,18,5,5,5,5,16,18]
]
mundo = Mundo(world_data)
########


######## player
class Jogador():
    def __init__(self, x, y):
        self.images_left = []
        self.images_right = []
        self.images_left_shooting = []
        self.images_right_shooting = []
        self.vida_images = []
        self.index = 0
        self.counter = 0
        for i in range(5):
            img_left = pygame.image.load(f'player/not shooting/megaman_run{i}.png').convert_alpha()
            img_right = pygame.transform.flip(img_left, True, False)
            self.images_left.append(img_left)
            self.images_right.append(img_right)
        for i in range(5):
            img_left_shooting = pygame.image.load(f'player/attacks/shooting_moving{i}.png').convert_alpha()
            img_right_shooting = pygame.transform.flip(img_left_shooting,True,False)
            self.images_left_shooting.append(img_left_shooting)
            self.images_right_shooting.append(img_right_shooting)
        
        self.image = self.images_left[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.pulando = True
        self.direction = -1
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.dano = False
        self.atirando = False
        self.ready_count = 0
        self.shoot_cooldown = 15
        self.counter_shooting = 0
        self.bullet = Bullet(self.rect.x - scroll[0],self.rect.y - scroll[1] + 35, self.direction)
        self.vida = 5
        self.index_vida = 0
        for i in range(6):
            self.vida_images.append(pygame.image.load(f'assets/vida/vida{i}.png').convert())
        self.vida_image = self.vida_images[self.index_vida]
        self.invencible = False
        self.invencible_contagem = 0
        self.alpha = 255
        self.cutscene = False
        self.andar_sozinho = False
        self.teleport = True
        self.resetar = False
        self.tocando = False
        
        ## sounds
        self.buster = pygame.mixer.Sound('sounds/05 - MegaBuster.wav')
        self.buster.set_volume(volume)

        self.land = pygame.mixer.Sound('sounds/06 - MegamanLand.wav')
        self.land.set_volume(volume)
        
        self.megaman_damage = pygame.mixer.Sound('sounds/07 - MegamanDamage.wav')
        self.megaman_damage.set_volume(volume)
        
        self.enegy_fill = pygame.mixer.Sound('sounds/24 - EnergyFill.wav')
        self.enegy_fill.set_volume(volume)
        
        self.enemy_damage = pygame.mixer.Sound('sounds/09 - EnemyDamage.wav')
        self.enemy_damage.set_volume(volume)
        
        self.megaman_defeat = pygame.mixer.Sound('sounds/08 - MegamanDefeat.wav')
        self.megaman_defeat.set_volume(volume)
        
        self.boss_gate = pygame.mixer.Sound('sounds/30 - BossGate.wav')
        self.boss_gate.set_volume(volume)
        
        self.explosion = pygame.mixer.Sound('sounds/13 - Explosion.wav')
        self.explosion.set_volume(volume)
        
        self.dink = pygame.mixer.Sound('sounds/11 - Dink.wav')
        self.dink.set_volume(1)
        

    def update(self):
        
        
            
        dx = 0
        dy = 0
        walk_cooldown = 8
        
        if self.invencible:
            self.invencible_contagem += 1
            if self.invencible_contagem % 2 == 1:
                self.alpha = 128
            else:
                self.alpha = 255
        else:
            self.alpha = 255
            
        if self.invencible_contagem == 100:
            self.invencible = False
            self.invencible_contagem = 0
        # keypresses
        botao = pygame.key.get_pressed()
        if self.cutscene == False and self.andar_sozinho == False and self.teleport == False and self.dano == False:
            if botao[pygame.K_a] and self.shoot_cooldown == 0:
                self.buster.play()
                self.shoot_cooldown = 20
                self.shoot = True
                self.counter_shooting +=1
                if self.direction == 1:
                    self.bullet = Bullet(self.rect.x - scroll[0],self.rect.y - scroll[1] + 35,self.direction)     
                else:
                    self.bullet = Bullet(self.rect.x - scroll[0] + 100,self.rect.y - scroll[1] + 35,self.direction)
                bullet_group.add(self.bullet)
            if botao[pygame.K_a]:
                self.atirando = True
            else:
                self.atirando = False
                
            
            
                
            if botao[pygame.K_LEFT] and botao[pygame.K_RIGHT]:
                self.index = 0  
            elif botao[pygame.K_RIGHT]:
                self.counter += 1 
                self.direction = -1
                if self.index == 0:
                    self.image = self.images_left[1]
                    self.counter = walk_cooldown + 1
                dx += 5
            elif botao[pygame.K_LEFT]:
                self.counter += 1 
                self.direction = 1
                if self.index == 0:
                    self.image = self.images_left[1]
                    self.counter = walk_cooldown + 1
                dx -= 5
                
            if botao[pygame.K_RIGHT] == False and botao[pygame.K_LEFT] == False and self.direction == 1:
                self.counter = 0
                self.index = 0
                self.image = self.images_left[self.index]
            if botao[pygame.K_RIGHT] == False and botao[pygame.K_LEFT] == False and self.direction == -1:
                self.counter = 0
                self.index = 0
                self.image = self.images_right[self.index]
        
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_left)-1:
                self.index = 1
            if self.direction == 1:
                self.image = self.images_left[self.index]
            if self.direction == -1:
                self.image = self.images_right[self.index]
        
        self.vel_y += 1.5
        if self.vel_y > 20:
            self.vel_y = 20
        dy += self.vel_y
        
        if self.andar_sozinho:
            self.counter += 1
            self.atirando = False
            dx += 2
    
        
        if self.atirando:
            if self.direction == 1:
                self.image = self.images_left_shooting[self.index]
            else:
                self.image = self.images_right_shooting[self.index]
        else:
            if self.direction == 1:
                self.image = self.images_left[self.index]
            else:
                self.image = self.images_right[self.index]
        
        if self.vel_y > 0 and self.vel_y != 1.5:
            self.pulando = True
        
        if self.dano:
            if self.direction == 1:
                dx += 7
                self.image = pygame.image.load('player/not shooting/megaman_hurt.png').convert_alpha()
            if self.direction == -1:
                dx -= 7
                self.image = pygame.transform.flip(pygame.image.load('player/not shooting/megaman_hurt.png').convert_alpha(), True, False)
        
        for tile in mundo.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.teleport = False
                if self.pulando:
                    self.land.play()
                    self.pulando = False
                self.dano = False
    
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                if self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                if botao[pygame.K_z] and self.cutscene == False and self.andar_sozinho == False:
                    self.vel_y -= 22
                    self.pulando = True
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                self.index = 0
                if self.dano == False:
                    if self.direction == 1:
                        if self.atirando:
                            self.image = self.images_left_shooting[self.index]
                        else:
                            self.image = self.images_left[self.index]
                    elif self.direction == -1:
                        if self.atirando:
                            self.image = self.images_right_shooting[self.index]
                        else:
                            self.image = self.images_right[self.index]
        
        if self.dano == False:
            if self.pulando and self.direction == 1:
                if self.atirando:
                    self.image = self.images_left_shooting[-1]
                else:
                    self.image = self.images_left[-1]
                
            elif self.pulando and self.direction == -1:
                if self.atirando:
                    self.image = self.images_right_shooting[-1]
                else:
                    self.image = self.images_right[-1]
            
        for tile in mundo.porta:
            
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                self.cutscene = True
        
        self.rect.x += dx
        self.rect.y += dy
        
        if self.rect.x < 604 or self.rect.x > 3964 and self.rect.x <= 4700:
            pass
        elif self.rect.x > 4700:
            scroll[0] += 4708 - scroll[0] - 100
        else:
            scroll[0] += self.rect.x - scroll[0] - 604
        
        if self.rect.x <= 0:
            self.rect.x = 0
        
        if self.rect.x > 4730 and len(mundo.tile_list) != 497:
            mundo.fechar = True

        
        if self.rect.top > screen_height:
            self.index_vida = 5
                
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        
        if boss.alive:
            if self.rect.x <= 4730:
                self.rect.x = 4730
            elif self.rect.x >= 5770:
                self.rect.x = 5770
            if self.rect.y <= 96:
                self.rect.y = 95
                
        if self.teleport:
            self.pulando = False
            self.image = pygame.image.load('player/teleport.png').convert_alpha()
        else:
            if self.tocando == False:
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(volume)
                self.tocando = True
            
        self.image.set_alpha(self.alpha)       
        
        screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))
        
        
        
        if self.rect.bottom <= 0:
            self.ready_count += 1
            if self.ready_count < 40:
                screen.blit(pygame.image.load('assets/assets/ready.png').convert_alpha(), (pygame.image.load('assets/assets/ready.png').convert_alpha().get_rect(center=(screen_width/2, screen_height/2))))
            elif self.ready_count == 80:
                self.ready_count = 0
        

    def vida_update(self):
        if self.index_vida >= 5:
            self.megaman_defeat.play()
            self.index_vida = 5
            pygame.mixer.music.unload()
            died_screen()
            
        self.vida_image = self.vida_images[self.index_vida]
        if self.teleport == False:
            screen.blit(self.vida_image, (100, 115))
        
jogador = Jogador(310, -3500)
########

######## inimigos
class Enemy():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.x = x
        self.y = y
        self.image = pygame.image.load('enemies/enemy1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contador = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.alive = True
        self.drop_item = False
        self.atirando = False
        self.contador2 = 0
        self.bullet = 'bala'
        self.direction = -1
        self.direction_bullet = -1
        for num in range(1,3):
            img_right = pygame.image.load(f'enemies/enemy{num}.png').convert_alpha()
            img_left = pygame.transform.flip(img_right,True,False)
            self.images_left.append(img_left)
            self.images_right.append(img_right)
        
        

        
    def draw(self):
        if self.alive and jogador.teleport == False and jogador.cutscene == False and jogador.andar_sozinho == False:
            self.contador += 1
            
            if self.contador == 80:
                if self.index == 1:
                    self.index = 0
                    self.rect.y += 10
                    
                else:
                    self.rect.y -= 10
                    self.index = 1
                self.contador = 0
            
            if jogador.rect.x < self.rect.x:
                self.direction = -1
                self.image = self.images_right[self.index]
            else:
                self.direction = 1
                self.image = self.images_left[self.index]
            
            
              
            if self.index == 1:
                if self.atirando == False:
                    if (self.direction == 1 and jogador.rect.x - self.rect.x < 700) or (self.direction == -1 and self.rect.x - jogador.rect.x < 700) or (jogador.rect.x < 620 and ((self.direction == 1 and jogador.rect.x - self.rect.x < 1344) or (self.direction == -1 and self.rect.x - jogador.rect.x < 1344))):
                        self.bullet = enemy_bullet(self.rect.x, self.rect.y)
                        self.direction_bullet = self.direction
                        self.atirando = True
                    
           
            if self.atirando:
                self.contador2 += 1
                if self.contador2 == 100:
                    self.bullet.kill = True
                    self.contador2 = 0
                    self.atirando = False
                    
            
              
            if jogador.rect.colliderect(self.rect) and jogador.invencible == False:
                jogador.megaman_damage.play()
                jogador.index_vida += 1
                jogador.invencible = True
                jogador.dano = True
                jogador.rect.y = self.rect.top - 73
                jogador.vel_y = -10
            
            if jogador.bullet.rect.colliderect(self.rect.x - scroll[0], self.rect.y - scroll[1], self.width, self.height):
                jogador.bullet.rect.x = -10
                jogador.bullet.rect.y = -10
                jogador.bullet.kill()
                if self.index == 1:
                    jogador.enemy_damage.play()
                    if random.randint(0, 3) == 3:
                        self.drop_item = True
                    self.alive = False
                else:
                    jogador.dink.play()  
            screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))   
        elif self.drop_item:
            self.image = pygame.image.load('assets/vida/vidaup.png').convert_alpha()
            if jogador.rect.colliderect(self.rect) and jogador.index_vida > 0:
                jogador.enegy_fill.play()
                jogador.index_vida -= 1
                self.drop_item = False
            screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))
            
        if self.bullet != 'bala':
            self.bullet.rect.x += 14 * self.direction_bullet
            self.bullet.update() 
            
        
class Enemy_():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.image = pygame.image.load('enemies/enemy2/enemy0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contador = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.alive = True
        self.direction = 1
        self.vida = 5
        self.vel_y = 0
        for num in range(3):
            img_left = pygame.image.load(f'enemies/enemy2/enemy{num}.png').convert_alpha()
            img_right = pygame.transform.flip(img_left,True,False)
            self.images_left.append(img_left)
            self.images_right.append(img_right)
        self.drop_item = False
        
    def draw(self):
        if self.alive and jogador.teleport == False and jogador.cutscene == False and jogador.andar_sozinho == False:
            dx = 0
            dy = 0
                    
                
            self.contador += 1
            
            
            if self.contador == 8:
                if self.index == 0:    
                    self.index = 1    
                elif self.index == 1:
                    self.index = 2  
                else:
                    self.index = 0
                self.contador = 0
            
            if self.direction == 1:
                self.image = self.images_left[self.index]
                dx -= 3
            else:
                self.image = self.images_right[self.index]
                dx += 3
            
                     
            self.vel_y += 1.5
            if self.vel_y > 10:
                self.vel_y = 10
                
            for tile in mundo.tile_list:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y - 50, self.width, self.height):
                    dx = 0
                    if self.direction == 1:
                        self.image = self.images_left[self.index]
                        self.direction = -1
                        
                    else:
                        self.image = self.images_left[self.index]
                        self.direction = 1
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    self.vel_y = 0    
                    
            dy += self.vel_y
            
            self.rect.y += dy
                
            self.rect.x += dx
                
            if jogador.rect.colliderect(self.rect) and jogador.invencible == False:
                jogador.megaman_damage.play()
                if jogador.invencible == False:
                    jogador.index_vida += 1
                    jogador.invencible = True
                jogador.dano = True
                jogador.rect.y = self.rect.top - 73
                jogador.vel_y = -10
            
            if jogador.bullet.rect.colliderect(self.rect.x - scroll[0], self.rect.y - scroll[1], self.width, self.height):
                jogador.enemy_damage.play()
                jogador.bullet.rect.x = -10
                jogador.bullet.rect.y = -10
                jogador.bullet.kill()
                self.vida -= 1
            
            if self.vida == 0:
                self.alive = False
                if random.randint(0, 3) == 3:
                    self.drop_item = True
                
            
            screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))
        
        if self.drop_item:
            self.image = pygame.image.load('assets/vida/vidaup.png').convert_alpha()
            if jogador.rect.colliderect(self.rect) and jogador.index_vida > 0:
                jogador.enegy_fill.play()    
                jogador.index_vida -= 1
                self.drop_item = False
            screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y + 50))
class Boss():
    def __init__(self, x, y):
        self.images_left = []
        self.images_right = []
        self.vida_images = []
        self.index = 0
        for i in range(4):
            img_left = pygame.image.load(f'bomber man/idle{i}.png').convert_alpha()
            self.images_left.append(img_left)
            img_right = pygame.transform.flip(img_left,True,False)
            self.images_right.append(img_right)
        self.image = self.images_left[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.pulando = False
        self.direction = -1
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.dano = False
        self.atirando = False
        self.victory = False
        self.alive = False
        self.invencible = False
        self.invc_cooldown = 0
        self.jumped = False
        self.pular_cooldown = 0
        self.jumped2 = False
        self.bullet = self.bullet = boss_bullet(self.rect.x, self.rect.y)  
        self.bullet_cooldown = 0
        self.index_vida = 0
        self.alpha = 255
        self.anim = False
        self.tocando = False
        
        
        for i in range(1, 12):
            self.vida_images.append(pygame.image.load(f'assets/vida/vida_boss{i}.png').convert())
        self.vida_image = self.vida_images[self.index_vida]
    def update(self):
        if self.alive:
            if self.tocando == False:
                pygame.mixer.music.load('Soundtracks/09 Boss Battle.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(volume)
                self.tocando = True
            dx = 0
            dy = 0
            
            if self.invencible:
                self.invc_cooldown += 1
                if self.invc_cooldown % 2 == 0:
                    self.alpha = 128
                else:
                    self.alpha = 255
            else:
                self.alpha = 255
            
            if self.invc_cooldown == 100:
                self.invencible = False
                self.invc_cooldown = 0
            
            
            
            self.vel_y += 1.5
            dy += self.vel_y
            
            if self.jumped:
                self.rect.x += 12 * self.direction
            if self.jumped2:
                self.rect.x += 5 * self.direction
                
            for tile in mundo.tile_list:
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
        
                    self.pular_cooldown += 1
                    self.pulando = False
                    self.dano = False
                    self.jumped = False
                    self.jumped2 = False
            
                    
                        
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    if self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                    if jogador.rect.x > self.rect.x:
                        if self.pular_cooldown == 60:
                            self.vel_y -= 30
                            self.jumped2 = True
                            self.pular_cooldown = 0
                            self.pulando = True
                        elif jogador.rect.x - self.rect.x < 100:
                            self.vel_y -= 30
                            self.jumped = True
                            self.pulando = True
                        self.direction = 1              
                    elif self.rect.x > jogador.rect.x:
                        if self.pular_cooldown == 60:
                            self.vel_y -= 30
                            self.jumped2 = True
                            self.pular_cooldown = 0
                            self.pulando = True
                        elif self.rect.x - jogador.rect.x < 100 :
                            self.vel_y -= 30
                            self.jumped = True
                            self.pulando = True
                        self.direction = -1
                
                if self.direction == -1:
                    self.image = self.images_left[self.index]
                    if self.bullet.kill:
                        if self.pulando:
                            self.index = 2
                        else:
                            self.index = 0
                    else:
                        self.index = 1
                else:
                    self.image = self.images_right[self.index]
                    if self.bullet.kill:
                        if self.pulando:
                            self.index = 2
                        else:
                            self.index = 0
                    else:
                        self.index = 1
                
                
                
                    
                
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_left[self.index]
                    if self.direction == -1:
                        self.image = self.images_right[self.index]
            
            if jogador.rect.colliderect(self.rect) and jogador.invencible == False:
                jogador.megaman_damage.play()
                if jogador.invencible == False:
                    jogador.index_vida += 2
                    jogador.invencible = True
                jogador.dano = True
                jogador.rect.y = self.rect.top - 73
                jogador.vel_y = -10
            
        
            
            
            
            self.rect.x += dx
            self.rect.y += dy
            
            if self.rect.x <= 4730:
                self.rect.x = 4730
            elif self.rect.x >= 5760:
                self.rect.x = 5760
    
            if jogador.bullet.kill:
                self.bullet_cooldown += 1  

            if self.bullet_cooldown == 70:
                self.bullet = boss_bullet(self.rect.x, self.rect.y + 10)
                if boss.pulando:
                    self.bullet.dx = True
                else:
                    self.bullet.dx = False
                self.bullet.boss_direction = self.direction
                self.bullet_cooldown = 0
            
            
            if jogador.bullet.rect.colliderect(self.rect.x - scroll[0], self.rect.y - scroll[1], self.width, self.height) and self.invencible == False:
                jogador.enemy_damage.play()
                jogador.bullet.rect.x = -10
                jogador.bullet.rect.y = -10
                jogador.bullet.kill()
                
                self.index_vida += 1
                self.invencible = True
                self.vida_image = self.vida_images[self.index_vida]
                if self.index_vida == 10:
                    self.alive = False
                    self.rect.y = 200
                    self.vel_y = 0
                    self.victory = True
                    jogador.cutscene = True
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load('Soundtracks/10 Victory!.mp3')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(volume)
                
            self.bullet.update()
        
            self.image.set_alpha(self.alpha)
            screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y))
            screen.blit(self.vida_image, (148, 115))
        elif self.victory:
            self.image = pygame.image.load('bomber man/power_upgrade.png').convert_alpha()
            self.rect.x = 5250
            dy = 3
            if self.vel_y >= 20:
                self.vel_y = 20
            if jogador.rect.x >= 4800 and self.anim == False:
                jogador.rect.x -= 4
                jogador.counter += 1
                jogador.direction = 1
                if self.index == 0:
                    self.image = self.images_left[1]
            elif jogador.rect.x < 4800 and self.anim == False:
                jogador.rect.x += 4
                jogador.counter +=1
                jogador.direction = -1
                if self.index == 0:
                    self.image = self.images_right[1]
            if 4801 > jogador.rect.x >= 4796:
                self.anim = True
                jogador.cutscene = False
                jogador.counter = 0
                jogador.direction = -1
            if self.anim:      
                for tile in mundo.tile_list:
                    if tile[1].colliderect(self.rect.x, self.rect.y - 70, self.width, self.height):
                        dy = 0
                
                if jogador.rect.colliderect(self.rect):
                    self.victory = False
                    victory_screen()
                    
                
                self.rect.y += dy     
                
                screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y))   
class boss_bullet():
    def __init__(self, x, y):
        self.image = pygame.image.load('bomber man/bomb0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.atirar = True
        self.kill = False
        self.vel_y = 0
        self.dx = False
        self.boss_direction = -1
        self.bomba_explosion = 0
        self.nao_mexe = False
        
        
        
    def update(self):
        
        if self.kill == False:
            dy = 0
            
            
            
            self.vel_y += 1.5
            
            for tile in mundo.tile_list:
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.width != 123:
                        self.rect.y -= 50
                    self.vel_y = 0
                    self.nao_mexe = True
                    dy = 0
                    self.bomba_explosion += 1
                    self.image = pygame.image.load('bomber man/explosion2.png').convert_alpha()
                    self.rect[2] = 123
                    self.rect[3] = 123
                    self.height = self.rect[3]
                    self.width = self.rect[2]
                    
                    
                    if self.bomba_explosion == 100:
                        self.kill = True
                        self.bomba_explosion = 0
                    jogador.explosion.play()
                    
                
            
            if jogador.rect.colliderect(self.rect) and jogador.invencible == False:
                jogador.megaman_damage.play()
                if jogador.invencible == False:
                    jogador.index_vida += 2
                    jogador.invencible = True
                jogador.dano = True
                jogador.rect.y = self.rect.top - 73
                jogador.vel_y = -10
                    
            
            
            if self.vel_y > 20:
                self.vel_y = 20
            
            if self.atirar and boss.pulando == False:
                self.vel_y -= 30
                self.atirar = False
            elif self.atirar and boss.pulando:
                self.vel_y -= 15
                self.atirar = False
                
            dy += self.vel_y
            
            self.rect.y += dy
            if self.nao_mexe == False:
                if self.dx:
                    self.rect.x -= -14 * self.boss_direction
                else:
                    self.rect.x -= -10 * self.boss_direction
            screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y))

class enemy_bullet():
    def __init__(self, x, y):
        self.image = pygame.image.load('enemies/enemy_bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 20
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.atirar = True
        self.kill = False
        self.vel_y = 0
        self.dx = False
        self.boss_direction = -1
        self.bomba_explosion = 0
        self.nao_mexe = False
        
        
        
    def update(self):
        
        if self.kill == False  and jogador.cutscene == False and jogador.andar_sozinho == False:
            if jogador.rect.colliderect(self.rect) and jogador.invencible == False:
                self.kill = True
                jogador.megaman_damage.play()
                if jogador.invencible == False:
                    jogador.index_vida += 1
                    jogador.invencible = True
                jogador.dano = True
                jogador.rect.y = self.rect.top - 73
                jogador.vel_y = -10
                    

            

            screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y))      

boss = Boss(5700, 500)
enemy3 = Enemy_(1332, 197)      
enemy4 = Enemy_(2000, 485)
enemy5 = Enemy_(4300, 485)
enemy6 = Enemy(1113, 353)
enemy8 = Enemy(923, 449)
enemy10 = Enemy(2463, 353)
enemy11 = Enemy(2778, 449)
enemy12 = Enemy(2898, 353)
enemy13 = Enemy(3183, 449)
enemy14 = Enemy(3568, 449)
enemy15 = Enemy(3663, 353)
enemy16 = Enemy(4143, 401)
enemy17 = Enemy(4053, 449)
enemy18 = Enemy(3943, 545)



bullet_group = pygame.sprite.Group()

###########

def main_menu():
    img0 = pygame.image.load('title screen/title_screen0.png').convert()
    img1 = pygame.image.load('title screen/title_screen1.png').convert()
    pygame.mixer.music.load('Soundtracks/01 Stage Select.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)
    i = 0
    while True:
        i += 1
        if i < 30:
            img = img0
        else:
            img = img1
        if i == 60:
            i = 0
        screen.blit(img, (280,-20))        
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    main_game()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(60)

def died_screen():
    global scroll, jogador, boss, enemy3, mundo, enemy4, enemy5, enemy6, enemy8, enemy10, enemy11, enemy12, enemy13, enemy14, enemy15, enemy16, enemy17, enemy18
    scroll = [0, 0]
    pygame.mixer.music.load('Soundtracks/03 Password.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)
    
    while len(mundo.porta) != 4:
        for i in mundo.restart:
            mundo.porta.append(i)
    while len(mundo.tile_list) != 493:
        mundo.tile_list.pop()

    jogador = Jogador(310, -3500)
    boss = Boss(5700, 500)
    enemy3 = Enemy_(1332, 197)      
    enemy4 = Enemy_(2000, 485)
    enemy5 = Enemy_(4300, 485)
    enemy6 = Enemy(1113, 353)
    enemy8 = Enemy(923, 449)
    enemy10 = Enemy(2463, 353)
    enemy11 = Enemy(2778, 449)
    enemy12 = Enemy(2898, 353)
    enemy13 = Enemy(3183, 449)
    enemy14 = Enemy(3568, 449)
    enemy15 = Enemy(3663, 353)
    enemy16 = Enemy(4143, 401)
    enemy17 = Enemy(4053, 449)
    enemy18 = Enemy(3943, 545)
    mundo.cooldown = 0
    mundo.fim = False
    
    
    img0 = pygame.image.load('title screen/died.png').convert()
    img1 = pygame.image.load('title screen/died1.png').convert()
    i = 0
    while True:
        i += 1
        if i < 40:
            img = img0
        else:
            img = img1
        if i == 80:
            i = 0
        screen.fill((0,112,236))
        screen.blit(img, (280,-20))        
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    main_game()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(60)
def victory_screen():
    pygame.mixer.music.unload()
    pygame.mixer.music.load('Soundtracks/15 Epilogue.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)
    
    while True:
        screen.blit(pygame.image.load('assets/assets/end.png').convert(), (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.quit()
                    exit()
        
        pygame.display.update()
        clock.tick(60)
    

###### jogo
def main_game():
    pygame.mixer.music.unload()
    pygame.mixer.music.load('Soundtracks/05 Bomb Man.mp3')  
    pygame.mixer.music.set_volume(0)

    while True:
        
        screen.blit(background, (0, 0))

        mundo.draw()
        
        bullet_group.update()
        
        bullet_group.draw(screen)
        
        enemy6.draw()
        enemy8.draw()  
        enemy10.draw()
        enemy11.draw()
        enemy12.draw()
        enemy13.draw()
        enemy14.draw()
        enemy15.draw()
        enemy16.draw()
        enemy17.draw()
        enemy18.draw()
        enemy3.draw()
        enemy4.draw()
        enemy5.draw()
        
        jogador.update()
        
        jogador.vida_update()
        
        
        if jogador.rect.x > 4930 and boss.index_vida == 0:
            boss.alive = True
    
        
        boss.update()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)

main_menu()
######