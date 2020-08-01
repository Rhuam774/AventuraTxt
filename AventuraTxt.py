#codigo: utf-8

import cidade
import deserto
import PacoteTxt1
from os import system
import sys
from time import sleep
import random


def lin (txt):
    print('******************************************************************************************************************')
    print(txt)
    print('******************************************************************************************************************\n')
def tempo(tempo, mensagem):
    aaa = tempo
    bbb = 0
    while aaa > bbb:
        print(f'\n{mensagem} {aaa}')
        sleep(1)
        aaa -= 1
        system('cls')

lin('Olá, esse jogo e um jogo de aventura atraves de texto, você e o personagem principal e terá de fazer as escolhas.')

nome = input('Qual e seu nome aventureiro? ')
system('cls')
tempo(3, 'Iremos começar em:')
system('cls')
#############################################################################################################################

escolha_automatica_de_fazes = random.choice(['cidade'])

if escolha_automatica_de_fazes == 'cidade':
    cidade.Cidade()
elif escolha_automatica_de_fazes == 'deserto':
    deserto.Deserto()
else:
    print('erro ao escolher a fase.')
