import pathfinder, mapreader, timer, cProfile, time
import pygamegui as gui



gui.DrawMap()
mapreader.InitMapBlocks()
gui.Update()
#cProfile.run("pathfinder.pf.AStar(pathfinder.paths.GetStart())")

timer.StartTimer()
pathfinder.pf.dfs(pathfinder.paths.GetStart())
timer.StopTimer()
timer.PrintTime("dfs")
gui.Clear()
gui.DrawPath(pathfinder.pf.path)
gui.Update()
time.sleep(1)
pathfinder.pf.Reset()

timer.StartTimer()
pathfinder.pf.bfs(pathfinder.paths.GetStart())
timer.StopTimer()
timer.PrintTime("bfs")
gui.Clear()
gui.DrawPath(pathfinder.pf.path)
gui.Update()
time.sleep(1)
pathfinder.pf.Reset()

timer.StartTimer()
pathfinder.pf.AStar(pathfinder.paths.GetStart())
timer.StopTimer()
timer.PrintTime("ASt")
gui.Clear()
gui.DrawPath(pathfinder.pf.path)
gui.Update()
gui.Update()
time.sleep(1)
pathfinder.pf.Reset()

timer.StartTimer()
pathfinder.pf.LineSearch(pathfinder.paths.GetStart())
timer.StopTimer()
timer.PrintTime("Lin")
gui.Clear()
gui.DrawPath(pathfinder.pf.path)
gui.Update()

while True:
    gui.Update()
    gui.clock.tick(gui.FPS)
