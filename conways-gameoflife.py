import pygame

pygame.init()

# global variables
windowHeight = 750
windowWidth = 750
screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
running = True
blockSize = 50
blockDrawSize = blockSize - 1
grid = []
colors = {
    "dead" : "black",
    "alive" : "red",
}

count = -1
for x in range(0,windowWidth,blockSize):
    count += 1
    grid.append([])
    for y in range(0, windowHeight, blockSize):
        grid[count].append("dead")
print(len(grid))
print(len(grid[14]))

#test
grid[3][4] = "alive"

print(grid[4][5])

def drawGrid():
    #range(start,stop,incrementby)
    xcount = -1
    for x in range(0,windowWidth,blockSize):
        ycount = -1
        xcount += 1
        for y in range(0, windowHeight, blockSize):
            ycount += 1
            block = pygame.Rect(x,y,blockDrawSize,blockDrawSize)
            pygame.draw.rect(screen, colors[grid[xcount][ycount]], block)

def toggleBlock(mousex, mousey):
    x = mousex
    y = mousey

    x /= blockSize
    y /= blockSize
    x = int(x)
    y = int(y)

    if grid[x][y] == "alive":
        grid[x][y] = "dead"
    elif grid[x][y] == "dead":
        grid[x][y] = "alive"
    else:
        print("something's wrong")



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousex, mousey = pygame.mouse.get_pos()
                toggleBlock(mousex, mousey)

    screen.fill("white")
    drawGrid()

    # main loop

    # update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
