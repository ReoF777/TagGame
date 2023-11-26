import random
import tkinter 

playerX = 0
playerY = 0
playerPos = []
playerPos.append([playerX, playerY])
appleX = 9
appleY = 9
Point = 0
key = ""

def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ""
    
def checkPos():
    global playerX, playerY
    if playerX > 9 or playerX < 0 or playerY > 9 or playerY < 0:
        if playerX > 9:
            playerX = 9
            
        if playerX < 0:
            playerX = 0
            
        if playerY > 9:
            playerY = 9
            
        if playerY < 0:
            playerY = 0
        
        canvas.create_rectangle(60*playerX, 60*playerY, 60*playerX+60, 60*playerY+60, fill="pink", outline="blue", width=5)
        root.after(80, keyDown)
        return False
    else:
        return True
    
def keyDown():
    global playerX, playerY,appleX, appleY, key, Point
    canvas.create_rectangle(60*playerX, 60*playerY, 60*playerX+60, 60*playerY+60, fill="white", outline="blue", width=5)
    
    if key == "Q" or key == "q": # Qを押すと終了
        root.destroy()
        return
    
    if checkPos() == False:
        return
    
    # appleを移動
    canvas.create_rectangle(60*appleX, 60*appleY, 60*appleX+60, 60*appleY+60, fill="skyblue", outline="blue", width=5)
    tmp = random.randint(0, 4)
    if tmp == 0 and appleX < 9:
        appleX = appleX + 1
    elif tmp == 1 and appleX > 0:
        appleX = appleX - 1
    elif tmp == 2 and appleY < 9:
        appleY = appleY + 1
    elif tmp == 3 and appleY > 0:
        appleY = appleY - 1
    
    canvas.create_rectangle(60*appleX, 60*appleY, 60*appleX+60, 60*appleY+60, fill="red", outline="blue", width=5)
    
    canvas.create_rectangle(60*playerX, 60*playerY, 60*playerX+60, 60*playerY+60, fill="skyblue", outline="blue", width=5)
    
    if key == "Up" or key == "w":
        playerY = playerY - 1
    elif key == "Down" or key == "s":
        playerY = playerY + 1
    elif key == "Left" or key == "a":
        playerX = playerX - 1
    elif key == "Right" or key == "d":
        playerX = playerX + 1
    
    if playerX == appleX and playerY == appleY:
        Point = Point + 50
        playerPos.append([playerX, playerY])
        appleX = random.randint(0, 9)
        appleY = random.randint(0, 9)
        if appleX == playerX and appleY == playerY:
            appleX = 0 if appleX == 9 else 9
            appleY = 0 if appleY == 9 else 9
            
        canvas.create_rectangle(60*appleX, 60*appleY, 60*appleX+60, 60*appleY+60, fill="red", outline="blue", width=5)
        
    canvas.create_rectangle(60*playerX, 60*playerY, 60*playerX+60, 60*playerY+60, fill="pink", outline="blue", width=5,)
    
    canvas.delete("point_text")
    point_text = f"Point: {Point}"
    canvas.create_text(300, 10, anchor="nw", text=point_text, font={"Arial", 50}, tag="point_text")
    root.after(80, keyDown)
    

root = tkinter.Tk()
root.geometry("600x600")
root.title("Maze Game")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tkinter.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

canvas.create_rectangle(60*playerX, 60*playerY, 60*playerX+60, 60*playerY+60, fill="pink", outline="blue", width=5)
for i in range(10):
    for j in range(10):
        if i != playerX or j != playerY:
            canvas.create_rectangle(60*j, 60*i, 60*j+60, 60*i+60, fill="skyblue", outline="blue", width=5)
        
canvas.create_rectangle(60*playerX, 60*playerY, 60*playerX+60, 60*playerY+60, fill="pink", outline="blue", width=5)
canvas.create_rectangle(60*appleX, 60*appleY, 60*appleX+60, 60*appleY+60, fill="red", outline="blue", width=5)
root.after(80, keyDown)
root.mainloop()
