from maam import display, massage    #import another file that containing the defination of display and massage func
import pygame
import cv2

pygame.init()
scr = pygame.display.set_mode((600, 500))
look_1 = pygame.image.load('logo.jpg')
look_1 = pygame.transform.scale(look_1, (600, 500))
scr.blit(look_1, (0, 0))
pygame.display.update()
done = True

def image_show(img_adress):
    '''This functoin is displaying  image on the screen '''
    global img
    img = cv2.imread(img_adress)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

while done:
    '''loop for holding the screen'''
    x = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:                               #intro screen
                scr = pygame.display.set_mode((800, 700))
                massage(50, (200, 0, 200), scr, '', "TO MAKE A SKETCH OF ANY PICTURE", 100, 200)
                massage(50, (200, 0, 200), scr, '', "USING PYTHON", 300, 250)
                massage(40, (255, 170, 100), scr, '', "by coder_byz.exe", 300, 400)
                pygame.display.update()

            if event.key == pygame.K_1:                             #screen 1
                scr1 = pygame.display.set_mode((800, 650))
                massage(25, (255, 255, 255), scr1, '', " PRESENTED BY :- coder_byz.exe", 500, 20)
                massage(65, (50, 100, 200), scr1, '', "SKETCH OF APJ ABDUL KALAM", 70, 300)
                pygame.display.update()

            if event.key == pygame.K_3:                            #showing real image and converted sketch
                image_show("C:\\Users\\sharm\\Pictures\\A._P._J._Abdul_Kalam.jpg")
                chitra = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                invert = cv2.bitwise_not(chitra)
                blur = cv2.GaussianBlur(invert, (21, 21), 0)
                invertedblur = cv2.bitwise_not(blur)
                sketch = cv2.divide(chitra, invertedblur, scale=256.0)
                cv2.imwrite("APJ2.png", sketch)
                image_show("C:\\Users\\sharm\\PycharmProjects\\MAX PLAYER\\APJ2.png")

            if event.key == pygame.K_x:                          #ending screen
                massage(80, (255, 0, 0), pygame.display.set_mode((800, 700)), '', "THANK YOU ", 200, 250)

pygame.quit()
