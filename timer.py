import time
start = 0
end = 0
elapsedTime = 0
def StartTimer():
    global start
    start = time.time()

def StopTimer():
    global start
    global end
    global elapsedTime
    end = time.time()
    elapsedTime = elapsedTime + (end - start)

def PrintTime(method):
    global elapsedTime
    print("Time elapsed for ", method, ": ", elapsedTime)
    elapsedTime = 0