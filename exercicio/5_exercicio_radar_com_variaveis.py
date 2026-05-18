#==================================
# Exerciocio de Radar com Variaveis
#==================================

#dados das variaveis

velocidade = 100
local_carro = 100

RADAR_1 = 90 # velocidade maxima radar
LOCAL_1 = 90 # local radar
RADAR_RANGE = 1 #alcance radar


velocidade_do_carro = velocidade > RADAR_1

area_do_radar = (
    (LOCAL_1 - RADAR_RANGE)
    <= local_carro <= 
    (LOCAL_1 + RADAR_RANGE)
)

carro_multado = velocidade_do_carro and area_do_radar

if area_do_radar:
    print('O carro passou do radar...')
else:
    print('O carro não passou...')

if carro_multado:
    print('Voce foi multado')
else:
    print('O carro não foi multado')