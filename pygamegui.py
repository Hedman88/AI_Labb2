import pygame, sys, mapreader
from pygame.locals import *

pygame.init()

FPS = 60
clock = pygame.time.Clock()

maprows = mapreader.ReadMap("Map3.txt") #display based on amount of tiles in map
displaySize = (len(maprows)*(len(maprows[0])-1))
display = pygame.display.set_mode((displaySize, displaySize))
display.fill((255,255,255))
pygame.display.set_caption("Path Finding")
rectSize = displaySize / (len(maprows[0])-1)

def StartPygame():
    pygame.init()

    FPS = 60
    clock = pygame.time.Clock()

    displaySize = (len(maprows)*(len(maprows[0])-1))
    display = pygame.display.set_mode((displaySize, displaySize))
    display.fill((255,255,255))
    pygame.display.set_caption("Path Finding")


def DrawMap():
    for i in range(len(maprows)):
        for j in range(len(maprows[0])-1):
            if(maprows[i][j] == "X"):
                pygame.draw.rect(display, (0,0,0), (j*rectSize, i*rectSize, rectSize, rectSize))
                continue
            #if(maprows[i][j] == "X"):
                #pygame.draw.rect(display, (0,0,0), (j*rectSize, i*rectSize, rectSize, rectSize))
                #pathfinder.paths.pathBlocks.append(pathfinder.PathBlock(i*100+j, neighbours, False, False, False))
            if(maprows[i][j] == "0"):
                pygame.draw.rect(display, (0,0,0), (j*rectSize, i*rectSize, rectSize, rectSize), 1)
            if(maprows[i][j] == "S"):
                pygame.draw.rect(display, (0,255,0), (j*rectSize, i*rectSize, rectSize, rectSize))
            if(maprows[i][j] == "G"):
                pygame.draw.rect(display, (255,0,0), (j*rectSize, i*rectSize, rectSize, rectSize))

def DrawPath(path):
    for i in range(len(path)-1):
        startPoint = (path[i].id%100 + 1)*(rectSize) - rectSize/2, (path[i].id/100 + 1)*(rectSize) - rectSize/2
        endPoint = (path[i+1].id%100 + 1)*(rectSize) - rectSize/2, (path[i+1].id/100 + 1)*(rectSize) - rectSize/2
        pygame.draw.line(display, (0,0,255), startPoint, endPoint, 3)

def DrawAStar(openList, closedList):
    for i in range(len(openList)):
        centerPoint = (openList[i].id%100 + 1)*(rectSize) - rectSize/2, (openList[i].id/100 + 1)*(rectSize) - rectSize/2
        pygame.draw.circle(display, (255,155,0), centerPoint, 3)
        if(openList[i].prevBlockID != 0):
            print(openList[i].prevBlockID)
            pB = openList[i].GetPrevBlock()
            x = (((pB.id%100 + 1) - (openList[i].id%100 + 1)) / 2) + (openList[i].id%100 + 1)
            y = (((pB.id/100 + 1) - (openList[i].id/100 + 1)) / 2) + (openList[i].id/100 + 1)
            endPoint = (x*rectSize - rectSize/2), (y*rectSize - rectSize/2)
            pygame.draw.line(display, (0,255,0), centerPoint, endPoint, 2)
    for i in range(len(closedList)):
        centerPoint = (closedList[i].id%100 + 1)*rectSize - rectSize/2, (closedList[i].id/100 + 1)*rectSize - rectSize/2
        pygame.draw.circle(display, (0,255,255), centerPoint, 3)
        if (closedList[i].prevBlockID != 0):
            print(closedList[i].prevBlockID)
            pB = closedList[i].GetPrevBlock()
            x = (((pB.id % 100 + 1) - (closedList[i].id % 100 + 1)) / 2) + (closedList[i].id % 100 + 1)
            y = (((pB.id / 100 + 1) - (closedList[i].id / 100 + 1)) / 2) + (closedList[i].id / 100 + 1)
            endPoint = (x * rectSize - rectSize / 2), (y * rectSize - rectSize / 2)
            pygame.draw.line(display, (255, 0, 0), centerPoint, endPoint, 2)

def DrawVisited(visited):
    for i in range(len(visited)):
        centerPoint = (visited[i].id%100 + 1)*(rectSize) - rectSize/2, (visited[i].id/100 + 1)*(rectSize) - rectSize/2
        pygame.draw.circle(display, (255,155,0), centerPoint, 3)
        if(visited[i].prevBlockID != 0):
            #print(visited[i].prevBlockID)
            pB = visited[i].GetPrevBlock()
            x = (((pB.id%100 + 1) - (visited[i].id%100 + 1)) / 2) + (visited[i].id%100 + 1)
            y = (((pB.id/100 + 1) - (visited[i].id/100 + 1)) / 2) + (visited[i].id/100 + 1)
            endPoint = (x*rectSize - rectSize/2), (y*rectSize - rectSize/2)
            pygame.draw.line(display, (0,255,0), centerPoint, endPoint, 2)

def Clear():
    display.fill((255,255,255))
    DrawMap()

def Update():
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
