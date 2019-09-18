# import tkinter

# # width = 20
# # height = 20
# window = tkinter.Tk()
# window.geometry("500x400")
# window.resizable(0, 0) # this prevents from resizing the window

# # to rename the title of the window
# window.title("EZ Sokoban")
# # pack is used to show the object in the window
# label = tkinter.Label(window, text = "Easy Sokoban", font = "2005_iannnnnCPU.ttf",).pack()

# # # creating 2 frames TOP and BOTTOM
# top_frame = tkinter.Frame(window).pack(side = "top")
# bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# wid = tkinter.Label(top_frame, text = "WIDTH :").pack(side = "left") # this is placed in 0 0
# # 'Entry' is used to display the input-field
# widEn = tkinter.Entry(top_frame).pack(side = "left") # this is placed in 0 1
# leng = tkinter.Label(top_frame,text = "LENGTH :").pack(side = "left")
# lengEn = tkinter.Entry(top_frame).pack(side = "left") # this is placed in 0 1
# btn4 = tkinter.Button(top_frame, text = " ENTER ", fg = "orange", bg = "black" ).pack(side = "left", fill = "x")


# btn3 = tkinter.Button(bottom_frame, text = "Button2", fg = "purple").pack(fill = "x")# 'side' is used to align the widgets




# window.mainloop()

# import tkinter

# window = tkinter.Tk()
# window.title("GUI")

# # creating 2 frames TOP and BOTTOM
# top_frame = tkinter.Frame(window).pack()
# bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# # now, create some widgets in the top_frame and bottom_frame
# wid = tkinter.Label(top_frame, text = "WIDTH :", fg = "pink").pack(side = "left") # this is placed in 0 0
# widEn = tkinter.Entry(top_frame).pack(side = "left") # this is placed in 0 1
# btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack(side = "left")# 'fg - foreground' is used to color the contents
# btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack(side = "left")# 'text' is used to write the text on the Button


# btn3 = tkinter.Button(bottom_frame, text = "Button2", fg = "purple").pack(side = "left")# 'side' is used to align the widgets
# btn4 = tkinter.Button(bottom_frame, text = "Button2", fg = "orange").pack(side = "left")

# window.mainloop()

try:
    from tkinter import *
except ImportError:
    from Tkinter import *
try:
    from tkinter.filedialog import askopenfilename
except ImportError:
    from tkFileDialog import askopenfilename
try:
    from tkinter.messagebox import *
except ImportError:
    from tkMessageBox import *


"""
    O ... igralec
    # ... zid
    * ... blokec (ki se ga lahko premika)
    X ... tocka za zmago
    A ... igralec na tocki za zmago
    R ... blokec na tocki za zmago
    
"""
import tkinter

def makeLevel(string):
    p = []
    with open(string, 'r') as f:
        for line in f:
            line = line.strip()
            foo = []
            for i in line:
               foo.append(i)
            p.append(foo)
    return p

def findPlayer():
    for i in range(w):
        for j in range(h):
            if(p[j][i] == 'O'):
                return(i,j)

def kvadrat(x, y, barva):
    canvas.create_rectangle(x, y, x+wid, y+hei, fill=barva)

def krog(x, y, barva):
    canvas.create_oval(x, y, x+wid, y+hei, fill=barva)

def draw():
    canvas.delete("all")
    for i in range(wid, width, wid):
        canvas.create_line(i, 0, i, height)

    for i in range(hei, height, hei):
        canvas.create_line(0, i, width, i)

    for i in range(w):
        for j in range(h):
            if(p[j][i] == '#'):
                kvadrat(i*wid, j*hei, "#252525")
            if(p[j][i] == 'O'):
                krog(i*wid, j*hei, "red")
            if(p[j][i] == '*'):
                kvadrat(i*wid, j*hei, "blue")
            if(p[j][i] == 'X'):
                kvadrat(i*wid, j*hei, "yellow")
            if(p[j][i] == 'A'):
                kvadrat(i*wid, j*hei, "yellow")
                krog(i*wid, j*hei, "red")
            if(p[j][i] == 'R'):
                kvadrat(i*wid, j*hei, "pink")
            
            
def kill(event):
    root.destroy()

def odmik(x, y):
    #global ply_y, ply_x
    if(p[y][x] == 'O'):
        p[y][x] = ' '
    if(p[y][x] == 'A'):
        p[y][x] = 'X'

def premik_na(x, y):
    if(p[y][x] == 'X'):
        p[y][x] = 'A'
    if(p[y][x] == ' '):
        p[y][x] = 'O'

def odmik_stvar(x, y):
    if(p[y][x] == '*'):
        p[y][x] = ' '
    if(p[y][x] == 'R'):
        p[y][x] = 'X'
        
def premik_stvar_na(x, y):
    if(p[y][x] == ' '):
        p[y][x] = '*'
    if(p[y][x] == 'X'):
        p[y][x] = 'R'


def premikanje(x, y):
    global ply_y, ply_x
    if(p[ply_y + y][ply_x + x] in dovoljeni):
        odmik(ply_x, ply_y)
        ply_y += y
        ply_x += x
        premik_na(ply_x, ply_y)

    elif(p[ply_y + y][ply_x + x] in premikajoci):
        if(p[ply_y + 2*y][ply_x + 2*x] in dovoljeni):
            odmik_stvar(ply_x + x, ply_y + y)
            premik_stvar_na(ply_x + 2*x, ply_y + 2*y)
            odmik(ply_x, ply_y)
            ply_y += y
            ply_x += x
            premik_na(ply_x, ply_y)
            

def jeZmaga():
    for i in p:
        for j in i:
            if(j == 'X'):
                return False
            elif(j == 'A'):
                return False
    return True

def movement(n):
    global ply_x, ply_y

    if(n == 'Up'):
        premikanje(0, -1)

    elif(n == 'Down'):
        premikanje(0, 1)

    elif(n == 'Left'):
        premikanje(-1, 0)

    elif(n == 'Right'):
        premikanje(1, 0)

    draw()
    if(jeZmaga()):
        showinfo("You won!", "Congratulations, you won!")
        root.destroy()
    
    

def restart():
    global p
    global ply_x, ply_y
    p = makeLevel(level)
    ply_x, ply_y = findPlayer()
    draw()
    
    
# def startMove(event):
#     for()
#         keyHandler(event)

def keyHandler(event):
    foo = event.keysym
    print(foo)
    movement(foo)
    if(event.char == 'r'):
        restart()


def askLevel():
    top = Tk()
    top.withdraw()
    level = askopenfilename(initialdir = "level", filetypes = [('Level files', '.lvl'), ('All files', '.*')], title = "Choose the level you want to play")
    top.destroy()

    try:
        return(makeLevel(level))
    except IOError:
        top = Tk()
        top.withdraw()
        if(askretrycancel("Error!", "There was an error trying to open your level. Do you want to try again?")):           
            try:
                return(askLevel())
            finally:
                top.destroy()
        else:
            top.destroy()
            return(False)


R,C = input("Enter Map's size (RxC) : ").split('x')
R,C = int(R),int(C)

p = [[' '] * C for i in range(R)]
for i in range(R):
    p[i][:C]=input()
    if len(p[i]) > C:
      print("out range !!!")
      break

if(not p):
    pass
else:
    w = len(p[0])
    h = len(p)

    dovoljeni = [' ', 'X']
    premikajoci = ['*', 'R']


    max_width = 1000
    max_height = 1000


    wid = hei = 50

    if(wid*w > max_width or hei*h > max_height):
        wid = hei = min(max_width//w, max_height//h)
    width = wid * w
    height = hei * h



    ply_x, ply_y = findPlayer()


    root = Tk()
    root.title("Easy Sokoban")
    root.focus_force()
    label = tkinter.Label(root, text = "Easy Sokoban", font = "2005_iannnnnCPU.ttf",).grid(row = 0)
    canvas = Canvas(root, width=width, height=height)
    canvas.grid(row = 1)
    draw()

    root.bind_all("<Escape>", kill)
    root.bind_all("<Key>", keyHandler)
    # root.bind_all("<Space>", startMove)

    root.mainloop()
