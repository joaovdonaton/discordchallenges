#O desafio de gerar números random sem o uso de métodos é até que simples.
#O Python (tanto o 3 quanto o 2) possuí uma biblioteca chamada datetime, que vem
#com alguns métodos para pegar o tempo atual, até mesmo em microsegundos. 
from datetime import time, datetime, timedelta

#Outra solução pro problema pode ser através do process ID do programa:
from os import getpid

#Você também pode usar alguma biblioteca para fazer requests HTTP e usar alguma API
#para gerar números aleatorios.
#Pseudo Código:
# resp = HTTP.get('http://api.rand.com.br/gerarnum')
# print(resp.text)