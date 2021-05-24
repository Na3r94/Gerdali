import pygame
import time
import random

pygame.init()

class Color:
    red = (150,40,40)
    blue = (20,20,200)
    green = (80,180,80)
    orange = (255,127,0)
    white = (255,255,255)
    light = (180,180,180)


class Gerdali:
    images = ['Jalase14/Images/duck.png' , 'Jalase14/Images/stork.png','Jalase14/Images/shooter.png']
    def __init__(self):
        self.r = 50
        self.x = random.randint(100,Game.w - 100)
        self.y = random.randint(100,Game.h - 100)
        self.color = random.choice([Color.red , Color.blue , Color.green,Color.orange])
        self.image_path = random.choice(Gerdali.images)
        self.image = pygame.image.load(self.image_path)
        self.area = pygame.draw.circle(Game.display,self.color,(self.x,self.y),self.r)

    def show(self):
        self.area = pygame.draw.circle(Game.display,self.color,(self.x,self.y),self.r)
        Game.display.blit(self.image,(self.x - self.r/2 ,self.y - self.r/2))

    def move(self):
        self.x = random.randint(0,Game.w)
        self.y = random.randint(0,Game.h)

class Game:
    w = 1280
    h = 720
    display = pygame.display.set_mode((w,h))
    bg_color = Color.light
    font = pygame.font.SysFont("Arial",20)
    pygame.display.set_caption('Gerdali')
    score = 0
    tm1 = 0
    tm2 = 0
    @staticmethod
    def play():
        clock = pygame.time.Clock()
        gerdalies = [Gerdali()]
        Game.tm1 = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for gerdali in gerdalies:
                        if gerdali.area.collidepoint(event.pos):
                            
                            if gerdali == gerdalies[-1]:
                                while True:
                                    temp = Gerdali()
                                    if not any (temp.image_path == g.image_path and temp.color == g.color for g in gerdalies):
                                        gerdalies.append(temp)
                                        Game.score += 1
                                        break
                               
                            else:
                                print('NO')
                                Game.score = 0
                                Game.play()
                            
                        gerdali.move()
            Game.display.fill(Game.bg_color)
            font = pygame.font.SysFont("Arial",70)
            Game.tm2 = time.time() - Game.tm1
            text_time = Game.font.render('Time :'+ str(int(Game.tm2)),True,Color.green)
            Game.display.blit(text_time,(30,15))

            if Game.tm2 > 90:
                text_lose = font.render('Game Over!!!' , True, Color.red)
                Game.display.blit(text_lose,(Game.w/2 - 150 ,Game.h/2 - 70))
                Game.score = 0
                pygame.display.update()
                time.sleep(3)
                Game.play()

            if Game.score == 11:
                text_win = font.render('You Win!!!',True,((255,0,0)))
                Game.display.blit(text_win,(Game.w/2 - 150 ,Game.h/2 - 70))
                Game.score = 0
                pygame.display.update()
                time.sleep(3)
                Game.play()


            for gerdali in gerdalies:
                gerdali.show()
            text_me= Game.font.render('Score = '+str(Game.score),True,(125,0,125))
            Game.display.blit(text_me,(Game.w/2,15))    
            pygame.display.update()
            clock.tick(24)

if __name__ == '__main__':
    Game.play()