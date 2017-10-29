import pygame, sys

from pygame.locals import *

class Player(pygame.sprite.Sprite):

    """Clase para el jugador, sin parametros inicializadores"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bloke = pygame.image.load("sprites/player.png")
        self.rect = self.bloke.get_rect()
        self.rect.centerx = 670
        self.rect.centery = 670
        self.fast = 20

    def dibujar (self, window):
        window.blit(self.bloke, self.rect)

    def movimientoDerecha(self, x):
        self.rect.centerx = x

class Blocke(pygame.sprite.Sprite):
    """Clase para el blocke de la pared completa"""
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.color = pygame.image.load(color)
        self.rect = self.color.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def paint(self, window):
        window.blit(self.color, self.rect)

class Ball(pygame.sprite.Sprite):
    """clase para la bola"""
    def __init__(self):
        self.ball = pygame.image.load("sprites/ball.png")
        self.rect = self.ball.get_rect()
        self.rect.centerx = 670
        self.rect.centery = 670
        self.bounce = pygame.mixer.Sound("sounds/bounce.wav")

    def paint(self, window):
        window.blit(self.ball, self.rect)

    def move(self, x , y):
        self.rect.centerx = x
        self.rect.centery = y

    def sound(self):
        self.bounce.play()
