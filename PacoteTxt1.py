#codigo: utf-8

from os import system
import sys
from time import sleep
import random

class pessoa():
    def __init__(self, nome):
        self.nome = nome

    def correndo(self):
        velocidade = 10
