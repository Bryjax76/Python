import pygame
import sys
from pygame.locals import *

## WYMIARY_OKNA ##

WIDTH = 640
HEIGHT = 480

## KOLORY ##

GRAY     = (100, 100, 100)
WHITE    = (255, 255, 255)
YELLOW   = (255, 255,   0)
BLACK    = (  0,   0,   0)

## STAŁE ##
BGCOLOR = GRAY
BLOKGAP = 2
BLOKWIDTH = 62
BLOKHEIGHT = 25
ARRAYWIDTH = 10
ARRAYHEIGHT = 5
PALETKAWIDTH = 100
PALETKAHEIGHT = 10
PILKACOLOR = WHITE
BLOK = 'blok'
PILKA = 'pilka'
PALETKA = 'paletka'
PILKASPEED = 1


class Blok(pygame.sprite.Sprite):
 
    def __init__(self):
        self.blokWidth = BLOKWIDTH
        self.blokHeight = BLOKHEIGHT
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.blokWidth, self.blokHeight))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.name = BLOK


        
class Pilka(pygame.sprite.Sprite):
    def __init__(self, displaySurf):
        pygame.sprite.Sprite.__init__(self)
        self.name = PILKA
        self.moving = False
        self.image = pygame.Surface((15, 15,))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.vectorx = PILKASPEED
        self.vectory = PILKASPEED
        self.score = 0
        

    def update(self, mousex, bloki, paletka, *args):
        if self.moving == False:
            self.rect.centerx = mousex

        else:
            self.rect.y += self.vectory

            hitGroup = pygame.sprite.Group(paletka, bloki)

            spriteHitList = pygame.sprite.spritecollide(self, hitGroup, False)
            if len(spriteHitList) > 0:
                for sprite in spriteHitList:
                    if sprite.name == BLOK:
                        sprite.kill()
                        self.score += 1
                self.vectory *= -1
                self.rect.y += self.vectory
            
            self.rect.x += self.vectorx
            
            blokHitList = pygame.sprite.spritecollide(self, bloki, True)
                
            if len(blokHitList) > 0:
                self.vectorx *= -1
                self.score += 1
            if self.rect.right > WIDTH:
                self.vectorx *= -1
                self.rect.right = WIDTH
            elif self.rect.left < 0:
                self.vectorx *= -1
                self.rect.left = 0
            if self.rect.top < 0:
                self.vectory *= -1
                self.rect.top = 0
        
class Paletka(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PALETKAWIDTH, PALETKAHEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.name = PALETKA


    def update(self, mousex, *args):
        if self.rect.x >= 0 and self.rect.right <= WIDTH:
            self.rect.centerx = mousex

        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        
class Score(object):
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('comicsansms', 200)
        self.render = self.font.render('' + str(self.score), True, BLACK, GRAY)
        self.rect = self.render.get_rect()
        self.rect.x = 450
        self.rect.y = 350
        self.rect.bottom = WIDTH

class main(object):
    def __init__(self):
        pygame.init()
        self.displaySurf, self.displayRect = self.makeScreen()
        self.mousex = 0
        self.bloki = self.createBloki()
        self.paletka = self.createPaletka()
        self.pilka = self.createPilka()
        self.score = Score()

        self.allSprites = pygame.sprite.Group(self.bloki, self.paletka, self.pilka)


    def updateScore(self):
        self.score.score = self.pilka.score
        self.score.render = self.score.font.render(str(self.score.score), True, BLACK, GRAY)
        self.score.rect = self.score.render.get_rect()
        self.score.rect.x = 290
        self.score.rect.y = 200
        self.score.rect.bottom = HEIGHT
        


    def makeScreen(self):
        pygame.display.set_caption('Arkanoid by Bryja & Czekotas')
        displaySurf = pygame.display.set_mode((WIDTH, HEIGHT))
        displayRect = displaySurf.get_rect()
        displaySurf.fill(BGCOLOR)
        displaySurf.convert()

        return displaySurf, displayRect


    def createPilka(self):
        pilka = Pilka(self.displaySurf)
        pilka.rect.centerx = self.paletka.rect.centerx
        pilka.rect.bottom = self.paletka.rect.top

        return pilka


    def createPaletka(self):
        paletka = Paletka()
        paletka.rect.centerx = self.displayRect.centerx
        paletka.rect.bottom = self.displayRect.bottom

        return paletka


    def createBloki(self):
        bloki = pygame.sprite.Group()
        
        for row in range(ARRAYHEIGHT):
            for i in range(ARRAYWIDTH):
                blok = Blok()
                blok.rect.x = i * (BLOKWIDTH + BLOKGAP)
                blok.rect.y = row * (BLOKHEIGHT + BLOKGAP)
                blok.color = self.setBlokColor(blok, row, i)
                blok.image.fill(blok.color)
                bloki.add(blok)

        return bloki


    def setBlokColor(self, blok, row, column):
        if column == 0 or column % 2 == 0:
            return YELLOW
        else:
            return BLACK
        

    def checkInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()

            if event.type == MOUSEMOTION:
                self.mousex = event.pos[0]

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.pilka.moving = True
                

    def terminate(self):
        pygame.quit()
        sys.exit()



    def mainLoop(self):
        while True:
            self.displaySurf.fill(BGCOLOR)
            self.updateScore()
            self.displaySurf.blit(self.score.render, self.score.rect)
            self.allSprites.update(self.mousex, self.bloki, self.paletka)
            self.allSprites.draw(self.displaySurf)
            pygame.display.update()
            self.checkInput()
            
            
if __name__ == '__main__':

    runGame = main()
    runGame.mainLoop()