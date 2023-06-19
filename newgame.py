from typing import Any
import pygame
import sys
import random
import os
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH = 800
HEIGHT = 700

#BACKGROUND=pygame.transform.scale(pygame.image.load('Assets/lo.jpg'), (WIDTH, HEIGHT))


#BACKGROUND_SOUND = pygame.mixer.play('Assets/romeo.mp3')
#BACKGROUND_SOUND.play()

arial = pygame.font.Font(None,12)
class Button():
	def __init__(self, image, pos, text_input, font=arial, base_color=BLACK, hovering_color=WHITE):
		self.image = image
		self.x = pos[0]
		self.y = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect()

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect, self.rect) and position[1] in range(self.rect, self.rect):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect, self.rect) and position[1] in range(self.rect, self.rect):
			self.text = self.font(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THEY SEE ME ROWLING")
clock = pygame.time.Clock()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.groups = all_sprites #if making another sprite, use this
        pygame.sprite.Sprite.__init__(self,self.groups) #and this
        self.image = pygame.image.load("Assets/t.png")
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.speed_x = -1
        self.speed_y = -1
        self.x = random.randint(0,WIDTH)
        self.y = random.randint(0,HEIGHT)
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self) -> None:
        self.x = self.rect.x
        self.y = self.rect.y
        if pygame.time.get_ticks() % 100000 < 50000:
            if random.randint(0,3):
                self.speed_x = -1.05
            else:
                self.speed_y = random.randint(-1,1)
        else:
            self.speed_y = 2
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > HEIGHT:
            self.rect.y = 0
        elif self.rect.bottom < 0:
            self.rect.y = HEIGHT
        if self.rect.left > WIDTH:
            self.rect.x = 0
        elif self.rect.right < 0:
            self.rect.x = WIDTH

class Car(pygame.sprite.Sprite):
    def __init__(self):
        self.groups = all_sprites #if making another sprite, use this
        pygame.sprite.Sprite.__init__(self,self.groups) #and this
        self.image = pygame.image.load("Assets/police.png")
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.speed_x = 0
        self.speed_y = 0
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.rect.x = self.x 
        self.rect.y = self.y

    def update(self):
        
        self.movement()
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.x = self.rect.x
        self.y = self.rect.y
        self.speed_x = 0
        self.speed_y = 0
        
    def movement(self):
        self.rect.y += self.speed_y
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:  # LEFT
            self.speed_x = -1
            self.image = pygame.transform.rotate(self.image,270)
        if keys_pressed[pygame.K_d]:  # RIGHT
            self.speed_x = 1
        if keys_pressed[pygame.K_w]:  # UP
            self.speed_y = -1
        if keys_pressed[pygame.K_s]:  # DOWN
            self.speed_y = 1
        if self.rect.top > HEIGHT:
            self.rect.y = 0
        elif self.rect.bottom < 0:
            self.rect.y = HEIGHT
        if self.rect.left > WIDTH:
            self.rect.x = 0
        elif self.rect.right < 0:
            self.rect.x = WIDTH
        

all_sprites = pygame.sprite.LayeredUpdates()


enemies = pygame.sprite.LayeredUpdates()
for _ in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
player_car = Car()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_car.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player_car.speed_x = 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_car.speed_x = 0

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player_car, enemies, False)
    #if hits:
     #running = False
    button = Button(pygame.image.load("Assets/beach.jpg"),(0,0),"Hello")
    window.fill((255, 255, 255))
    all_sprites.draw(window)
    pygame.display.update()