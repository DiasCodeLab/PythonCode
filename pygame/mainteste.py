#===========================================
# Pygame movimentando objeto para a esquerda
#===========================================

#importando biblioteca pygame
import pygame

#dando inicio ao codigo
pygame.init()

# função que retorna uma tela com determinada resolução.
def display():
    tela = pygame.display.set_mode((1280,720))
    return tela

#função que define a cor da tela display.
def cor_tela(tela):
    tela.fill("black")

#função que retorna um retangulo centralizado na tela. 
def retangulo():
    primeiro_retangulo = pygame.Rect(620,300,40,120)
    return primeiro_retangulo

#função que define a cor do retangulo centralizado na tela.
def cor_retangulo(display,primeiro_retangulo):
    pygame.draw.rect(display,"white",primeiro_retangulo)


#evento mover retangulo para a esquerda.
def retangulo_esquerda(eventos,primeiro_retangulo):
    if eventos.type == pygame.KEYDOWN:
        if eventos.key == pygame.K_a:
            primeiro_retangulo.x -= 10

#variaveis contendo funções
tela = display()
objeto_retangulo = retangulo()


#condiucao do laço de repetição whoile
loop = True

#laço de repetição para manipular funções
while loop:

    #atribuindo todos os eventos do pygame ao evento
    evento = pygame.event.get()

    #pegando os evento e listando todos para o eventos
    for eventos in evento:
        retangulo_esquerda(eventos,objeto_retangulo)
    
    # retornando a tela e sua cor ao usuario
    cor_tela(tela)

    #retornando o objeto retangulo na tela do usuario
    cor_retangulo(tela,objeto_retangulo)

    # atualizando os frames da tela do usuario.
    pygame.display.flip()

#finalizando codigo
pygame.quit()







