

class PathFinder:
    goalFound = False
    visited = set()
    path = []
    def dfs(self, currentBlock):
        
        if(currentBlock.isGoal):
            self.goalFound = True
            self.path.append(currentBlock)
            return
        if(currentBlock not in self.visited and self.goalFound == False):
            self.visited.add(currentBlock)
            print(currentBlock)
            for neighbour in currentBlock.adjacents:
                print(neighbour)
                neighbourBlock = paths.GetBlockByID(neighbour)
                if(neighbourBlock.traversable):
                    self.dfs(neighbourBlock)
                    if(self.goalFound):
                        self.path.append(currentBlock)
                        return
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
