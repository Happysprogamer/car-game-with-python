import pygame
import random
import tkinter
from tkinter import messagebox

def reset_game():
    global araba, araba_xhiz, araba_yhiz, engel, puan, score_text
    araba.center = (genislik/2, 600)
    araba_xhiz = 0
    araba_yhiz = 0
    engel.center = (random.randint(80, genislik-80), random.randint(-1000, -500))
    puan = 0
    score_text = font.render(f"Puan: {puan}", True, (0, 0, 0))
    pygame.mixer.music.play(-1)

pygame.init()
clock = pygame.time.Clock()
genislik = 500
yukseklik = 700
pencere = pygame.display.set_mode((genislik,yukseklik))
pygame.display.set_caption("Araba Yarışı")

puan = 0
font = pygame.font.SysFont("arial",20)
score_text = font.render(f"Puan: {puan}",True,(0,0,0))

yol = pygame.image.load("yol.png")
yol_pozisyon1 = [0,0]
yol_pozisyon2 = [0, -yukseklik]

araba_resim = pygame.image.load("araba.png")
araba = araba_resim.get_rect(center=(genislik/2,600))
araba_xhiz = 0
araba_yhiz = 0

engel_resim = pygame.image.load("engel.png")
engel = engel_resim.get_rect(center=(random.randint(80,genislik-80), random.randint(-1000,-500)))
engel_hiz = 15

pygame.mixer.init()
carpis_sound = pygame.mixer.Sound('C:/Users/Unal/Desktop/carpis.wav')
pygame.mixer.music.load('C:/Users/Unal/Desktop/surus.wav')
pygame.mixer.music.play(-1)

oyun = True
while oyun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                araba_xhiz = -10
            if event.key == pygame.K_RIGHT:
                araba_xhiz = 10
            if event.key == pygame.K_UP:
                araba_yhiz = -10
            if event.key == pygame.K_DOWN:
                araba_yhiz = 10
        if event.type == pygame.KEYUP:
            araba_xhiz = 0
            araba_yhiz = 0

    araba.x += araba_xhiz
    araba.y += araba_yhiz

    if araba.left <= 50:
        araba.left = 50
    if araba.right >= genislik-50:
        araba.right = genislik-50
    if araba.center[1] >= yukseklik:
        araba.center = (araba.center[0], 0)
    if araba.center[1] <= 0:
        araba.center = (araba.center[0], 0)

    yol_pozisyon1[1] += 20
    yol_pozisyon2[1] += 20
    if yol_pozisyon1[1] >= yukseklik:
        yol_pozisyon1[1] = -yukseklik
    if yol_pozisyon2[1] >= yukseklik:
        yol_pozisyon2[1] = -yukseklik

    engel.y += engel_hiz
    if engel.top >= yukseklik:
        engel.center = (random.randint(80,genislik-80), random.randint(-500,0))
        puan += 1
        score_text = font.render(f"Puan: {puan}", True, (0, 0, 0))

    if araba.colliderect(engel):
        pygame.mixer.Sound.play(carpis_sound)
        pygame.mixer.music.stop()
        pencere.fill((255,0,0))
        pygame.display.update()
        pygame.time.delay(500)
        res = messagebox.askyesno('Öldün', f'\tpuanın: {puan}.\n Yeniden başlamak ister misin?')
        if res:
            reset_game()
        else:
            oyun = False

    pencere.blit(yol, yol_pozisyon1)
    pencere.blit(yol, yol_pozisyon2)
    pencere.blit(araba_resim, araba)
    pencere.blit(engel_resim, engel)
    pencere.blit(score_text, (10,10))

    clock.tick(60)
    pygame.display.update()

pygame.quit()
