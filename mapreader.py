
def ReadMap(mapFileName):
    maprows = []
    f = open(mapFileName,"r")
    maprows = f.readlines()
    f.close()
    return maprows

