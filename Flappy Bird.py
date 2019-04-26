import pygame
import sys
import random


class Bird(object):

    def __init__(self):
        self.birdRect = pygame.Rect(65, 50, 50, 50)
        self.birdStatus = [pygame.image.load("Resource/0.png").convert_alpha(),
                           pygame.image.load("Resource/1.png").convert_alpha(),
                           pygame.image.load("Resource/2.png").convert_alpha(),
                           pygame.image.load("Resource/dead.png").convert_alpha()]
        self.status = 0
        self.birdX = 200
        self.birdY = 350
        self.jump = False
        self.dead = False
        self.fall = False
        self.jumpSpeed = 10
        self.gravity = 5

    def birdupdate(self):
        if self.jump:
            self.jumpSpeed = self.jumpSpeed - 1
            self.birdY = self.birdY - self.jumpSpeed
        elif self.fall:
            self.gravity = self.gravity + 1
            self.birdY = self.birdY + self.gravity
        self.birdRect[1] = self.birdY


class Pipeline(object):

    def __init__(self):
        self.pipeX = 400
        self.gap = 130
        self.offset = 0
        self.pipeUp = pygame.image.load("Resource/top.png")
        self.pipeDown = pygame.image.load("Resource/bottom.png")

    def updatepipeline(self):
        self.pipeX = self.pipeX - 5
        if self.pipeX < -80:
            global points
            points = points + 1
            self.offset = random.randint(-110, 110)
            self.pipeX = 400


def createmap():
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(Pipeline.pipeDown, (Pipeline.pipeX, 360 + Pipeline.gap - Pipeline.offset))
    screen.blit(Pipeline.pipeUp, (Pipeline.pipeX, 0 - Pipeline.gap - Pipeline.offset))
    Pipeline.updatepipeline()
    if Bird.dead:
        Bird.status = 3
    elif Bird.jump:
        Bird.status = 1
    elif Bird.fall:
        Bird.status = 2
    else:
        Bird.status = 0
    screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX, Bird.birdY))
    Bird.birdupdate()
    pygame.display.update()


def checkingdeath():
    uprect = pygame.Rect(Pipeline.pipeX, 360 + Pipeline.gap - Pipeline.offset + 10,
                         Pipeline.pipeUp.get_width() - 10,
                         Pipeline.pipeUp.get_height())

    downrect = pygame.Rect(Pipeline.pipeX, 0 - Pipeline.gap - Pipeline.offset - 10,
                           Pipeline.pipeDown.get_width() - 10,
                           Pipeline.pipeDown.get_height())

    if uprect.colliderect(Bird.birdRect) or downrect.colliderect(Bird.birdRect):
        Bird.dead = True
    if not 0 < Bird.birdRect[1] < height:
        Bird.dead = True
        return True
    else:
        return False


def getresult():
    final_text1 = "Game Over"
    final_text2 = "Your final points is :  " + str(points)
    final_text3 = "Award"
    final_text4 = "Hit the space to restart"
    final_text5 = "Well Done"
    final_text6 = "Good Job"
    final_text7 = "Excellent"
    font1_font = pygame.font.SysFont("Arial", 70)
    font1_surf = font.render(final_text1, 1, (225, 105, 86))
    font2_font = pygame.font.SysFont("Arial", 60)
    font2_surf = font.render(final_text2, 1, (203, 177, 96))
    font3_font = pygame.font.SysFont("Times", 50)
    font3_surf = font.render(final_text3, 1, (90, 150, 175))
    font4_font = pygame.font.SysFont("Times", 5)
    font4_surf = font.render(final_text4, 1, (255, 0, 255))
    font5_font = pygame.font.SysFont("Times", 20)
    font5_surf = font.render(final_text5, 1, (200, 29, 30))
    font6_font = pygame.font.SysFont("Times", 20)
    font6_surf = font.render(final_text6, 1, (155, 124, 40))
    font7_font = pygame.font.SysFont("Times", 20)
    font7_surf = font.render(final_text7, 1, (100, 20, 50))
    screen.blit(font1_surf, [screen.get_width() / 2 - font1_surf.get_width() / 2, 100])
    screen.blit(font2_surf, [screen.get_width() / 2 - font2_surf.get_width() / 2, 200])
    screen.blit(font3_surf, [screen.get_width() / 2 - font3_surf.get_width() / 2, 300])
    medal1 = pygame.image.load("Resource/Gold.png").convert_alpha()
    medal2 = pygame.image.load("Resource/Silver.png").convert_alpha()
    medal3 = pygame.image.load("Resource/Copper.png").convert_alpha()
    medal4 = pygame.image.load("Resource/tryagain.jpg").convert_alpha()
    new_m1 = pygame.transform.scale(medal1, (100, 100))
    new_m2 = pygame.transform.scale(medal2, (100, 100))
    new_m3 = pygame.transform.scale(medal3, (100, 100))
    new_m4 = pygame.transform.scale(medal4, (100, 100))
    sound_1 = pygame.mixer.Sound("Resource/applause1.wav")
    sound_1.set_volume(0.8)
    sound_2 = pygame.mixer.Sound("Resource/applause2.wav")
    sound_2.set_volume(0.8)
    sound_3 = pygame.mixer.Sound("Resource/applause3.wav")
    sound_3.set_volume(0.8)
    sound_4 = pygame.mixer.Sound("Resource/scream.wav")
    sound_4.set_volume(0.8)
    if 10 < points < 20:
        sound_1.play(1, 10, 10)
        screen.blit(font5_surf, [screen.get_width() / 2 - font5_surf.get_width() / 2, 600])
        screen.blit(new_m3, (150, 400))
    elif 20 < points < 30:
        sound_2.play(1, 10, 10)
        screen.blit(font6_surf, [screen.get_width() / 2 - font6_surf.get_width() / 2, 600])
        screen.blit(new_m2, (150, 400))
    elif points > 30:
        sound_3.play(1, 10, 10)
        screen.blit(font7_surf, [screen.get_width() / 2 - font7_surf.get_width() / 2, 600])
        screen.blit(new_m1, (150, 400))
    else:
        sound_4.play(1, 10, 10)
        screen.blit(font4_surf, [screen.get_width() / 2 - font4_surf.get_width() / 2, 600])
        screen.blit(new_m4, (150, 400))
    pygame.display.flip()


def startover(): # reset the game
    global points
    points = 0
    Bird.birdX = 200
    Bird.birdY = 350
    Bird.gravity = 5
    Bird.jumpSpeed = 10
    Bird.status = 0
    Bird.dead = False
    Bird.jump = False
    Bird.fall = False
    Pipeline.pipeX = 400
    createmap()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    flap_sound = pygame.mixer.Sound("Resource/flap.wav")
    flap_sound.set_volume(0.4)
    fall_sound = pygame.mixer.Sound("Resource/fall.wav")
    fall_sound.set_volume(0.4)
    pygame.mixer.music.load("Resource/bgm.mp3")
    pygame.mixer.music.play()
    points = 0
    pygame.display.set_caption("Flappy Bird")
    font = pygame.font.SysFont(None, 50)
    size = width, height = 400, 700
    screen = pygame.display.set_mode(size)
    icon = pygame.image.load("Resource/0.png")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    Bird = Bird()
    Pipeline = Pipeline()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not Bird.dead:
                flap_sound.play()
                Bird.jump = True
                Bird.gravity = 5
                Bird.jumpSpeed = 10
            elif Bird.dead:
                if event.type == pygame.KEYDOWN:
                    startover()
            else:
                Bird.fall = True
                fall_sound.play()
                Bird.gravity = 3
        background = pygame.image.load("Resource/background.png")
        if checkingdeath():
            fall_sound.stop()
            getresult()
            pygame.display.update()
        else:
            createmap()
    pygame.QUIT()

# Reference: https://github.com/f-prime/FlappyBird/blob/master/flappybird.py