import pathfinder


def ReadMap(mapFileName):
    f = open(mapFileName,"r")
    global maprows
    maprows = f.readlines()
    f.close()
    print(len(maprows))
    return maprows

def InitMapBlocks():
    print(len(maprows))
    for i in range(len(maprows)):
        for j in range(len(maprows[0])-1):
            selfID = i*100+j
            #All neighbouring IDs
            N = (i-1)*100+j
            NE = (i-1)*100+j+1
            E = i*100+j+1
            SE = (i+1)*100+j+1
            S = (i+1)*100+j
            SW = (i+1)*100+j-1
            W = i*100+j-1
            NW = (i-1)*100+j-1
            #SE, S, E, N, NW, W, SW, NE best order?
            neighbours = []
            if(maprows[i][j] == "X"):
                continue
            #Appending all relevant IDs to current block
            if(maprows[i-1][j] != "X"):
                neighbours.append(N)
            if(maprows[i-1][j+1] != "X" and maprows[i-1][j] != "X" and maprows[i][j+1] != "X"):
                neighbours.append(NE)
            if(maprows[i][j+1] != "X"):
                neighbours.append(E)
            if(maprows[i+1][j+1] != "X" and maprows[i][j+1] != "X" and maprows[i+1][j] != "X"):
                neighbours.append(SE)
            if(maprows[i+1][j] != "X"):
                neighbours.append(S)
            if(maprows[i+1][j-1] != "X" and maprows[i+1][j] != "X" and maprows[i][j-1] != "X"):
                neighbours.append(SW)
            if(maprows[i][j-1] != "X"):
                neighbours.append(W)
            if(maprows[i-1][j-1] != "X" and maprows[i][j-1] != "X" and maprows[i-1][j] != "X"):
                neighbours.append(NW)
    
            if(maprows[i][j] == "0"):
                pathfinder.paths.pathBlocks.append(pathfinder.PathBlock(selfID, neighbours, True, False, False))
            if(maprows[i][j] == "S"):
                pathfinder.paths.pathBlocks.append(pathfinder.PathBlock(selfID, neighbours, True, False, True))
            if(maprows[i][j] == "G"):
                pathfinder.paths.pathBlocks.append(pathfinder.PathBlock(selfID, neighbours, True, True, False))
