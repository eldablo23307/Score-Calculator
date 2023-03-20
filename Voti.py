import time

def Startup():
    x = 0
    ast = "*"
    print("Loading")
    while x <= 10:
        print(ast)
        ast += "*"
        x += 1
        time.sleep(0.5)
    print("Ready")

def Calcolatore():
    print("Calcolatore di Voti")
    materia = input("Di quale materia vuoi calcolare il tuo punteggio: ")
    count = int(input("Di quanti voti hai: "))
    x = 1
    list = []
    while x <= count:
        print("Inserire il voto ")
        voto = int(input())
        list.append(voto)
        x += 1
    media = sum(list) / count
    media = round(media)
    media = str(media)
    print("La tua media per " + materia + " è " + media)

def test():
    punteggio_presso = int(input("Inserire il punteggio prese nel test: "))
    punteggio_massimo = int(input("Inserire il punteggio massimo nel test: "))

    tot = ((punteggio_presso/punteggio_massimo)*8)+2

    print(tot)


Startup()
scelta = input("Qualle modalita scegli calcolo della media o calcolo punteggio test?:")

if (scelta == "calcolo della media"):
    Calcolatore()
elif(scelta == "calcolo punteggio test"):
    test()


""""
import pygame
s
pygame.init()
    win = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Calcolatore di Voti")

run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        fonts = pygame.font.SysFont("Arial", 36)
    txtsurf = fonts.render("Calcolatore", True, "white")
    win.blit(txtsurf,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
    pygame.display.update()
""" 
# Questa parte la aggiungero un furturo(forse)
