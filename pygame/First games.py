import pygame
pygame.init()

WIDTH = 700
HEIGHT = 480

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonic")

walkRight = [pygame.image.load('RUN START.png'), pygame.image.load('RUN 1.png'), pygame.image.load('RUN 2.png'), pygame.image.load('RUN START.png'), pygame.image.load('RUN 1.png'), pygame.image.load('RUN 2.png'), pygame.image.load('RUN START.png'), pygame.image.load('RUN 1.png'), pygame.image.load('RUN 2.png')]
walkLeft = [pygame.image.load('RUN L1.png'), pygame.image.load('RUN L2.png'), pygame.image.load('RUN L3.png'), pygame.image.load('RUN L1.png'), pygame.image.load('RUN L2.png'), pygame.image.load('RUN L3.png'), pygame.image.load('RUN L1.png'), pygame.image.load('RUN L2.png'), pygame.image.load('RUN L3.png'),]
bg = pygame.image.load('background.png')
char = pygame.image.load('STANCE 1.png')

x = 300
y = 300
width = 30
height = 30
vel = 25

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
      
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
    
    pygame.display.update() 
    

# Main_loop

run = True
while run:
    clock.tick(27) # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
pygame.quit()
