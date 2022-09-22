import pygame
from pygame.locals import *
from sys import exit
from random import randint

# CRIAR TELA E VARIAVEIS:

pygame.init()

width = 640
height = 480

x_snake = int(width / 2)
y_snake = int(height / 2)

speed = 10
x_control = speed
y_control = 0

x_apple = randint(40, 600)
y_apple = randint(50, 430)

score = 0
font = pygame.font.SysFont('arial', 20, bold=True, italic=True)

tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo da cobrinha')
relogio = pygame.time.Clock()
list_snake = []
initial_size = 5
dead = False

# esta funcao desenha o corpo da cobra
def increase_snake(list_snake):
    for XeY in list_snake:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


def reiniciar_jogo():
    global score, initial_size, x_snake, y_snake, list_snake, list_head, x_apple, y_apple, dead
    score = 0
    initial_size = 5
    x_snake = int(width / 2)
    y_snake = int(height / 2)
    list_snake = []
    list_head = []
    x_apple = randint(40, 600)
    y_apple = randint(50, 430)
    dead = False


while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))

    mensagem = f'Pontos: {score}'
    texto_formatado = font.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

# CONTROLAR A CABEÇA DA COBRA

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == speed:
                    pass
                else:
                    x_control = -speed
                    y_control = 0
            if event.key == K_d:
                if x_control == -speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0
            if event.key == K_w:
                if y_control == speed:
                    pass
                else:
                    y_control = -speed
                    x_control = 0
            if event.key == K_s:
                if y_control == -speed:
                    pass
                else:
                    y_control = speed
                    x_control = 0

    x_snake = x_snake + x_control
    y_snake = y_snake + y_control

# ADICIONAR COBRA E FRUTA, vulgo quadrados :p:

    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(tela, (255, 0, 0), (x_apple, y_apple, 20, 20))

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        score += 1
        initial_size = initial_size + 1

    list_head = []
    list_head.append(x_snake)
    list_head.append(y_snake)

    list_snake.append(list_head)

    if list_snake.count(list_head) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()

        dead = True
        while dead:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (width // 2, height // 2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

# condiçao para cobra não sumir da tela (sai de um lado e aparece do outro)

    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width
    if y_snake < 0:
        y_snake = height
    if y_snake > height:
        y_snake = 0

    if len(list_snake) > initial_size:
        del list_snake[0]

    increase_snake(list_snake)

    tela.blit(texto_formatado, (450, 40))

    pygame.display.update()