#codigo: utf-8

from os import system
import sys
from time import sleep
import random
import re
def lin (txt):
    print('******************************************************************************************************************')
    print(txt)
    print('******************************************************************************************************************\n')
    sleep(3)
    system('cls')




def Cidade():
    lin('Você esta na cidade. Termine as frases.')
    sleep(2)
    system('cls')

    aaa = 1
    bbb = 0


    lin('\nVocê esta na sua casa, olhando pela janela você ver que e dia.')  # ds quer dizer decisão
    horario = (14.16)
    while aaa > bbb:

        ds1 = input('\nVocê esta na sua casa, você olha no relogio e são ' + str(horario) + ', você está em duvida se vai passear ou durmir, e então você resolve: ')  # ds quer dizer decisão

        if re.search('passear', ds1, re.IGNORECASE):
            lin('você sai pra passear!')
            ds2 = input('você sai pra passear mais fica tambem em duvida se vai pro parque ou vai pro shopping, depois de pensar você decide ir ao: ')
            if re.search('parque', ds2, re.IGNORECASE):
                lin('Agora voçe esta no parque!')
                print('No parque esta chato pois não tem ninguem, todos estão em casa com medo do corona virus (covid-19)\n')
                sleep(4)
                lin('Você faz alguns exercicios')
                sleep(3)
                ds3 = input('Depois de fazer exercicios você então pensa se vai pra casa ou pro shopping e decide ir: ')
                if re.search('casa', ds3, re.IGNORECASE):
                    lin('Você chegou em sua casa')
                    ds4 = input('Você chegou em casa, está cansado, quer ir tomar um bannho e dormir ou quer sair pra outro lugar? ')
                    if re.search('outro', ds4, re.IGNORECASE):
                        dsauto = random.choice(['Hoo não, você estava muito cansado e acabou batendo o carro por ter dormido no volante!','Você não conseguiu chegar até ao carro e acabou dormindo na sala de tanto cansaço!'])
                        lin(dsauto)
                        sys.exit()
                    else:
                        print('erro ortografico! :(')
                elif re.search('shopping', ds3, re.IGNORECASE):
                    lin('Agora você chega ao shopping!')
                    print('hoje o shopping está fechado por conta do corona virus(covid-19)!\n')
                    sleep(4)
                    print('Você está voltando pra casa')
                    system('cls')
                    horario += 3.43
                else:
                    print('erro ortografico! :(')
            elif re.search('shopping', ds2, re.IGNORECASE):
                lin('Agora você chega ao shopping!')
                print('hoje o shopping está fechado!')
                sleep(2)
                print('Você está voltando pra casa...')
                sleep(3)
                system('cls')
                dsauto3 = random.choice(['você acaba de chegar em casa muito cansado', 'Você estava indo pra casa quando derrepente a gasolina do carro acaba!'])
                if re.search('chegar', dsauto3, re.IGNORECASE):
                    lin(dsauto3)
                    lin('Você pensa em ir durmir e quando deita na cama você acorda e descobre que foi tudo um sonho')
                    sys.exit()
                elif re.search('acabou', dsauto3, re.IGNORECASE):
                    lin(dsauto3)
                    print(f'-- Hoo não, estou longe de casa e já é noite!\n')
                    ds5 = input('Por sorte há um posto á 300 metros! Você então pensa se *vai até ao posto* ou pensa em *fazer um ligação* pra um parente ou amigo trazer. Depois de pensar você decide: ')
                    if re.search('posto', ds5,re.IGNORECASE):
                        dsauto4 = random.choice(["""'Você vai até ao posto mais quando chega lá, se depara com ele fechado, pois o pessoal do posto está em quarentena por conta do covid-19""","""
                        Você foi até ao posto e comprou gasolina!"""])
                        if re.search('comprou', dsauto4, re.IGNORECASE):
                            lin(dsauto4)
                            lin('Você voltou pro carro com a gasolina, abasteceu e foi pra casa.')
                            lin('você está em casa!')
                            print('-- Estou cansado e vou durmir')
                            sleep(3)
                            lin('Você foi durmir e quando se deitou logo acordou e descobriu que foi tudo um sonho.')
                            lin('É fim.')
                            sys.exit()
                        elif re.search('fechado', dsauto4, re.IGNORECASE):
                            lin(dsauto4)
                            lin('voltando pro carro você e assautado e está sem celular! Chegando no carro você percebe que o vidro está quebrado e seu som foi levado!')
                            lin('Logo você acorda e percebe que foi apenas um pesadelo! uffa...')
                            sys.exit()
                    elif re.search('ligação', ds5, re.IGNORECASE):
                        lin('Você tenta fazer algumas ligações mais a bateria no celular acaba logo na 2 tentativa!')
                        print('--acho que terei que ir ao posto')
                        sleep(2)
                        dsauto5 = random.choice([ """'Você vai até ao posto mais quando chega lá, se depara com ele fechado, pois o pessoal do posto está em quarentena por conta do covid-19""", """
                                                Você vai até ao posto e compra gasolina."""])
                        if re.search('comprou', dsauto5, re.IGNORECASE):
                            lin(dsauto5)
                            lin('Você voltou pro carro com a gasolina, abasteceu e foi pra casa.')
                            lin('você está em casa!')
                            print('-- Estou cansado e vou durmir')
                            sleep(3)
                            lin('Você foi durmir e quando se deitou logo acordou e descobriu que foi tudo um sonho.')
                            lin('É fim.')
                            sys.exit()
                        elif re.search('fechado', dsauto5, re.IGNORECASE):
                            lin(dsauto5)
                            lin('voltando pro carro você e assautado e está sem celular! Chegando no carro você percebe que o vidro está quebrado e seu som foi levado!')
                            lin('Logo você acorda e percebe que foi apenas um pesadelo! uffa...')
                            sys.exit()
                else:
                    print('erro ortografico! :(')
            else:
                print('erro ortografico! :(')
        elif re.search('durmir', ds1, re.IGNORECASE):
            dsauto2 = random.choice(['Você tem bons sonho e acorda a noite!', 'Você não tem nem um sonho e acorda sem sono', 'Você não consegue dormir pois o som do visinho esta auto de mais'])
            lin(dsauto2)
            sleep(2)
            system('cls')
            horario += 2.23
        else:
            print('erro ortografico! :(')
