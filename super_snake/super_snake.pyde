def setup():
    global racoon
    size(800,800)
    background (0,0,0)
    racoon = loadImage("racoon.png")
x = 400
y = 400   
i = 1
c = floor(random(1,40))* 20
d = floor(random(1,40))* 20
e = floor(random(1,40))* 20
l = 3
cl = 0
body = []
g = 0
f = floor(random(1,40))* 20
respwan = []
respwan2 = []
x1 = 500
y1 = 500
x2 = 300
y2 = 300
move = floor(random(1,2))
move2 = floor(random(1,2))
o = 0
m = floor(random(1,40))* 20 
n = floor(random(1,40))* 20
flicker = 0
counter = 0
reset = 0
score = 0
bigman = 0
def gameLoop():
    global x,y,i,c,d,e,l,f,g,x1,y1,move,x2,y2,move2,o,m,n,counter,flicker,reset,score,racoon,bigman
    if reset == 1:
        g = 2
        reset = 0
        score = l
        l = 3
        d = floor(random(1,40))* 20
        c = floor(random(1,40))* 20
        m = floor(random(1,40))* 20
        n = floor(random(1,40))* 20 
        cl = 0
        x1 = 500
        y1 = 500
        x2 = 300
        y2 = 300
        y = 400
        x = 400
        flicker = 0
        counter = 0
        bigman = 0
    clear()
    fill (255)
    rect(x,y,20,20)
    rect(c,d,20,20)
    fill(255,0,255)
    rect(f,e,20,20)
    fill(55,55,55)
    image(racoon,x1,y1,20,20)
    fill(0,255,0)
    rect(m,n,20,20)
    fill (255)
    if  x>=800:
        reset = 1
    if  y>=800:
        reset = 1
    if  x<=0:
        reset = 1
    if  y<=0:
        reset = 1
    for segment in body:
        square(segment[0],segment[1],20)
        if  [x,y]==segment:
            y = 400
            x = 400
            l = 3
            d = floor(random(1,40))* 20
            c = floor(random(1,40))* 20
            g = 2
    while len(body)>=l:
        body.pop(0)
    body.append([x,y])
    respwan.append([c,d])
    respwan2.append([m,n])
    if x==c and y==d:
        l += 1
        d = floor(random(1,40))* 20
        c = floor(random(1,40))* 20
        if [c,d] == segment:
            d = floor(random(1,40))* 20
            c = floor(random(1,40))* 20
        if c==m and d==n:
            m = floor(random(1,40))* 20
            n = floor(random(1,40))* 20
    if x==m and y==n:
        l += 2
        m = floor(random(1,40))* 20
        n = floor(random(1,40))* 20
        counter += 40
        if [m,n] == segment:
            m = floor(random(1,40))* 20
            n = floor(random(1,40))* 20
        if m==c and n==m:
            m = floor(random(1,40))* 20
            n = floor(random(1,40))* 20
    if x==x1 and y==y1:
        reset = 1
    if x >= x2 and y >= y2 and x <= (x2+40) and y<= (y2+40) and bigman == 1:
        reset = 1
    if x==f and y==e:
        reset = 1

    if move == 1:
        if x1>=x:
            x1 -= 20
            move = floor(random(1,4))
        elif x1<=x:
            x1 += 20
            move = floor(random(1,4))
    elif move == 2:
        if y1>=y:
            y1 -= 20
            move = floor(random(1,4))
        elif y1<=y:
            y1 += 20
            move = floor(random(1,4))
    else:
        move = floor(random(1,3))
    if move2 == 1:
        if x2>=x:
            x2 -= 20
            move2 = floor(random(1,4))
        elif x2<=x:
            x2 += 20
            move2 = floor(random(1,4))
    elif move2 == 2:
        if y2>=y:
            y2 -= 20
            move2 = floor(random(1,4))
        elif y2<=y:
            y2 += 20
            move2 = floor(random(1,4))
    else:
        move2 = floor(random(1,3))
    if i == 1:
        x += 20
    if i == 2:
        y += 20
    if i == 3:
        x -= 20
    if i == 4:
        y -= 20
    if l >= 25:
        delay(50)
        fill (255)
        fill(55,55,55)
        image(racoon,x2,y2,40,40)
        fill (255)
        bigman = 1
        counter -= 1 
    elif l >= 14:
        delay(75)   
        counter -= 1     
    elif l >= 10:
        delay(100)
        counter -= 1 
    elif l >= 7:
        delay(125)
        counter -= 1 
        fill (255)
    else:
        delay(150)
        counter -= 1 
    if counter >= 1:
        if flicker <= 10:
            flicker += 1 
        else:
            flicker = 0 
    else:
         flicker = 0          
    if counter <= 0:
        counter = 0
    if flicker >= 6:
        clear()

def draw():
    global  x,y,i,c,d,e,l,f,g,cl,x1,y1,move,x2,y2,move2,o,m,n,counter,flicker,reset,score,racoon,bigman
    if g == 1:
        clear()
        gameLoop()
    elif g == 2:
        clear()
        textSize(26)
        text ("Game Over",width/2,height/2.2)
        text ("score",width/2,height/1.6)
        textSize(20)
        text (score,width/2,height/1.5)
        textSize(20)
        text ("press g to try agian",width/2,height/1.9)
        textSize(20)
        text ("press i to for instructions",width/2,height/1.7)
    else:
        textAlign(CENTER,CENTER)
        textSize(26)
        text ("SUPER SNAKE",width/2,height/2.1)
        textSize(20)
        text ("press g to start",width/2,height/1.9)
        textSize(20)
        text ("press i to for instructions",width/2,height/1.7)
    if o == 1 and g != 1:
        clear()
        textAlign(CENTER,CENTER)
        textSize(20)
        text ("white square is the fruit that gives",width/3.5,height/3)
        text ("you length when you eat it",width/3.5,height/2.8)
        textSize(20)
        text ("press g to start",width/2,height/1.9)
        text ("move with awsd",width/2,height/1.7)
        text ("pink fruit is the fruit that gives",width/3.5,height/1.5)
        text ("you length when you clicking on it",width/3.5,height/1.45)
        text ("but trying to eat it you lose",width/3.5,height/1.4)
        text ("grey fruit is the fruit that hunts",width/1.5,height/3)
        text ("you and it's to small to eat your",width/1.5,height/2.8)
        text ("body but it can eat your head",width/1.5,height/2.6)
        text ("so be carefull",width/1.5,height/2.4)
        text ("green fruit is the fruit that gives",width/1.5,height/1.5)
        text ("you two length when you eat it",width/1.5,height/1.45)
        text ("but causes your vision to flash",width/1.5,height/1.4)
        fill (255)
        rect(200,220,20,20)
        fill(255,0,255)
        rect(200,500,20,20)
        fill(55,55,55)
        rect(525,220,20,20)
        fill(0,255,0)
        rect(525,500,20,20)
        fill (255)
    if key == "g":
        g = 1
        o = 0
    if key == "i":
        o = 1
    
def keyPressed():
    global x,y,i,c,d,e,l,f,g,cl,x1,y1,move,x2,y2,move2,o,m,n,counter,flicker,reset,score,racoon,bigman
    if key=="d" and i != 3:
        i = 1 
        redraw()  
    if key=="s" and i != 4:
        i = 2
        redraw()
    if key=="a" and i != 1:
        i = 3
        redraw()
    if key=="w" and i != 2:
        i = 4
        redraw()
def mousePressed(): 
    global x,y,i,c,d,e,l,f,g,cl,x1,y1,move,x2,y2,move2,o,m,n,counter,flicker,reset,score,racoon,bigman
    if f <= (mouseX + 20) and e <= (mouseY + 20):
        cl += 1
        f = floor(random(1,40))* 20
        e = floor(random(1,40))* 20
    if cl == 5:
        cl = 0
        l += 1
        d = floor(random(1,40))* 20
        c = floor(random(1,40))* 20
    
 
