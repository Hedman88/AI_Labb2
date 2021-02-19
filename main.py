import pathfinder, mapreader
import pygamegui as gui
from pygame.locals import *

#maprows = mapreader.ReadMap("Map2.txt")
gui.DrawMap()
mapreader.InitMapBlocks()
gui.Update()
#pathfinder.pf.dfs(pathfinder.paths.GetStart())
#pathfinder.pf.bfs(pathfinder.paths.GetStart())
#pathfinder.pf.AStar(pathfinder.paths.GetStart())
pathfinder.pf.LineSearch(pathfinder.paths.GetStart())
#print(pathfinder.pf.path)

#for i in pathfinder.pf.path:
#    print(i.id)
#    pygame.draw.circle(display, (150,0,150), ((i.id%100 + 1)*(rectSize) - rectSize/2, (i.id/100 + 1)*(rectSize) - rectSize/2), 3)

gui.DrawPath(pathfinder.pf.path)

gui.Update()
while True:
    gui.Update()


    gui.clock.tick(gui.FPS)
