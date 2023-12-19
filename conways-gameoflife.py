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
deadcolor = (14,197,249)
alivecolor = (249,14,167)
colors = {
    "dead" : deadcolor,
    "alive" : alivecolor,
}

count = -1
for x in range(0,windowWidth,blockSize):
    count += 1
    grid.append([])
    for y in range(0, windowHeight, blockSize):
        grid[count].append("dead")

#debug
#print(len(grid))
#print(len(grid[14]))
#print(grid[4][5])

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

def getLiveNeighbourCount(x,y):
    liveNeighbourCount = 0
    xlength = len(grid)-1
    ylength = len(grid[0])-1
    #print(x,y)
    #specific cases
    #x=0
    if x == 0:
        if y == 0:
            if grid[x][y+1] == "alive": #down
                liveNeighbourCount += 1
            if grid[x+1][y] == "alive": #right
                liveNeighbourCount += 1
            if grid[x+1][y+1] == "alive": #down right
                liveNeighbourCount += 1
        elif y == ylength:
            if grid[x][y-1] == "alive": #up
                liveNeighbourCount += 1
            if grid[x+1][y] == "alive": #right
                liveNeighbourCount += 1
            if grid[x+1][y-1] == "alive": #up right
                liveNeighbourCount += 1
        else:
            if grid[x][y-1] == "alive": #up
                liveNeighbourCount += 1
            if grid[x][y+1] == "alive": #down
                liveNeighbourCount += 1
            if grid[x+1][y] == "alive": #right
                liveNeighbourCount += 1
            if grid[x+1][y-1] == "alive": #up right
                liveNeighbourCount += 1
            if grid[x+1][y+1] == "alive": #down right
                liveNeighbourCount += 1
        return liveNeighbourCount

    #x=max
    if x == xlength:
        if y == 0:
            if grid[x-1][y] == "alive": #left
                liveNeighbourCount += 1
            if grid[x][y+1] == "alive": #down
                liveNeighbourCount += 1
            if grid[x-1][y+1] == "alive": #down left
                liveNeighbourCount += 1
        if y == ylength:
            if grid[x][y-1] == "alive": #up
                liveNeighbourCount += 1
            if grid[x-1][y] == "alive": #left
                liveNeighbourCount += 1
            if grid[x-1][y-1] == "alive": #up left
                liveNeighbourCount += 1
        else:
            if grid[x][y-1] == "alive": #up
                liveNeighbourCount += 1
            if grid[x][y+1] == "alive": #down
                liveNeighbourCount += 1
            if grid[x-1][y] == "alive": #left
                liveNeighbourCount += 1
            if grid[x-1][y-1] == "alive": #up left
                liveNeighbourCount += 1
            if grid[x-1][y+1] == "alive": #down left
                liveNeighbourCount += 1
        return liveNeighbourCount
    #y=0
    if y == 0:
        if grid[x][y+1] == "alive": #down
            liveNeighbourCount += 1
        if grid[x+1][y] == "alive": #right
            liveNeighbourCount += 1
        if grid[x-1][y] == "alive": #left
            liveNeighbourCount += 1
        if grid[x-1][y+1] == "alive": #down left
            liveNeighbourCount += 1
        if grid[x+1][y+1] == "alive": #down right
            liveNeighbourCount += 1
        return liveNeighbourCount

    #y=max
    if y == ylength:
        if grid[x][y-1] == "alive": #up
            liveNeighbourCount += 1
        if grid[x+1][y] == "alive": #right
            liveNeighbourCount += 1
        if grid[x-1][y] == "alive": #left
            liveNeighbourCount += 1
        if grid[x-1][y-1] == "alive": #up left
            liveNeighbourCount += 1
        if grid[x+1][y-1] == "alive": #up right
            liveNeighbourCount += 1
        return liveNeighbourCount

    #general case
    if grid[x][y-1] == "alive": #up
        liveNeighbourCount += 1
    if grid[x][y+1] == "alive": #down
        liveNeighbourCount += 1
    if grid[x+1][y] == "alive": #right
        liveNeighbourCount += 1
    if grid[x-1][y] == "alive": #left
        liveNeighbourCount += 1
    if grid[x-1][y-1] == "alive": #up left
        liveNeighbourCount += 1
    if grid[x+1][y-1] == "alive": #up right
        liveNeighbourCount += 1
    if grid[x-1][y+1] == "alive": #down left
        liveNeighbourCount += 1
    if grid[x+1][y+1] == "alive": #down right
        liveNeighbourCount += 1
    return liveNeighbourCount

def main():
    xlength = len(grid)
    ylength = len(grid[0])
    #print(xlength,ylength)
    for x in range(xlength):
        for y in range(ylength):
            if grid[x][y] == "alive":
                if getLiveNeighbourCount(x,y) < 2:
                    grid[x][y] = "dead"
                elif getLiveNeighbourCount(x,y) > 3:
                    grid[x][y] = "dead"
            elif grid[x][y] == "dead":
                if getLiveNeighbourCount(x,y) == 3:
                    grid[x][y] = "alive"

play = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousex, mousey = pygame.mouse.get_pos()
                toggleBlock(mousex, mousey)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if play == True:
                    play = False
                elif play == False:
                    play = True

    screen.fill("white")
    drawGrid()

    #main game loop

    if play:
        main()

    # update display
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
