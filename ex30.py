"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

fiscalizacao = velocidade > RADAR_1
range_antes = local_carro >= (LOCAL_1 - RADAR_RANGE)
range_apos = local_carro <= (LOCAL_1 + RADAR_RANGE)
atrevessou_fiscalizacao = range_antes and range_apos
multado = fiscalizacao and range_antes


if fiscalizacao:
    print('O carro passou da velocidade!')

if atrevessou_fiscalizacao:
    print('Atravessou o radar 1')

if multado:
    print('Multado por ultrapassar velocidade')