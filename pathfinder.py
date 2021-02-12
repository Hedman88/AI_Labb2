

class PathFinder:
    goalFound = False
    visited = set()
    path = []
    bfsQ = []
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
                    
    def bfs(self, startBlock):
        self.visited.add(startBlock)
        self.bfsQ.append(startBlock)
        while self.bfsQ:
            s = self.bfsQ.pop(0)
            print(s.id)
            for neighbour in s.adjacents:
                neighbourBlock = paths.GetBlockByID(neighbour)
                if neighbourBlock not in self.visited:
                    self.visited.add(neighbourBlock)
                    self.bfsQ.append(neighbourBlock)
                    if(s.isGoal):
                        print(s)
                        self.path.append(s)
                        return

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
                #print(ID)
                return i

paths = Paths()
pf = PathFinder()
