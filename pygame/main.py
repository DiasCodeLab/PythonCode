import pygame

def tela_game():
    display = pygame.display.set_mode((1280,720))
    return display
 
def cor(display):
    display.fill("black")

def botao_fechar(eventos,loop):
    if eventos.type == pygame.QUIT:
        loop = False
    return loop

def tecla_fechar(eventos,loop):
    if eventos.type == pygame.KEYDOWN:
        if eventos.key == pygame.K_a:
            loop = False
    return loop

def primeiro_jogador():
    player1 = pygame.Rect(0,0,30,150)
    return player1

def segundo_jogador():
    jogador2 = pygame.Rect(1250,0,30,150)
    return jogador2

def retangulo(display,player1,player2):
    pygame.draw.rect(display,"white",player1)   
    pygame.draw.rect(display,"white",player2)

loop = True


player1 = primeiro_jogador()
player2 = segundo_jogador()
tela = tela_game()

while loop:

    evento = pygame.event.get()
    
    for eventos in evento:
        loop  = tecla_fechar(eventos,loop)
        loop =  botao_fechar(eventos,loop)
    
    cor(tela)
    retangulo(tela,player1,player2)
    pygame.display.flip()

pygame.quit()


                
