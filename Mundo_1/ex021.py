#Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

# Inicializando o mixer do Pygame
pygame.mixer.init()

# Carregando o arquivo MP3
pygame.mixer.music.load('musica.mp3')

# Dando o play
pygame.mixer.music.play()

# Comando para manter o programa aberto enquanto a música toca
input('Aperte Enter para parar a música...')