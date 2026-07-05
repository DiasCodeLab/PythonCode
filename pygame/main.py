import pygame

def tela_game():
    display = pygame.display.set_mode((1280,720))
    return display
 
def atualizar(display):
    display.fill((0,255,0))
    pygame.display.flip()

def botao_fechar(eventos,loop):
    if eventos.type == pygame.QUIT:
        loop = False
    return loop

def tecla_fechar(eventos,loop):
    if eventos.type == pygame.KEYDOWN:
        if eventos.key == pygame.K_a:
            loop = False
    return loop


loop = True

tela = tela_game()

while loop:

    evento = pygame.event.get()
    
    for eventos in evento:
        loop  = tecla_fechar(eventos,loop)
        loop =  botao_fechar(eventos,loop)
    
    atualizar(tela)

pygame.quit()
                
