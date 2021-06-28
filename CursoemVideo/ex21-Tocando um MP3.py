import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer_music.load('ex21-Tocando um MP3.mp3')
pygame.mixer_music.play()
pygame.event.wait()

#Método antigo--- não funcionou
#from playsound import playsound

#playsound.playsond('ex21-Tocando um MP3.mp3')'''


#Funciona, porém ele roda a música no Groove
#import webbrowser

#webbrowser.open('ex21-Tocando um MP3.mp3')'''
