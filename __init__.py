import pygame, sys
from clases import *
from pygame.locals import *
#inicializacion de pygame
pygame.init()
pygame.display.set_caption("Breakout")#titulo de la ventana

#variables para el color de la pantalla, y de los contadores del juego
white = (0, 0, 0)

#variables de la medida de la pantalla, y de las fuentes usadas
window = pygame.display.set_mode((1300,720))
fuente = pygame.font.Font("fonts/acknowtt.ttf", 150)
fuente_2 = pygame.font.Font("fonts/emulogic.ttf",20)
fuente_3 = pygame.font.Font("fonts/acknowtt.ttf", 120)

#sonidos del juego
lose = pygame.mixer.Sound("sounds/lose.wav")

#objetos de texto para el menu
titulo = fuente.render("BreakOut", 2, (200, 11, 11))
press = fuente_2.render("press any key to play", 0, (200, 11, 11))

#tupla contenedora de los archivos de los bloques
colors = ("sprites/blok1.png", "sprites/blok2.png", "sprites/blok3.png", "sprites/blok4.png", "sprites/blok5.png", "sprites/blok6.png", "sprites/blok7.png")
icon = pygame.image.load("sprites/icon.png")
pygame.display.set_icon(icon)
blockes = []# lista de bloques que conforman la pared del juego

#rectangulos que forman los limites del juego
rectangulo = pygame.Rect(23,90,25,600)
rectangulo_2 = pygame.Rect(23, 90, 1255, 25)
rectangulo_3 = pygame.Rect(1253, 90, 25, 600)
rectangulo_4 = pygame.Rect(23, 690, 25, 20)
rectangulo_5 = pygame.Rect(1253, 690, 25, 20)

def anotherBrickInTheWall():
    """funcion para construir la pared del juego"""
    ancho = 88
    alto = 200
    for x in range(7):
        for y in range(15):
            blok = Blocke(ancho, alto, colors[x])
            blockes.append(blok)
            ancho += 81
        alto += 25
        ancho = 88

jugador = Player()                               #se inicializa el jugador
ball = Ball()                                    # se inicializa la bola
anotherBrickInTheWall()                          # se contrulle la pared

def game():
    sco = 0
    level_i = 1
    level ="1"
    life_i = 3
    life = "3"
    lev, lev2, lev3 = True, True, True
    title = True
    up , down , left, right= True, True, False, True
    life_one, life_two, life_three = True, True, True
    game = fuente_3.render("GAME OVER", 0, (255, 255, 255))
    #begin.play()
    while True:
        window.fill(white)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        while title == True:                      # ciclo para el menu
            window.blit(press,(425, 300))
            window.blit(titulo,(350, 190))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    title = False

        #rutina de niveles
        if sco > 100 and lev == True:
            level_i += 1
            level = str(level_i)
            lev = False
        elif sco > 180 and lev2 == True:
            level_i += 1
            level = str(level_i)
            lev2 = False
        elif sco > 300 and lev3 == True:
            level_i += 1
            level = str(level_i)
            lev3 = False

        if sco < 10:
            scr = "oo{}". format(sco)             # condiciones para el contador de puntos
            score = fuente_3.render(scr, 0 , (255, 255, 255))
        if sco >= 10:
            scr = "o{}". format(sco)
            score = fuente_3.render(scr, 0 , (255, 255, 255))
        if sco >= 100:
            scr = "{}". format(sco)
            score = fuente_3.render(scr, 0 , (255, 255, 255))

        xp, yp = pygame.mouse.get_pos()# se pasa como parametro la posicion en x del mouse
        lv = fuente_3.render(level, 0, ( 255, 255, 255))
        lf = fuente_3.render(life, 0, (255, 255, 255))

        #impresion de los puntos, de las vidas y del nivel en el que se esta
        window.blit(score,(350,0))
        window.blit(lv, (940, 0))

        #se pasa como parametro las cordenadas en x del mouse para el objeto jugador
        jugador.movimientoDerecha(xp)
        jugador.dibujar(window)

        #rutina para detectar colicion con bloque
        for bk in blockes:
            if bk.rect.colliderect(ball):
                if up == True and right == True and ball.rect.centerx > bk.rect.centerx - 40 and ball.rect.centerx < bk.rect.centerx + 40:
                    ball.sound()
                    up = False
                    down = True

                elif up == True and right == True and ball.rect.centery > bk.rect.centery - 15 and ball.rect.centery < bk.rect.centery + 15:
                    ball.sound()
                    right = False
                    left = True

                elif up == True and left == True and ball.rect.centerx > bk.rect.centerx - 40 and ball.rect.centerx < bk.rect.centerx + 40:
                    ball.sound()
                    up = False
                    down = True

                elif up == True and left == True and ball.rect.centery > bk.rect.centery - 15 and ball.rect.centery < bk.rect.centery + 15:
                    ball.sound()
                    left = False
                    right = True

                elif down == True and left == True and ball.rect.centerx > bk.rect.centerx - 40 and ball.rect.centerx < bk.rect.centerx + 40:
                    ball.sound()
                    down = False
                    up = True

                elif down == True and left == True and ball.rect.centery > bk.rect.centery - 15 and ball.rect.centery < bk.rect.centery + 15:
                    ball.sound()
                    left = False
                    right = True

                elif down == True and right == True and ball.rect.centerx > bk.rect.centerx - 40 and ball.rect.centerx < bk.rect.centerx + 40:
                    ball.sound()
                    down = False
                    up = True

                elif down == True and right == True and ball.rect.centery > bk.rect.centery - 15 and ball.rect.centery < bk.rect.centery + 15:
                    ball.sound()
                    right = False
                    left = True

                blockes.remove(bk)
                sco += 4

        for bk in blockes:#impresion de la pared
            bk.paint(window)

         #limites del juego pintados de gris
        pygame.draw.rect(window,(179,179,179), rectangulo)
        pygame.draw.rect(window,(179,179,179), rectangulo_2)
        pygame.draw.rect(window,(179,179,179), rectangulo_3)
        pygame.draw.rect(window,(25, 9, 255), rectangulo_4)
        pygame.draw.rect(window,(255, 9, 9), rectangulo_5)

        #condiciones para el rebote entre paredes
        if up == True and right == True and ball.rect.centerx <= 1240 and ball.rect.centery >= 120:
            ball.rect.centerx += 10
            ball.rect.centery -= 10
            if ball.rect.centerx == 1240:
                ball.sound()
                right = False
                left = True

            if ball.rect.centery == 120:
                ball.sound()
                up = False
                down = True

        elif up == True and left == True and ball.rect.centerx >= 50 and ball.rect.centery >= 120:
            ball.rect.centerx -= 10
            ball.rect.centery -= 10
            if ball.rect.centerx == 50:
                ball.sound()
                left = False
                right = True

            if ball.rect.centery == 120:
                ball.sound()
                up = False
                down = True

        elif down == True and left == True and ball.rect.centerx >= 50 and ball.rect.centery <= 720:
            ball.rect.centerx -= 10
            ball.rect.centery += 10
            if ball.rect.centerx == 50:
                ball.sound()
                left = False
                right = True
            #condiciones para rebote entre lados del jugador
            if ball.rect.centerx >= jugador.rect.centerx - 60 and ball.rect.centerx <= jugador.rect.centerx and ball.rect.centery == 650:
                #print("side 1")
                ball.sound()
                up = True
                down = False
            if ball.rect.centerx >= jugador.rect.centerx and ball.rect.centerx <= jugador.rect.centerx + 60 and ball.rect.centery == 650:
                ball.sound()
                #print("side 2")
                up = True
                down = False
                left = False
                right = True


        elif down == True and right == True and ball.rect.centerx <= 1240 and ball.rect.centery <= 720:
            ball.rect.centerx += 10
            ball.rect.centery += 10
            if ball.rect.centerx == 1240:
                ball.sound()
                right = False
                left = True
            
            #condiciones para rebote entre lados del jugador
            if ball.rect.centerx >= jugador.rect.centerx and ball.rect.centerx <= jugador.rect.centerx + 60 and ball.rect.centery == 650:
                ball.sound()
                #print("side 2")
                up = True
                down = False
            if ball.rect.centerx >= jugador.rect.centerx - 60 and ball.rect.centerx <= jugador.rect.centerx and ball.rect.centery == 650:
                #print("side 1")
                ball.sound()
                up = True
                down = False
                right = False
                left = True

        elif life_i < 4 and life_one == True:
            lose.play()
            life_one = False
            life_i -= 1
            life = str(life_i)
            ball.rect.centery, ball.rect.centerx = 670, 330
            down, up, left, right = False, True, True, False

        elif life_i < 3 and life_two == True:
            lose.play()
            life_two = False
            life_i -= 1
            life = str(life_i)
            ball.rect.centery, ball.rect.centerx = 670, 830
            down, up, right, left = False, True, True, False

        elif life_i < 2 and life_three == True:
            lose.play()
            life_three = False
            life_i -= 1
            life = str(life_i)
            ball.rect.centery, ball.rect.centerx = 670, 530
            down, up, left, right = False, True, True, False
        else:

            window.blit(game, (350, 190))
            down, right, left = False, False, False

        ball.paint(window)
        window.blit(lf, (800, 0))
        pygame.display.update()

if __name__ == '__main__':
    game()
