import pygamegui as gui
import time, math

class PathFinder:
    goalFound = False
    visited = []
    path = []
    def dfs(self, currentBlock):
        gui.Clear()
        gui.DrawVisited(self.visited)
        gui.Update()
        if(currentBlock.isGoal):
            self.goalFound = True
            self.path.append(currentBlock)
            return
        if(currentBlock not in self.visited and self.goalFound == False):
            self.visited.append(currentBlock)
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
        self.visited.append(startBlock)
        bfsQ = []
        bfsQ.append(startBlock)
        while bfsQ:
            s = bfsQ.pop(0)
            print(s.id)
            for neighbour in s.adjacents:
                neighbourBlock = paths.GetBlockByID(neighbour)
                if neighbourBlock not in self.visited:
                    self.visited.append(neighbourBlock)
                    bfsQ.append(neighbourBlock)
                    neighbourBlock.prevBlockID = s.id
                    if(neighbourBlock.isGoal):
                        print(neighbourBlock)
                        self.path.append(neighbourBlock)
                        prevID = neighbourBlock.prevBlockID
                        while(prevID != 0):
                            print("going")
                            prevBlock = paths.GetBlockByID(prevID)
                            self.path.append(prevBlock)
                            prevID = prevBlock.prevBlockID
                        return
                

    def AStar(self, startBlock):
        openList = []
        closedList = []
        openList.append(startBlock)

        while openList:
            print("running")
            q = openList[0]
            #find best block by f value
            for i in range(len(openList)):
                if(q.f > openList[i].f):
                    q = openList[i]
            openList.remove(q)
            #go through all successors
            for neighbourID in q.adjacents:
                skip = False
                neighbourBlock = paths.GetBlockByID(neighbourID)

                if(neighbourBlock.isGoal):
                    self.path.append(neighbourBlock)
                    prevID = q.prevBlockID
                    while(prevID != 0):
                        print("going")
                        #print(prevID)
                        prevBlock = paths.GetBlockByID(prevID)
                        self.path.append(prevBlock)
                        prevID = prevBlock.prevBlockID
                    return
                if(neighbourBlock.id%100 != q.id%100 and neighbourBlock.id/100 != q.id/100):
                    neighbourBlock.g = q.g + 1.4
                else:
                    neighbourBlock.g = q.g + 1
                neighbourBlock.h = self.Diagonal(neighbourID)
                neighbourBlock.f = neighbourBlock.g + neighbourBlock.h
                for i in openList:
                    if(i.id == neighbourBlock.id and neighbourBlock.f >= i.f):
                        skip = True
                for i in closedList:
                    if(i.id == neighbourBlock.id and neighbourBlock.f >= i.f):
                        skip = True
                if skip is False:
                    # set q as parent to all neighbour blocks
                    neighbourBlock.prevBlockID = q.id
                    openList.append(neighbourBlock)
            closedList.append(q)
            gui.Clear()
            gui.DrawAStar(openList, closedList)
            gui.Update()
            time.sleep(0.01)

    def LineSearch(self, startBlock):
        self.visited.append(startBlock)
        print(startBlock.id)
        lineQ = []
        sbQ = []
        # Initiate first 3 directional lines
        for i in range(3):
            lineDir = startBlock.adjacents[0]
            for neighbourID in startBlock.adjacents:
                if self.Diagonal(neighbourID) < self.Diagonal(lineDir) and neighbourID not in lineQ:
                    lineDir = neighbourID
            lineQ.append(lineDir)
            sbQ.append(self.SendLine(startBlock, lineDir))

        while sbQ:
            sb = sbQ.pop(0)
            nID = sb.adjacents[0]
            #Get neighbour closest to goal
            for neighbourID in sb.adjacents:
                if(self.Diagonal(neighbourID) < self.Diagonal(nID) and paths.GetBlockByID(neighbourID) not in self.visited):
                    nID = neighbourID
            nextStartBlock = self.SendLine(sb, nID)
            if(nextStartBlock.isGoal):
                self.path.append(nextStartBlock)
                prevID = nextStartBlock.prevBlockID
                while (prevID != 0):
                    print("going")
                    prevBlock = paths.GetBlockByID(prevID)
                    self.path.append(prevBlock)
                    prevID = prevBlock.prevBlockID
                return
            sbQ.append(nextStartBlock)
        # for neighbourID in lineQ:
        #     nBlock = paths.GetBlockByID(neighbourID)
        #     self.visited.append(nBlock)
        #     nBlock.prevBlockID = startBlock.id
        #     nextID_dif = nBlock.id - startBlock.id
        #     print(nextID_dif)
        #     while True:
        #         nextID = nBlock.id + nextID_dif
        #         if nextID not in nBlock.adjacents:
        #             lineQ.append(nBlock.id)
        #             break
        #         nBlock = paths.GetBlockByID(nextID)
        #         nBlock.prevBlockID = nextID - nextID_dif
        #         self.visited.append(nBlock)
        #         gui.Clear()
        #         gui.DrawVisited(self.visited)
        #         gui.Update()
        #         time.sleep(0.1)

    def SendLine(self, startBlock, dir):
        nextID_dif = dir - startBlock.id
        while True:
            nextID = startBlock.id + nextID_dif
            if nextID not in startBlock.adjacents:
                return startBlock
            startBlock = paths.GetBlockByID(nextID)
            if(startBlock in self.visited):
                return startBlock
            startBlock.prevBlockID = nextID - nextID_dif
            if(startBlock.isGoal):
                self.goalFound = True
                return startBlock
            self.visited.append(startBlock)
            gui.Clear()
            gui.DrawVisited(self.visited)
            gui.Update()
            time.sleep(0.1)

    def Manhattan(self, currentID):
        xCur = currentID % 100
        yCur = currentID / 100
        # Converting ID to coordinates
        goalID = paths.GetGoal().id
        xGoal = goalID % 100
        yGoal = goalID / 100
        h = abs(xCur - xGoal) + abs(yCur - yGoal)
        return h

    def Diagonal(self, currentID):
        xCur = currentID % 100
        yCur = currentID / 100
        #Converting ID to coordinates
        goalID = paths.GetGoal().id
        xGoal = goalID % 100
        yGoal = goalID / 100
        #Diagonal Distance Heuristics
        h = max([abs(xCur - xGoal), abs(yCur - yGoal)])
        return h

    def Euclidean(self, currentID):
        xCur = currentID % 100
        yCur = currentID / 100
        # Converting ID to coordinates
        goalID = paths.GetGoal().id
        print("Goal id:", goalID)
        xGoal = goalID % 100
        yGoal = goalID / 100

        h = math.sqrt((xCur - xGoal)**2 + (yCur - yGoal)**2)
        return h
        
class PathBlock:
    nextBlockID = 0
    prevBlockID = 0
    #A* values
    g = 0.0
    h = 0.0
    f = 0.0
    def __init__(self, ID, adjacents, traversable, isGoal, isStart):
        self.id = ID
        self.adjacents = adjacents
        self.traversable = traversable
        self.isGoal = isGoal
        self.isStart = isStart

    def GetPrevBlock(self):
        return paths.GetBlockByID(self.prevBlockID)

class Paths:
    pathBlocks = []
    def GetStart(self):
        for i in self.pathBlocks:
            if(i.isStart):
                return i

    def GetGoal(self):
        for i in self.pathBlocks:
            if(i.isGoal):
                return i
    
    def GetBlockByID(self, ID):
        for i in self.pathBlocks:
            if(i.id == ID):
                #print(ID)
                return i

paths = Paths()
pf = PathFinder()
