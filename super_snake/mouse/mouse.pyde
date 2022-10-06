def setup():
    fullScreen()
    
def draw():
    clear()
    fill(255,255,255)
    circle(mouseX,mouseY,30)
    
counter = 0
def mousePressed():
    global counter
    counter += 1
    print(counter)
