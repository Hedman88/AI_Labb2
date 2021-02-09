visited = set()

class PathFinder:
    goalFound = False
    def dfs(self, visited, pathBlocks, currentBlock):
        if(currentBlock.isGoal):
            self.goalFound = True
        if(currentBlock not in visited and self.goalFound == False):
            visited.add(currentBlock)
            print(currentBlock)
            for neighbour in currentBlock.adjacents:
                print(neighbour)
                n = paths.GetBlockByID(neighbour)
                if(n.traversable):
                    self.dfs(visited, pathBlocks, paths.GetBlockByID(neighbour))

    #def bfs():

    #def Astar():
        
class PathBlock:

    def __init__(self, ID, adjacents, traversable, isGoal, isStart):
        self.id = ID
        self.adjacents = adjacents
        self.traversable = traversable
        self.isGoal = isGoal
        self.isStart = isStart

class Paths:
    pathBlocks = []
    def GetStart(self):
        for i in self.pathBlocks:
            if(i.isStart):
                return i

    def GetBlockByID(self, ID):
        for i in self.pathBlocks:
            if(i.id == ID):
                print(ID)
                return i

paths = Paths()
pf = PathFinder()
