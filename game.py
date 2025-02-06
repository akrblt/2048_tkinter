# 2048
# Ahmet KARABULUT
# creation de jeu 2048
# version 1.0
# date 28.01.2025

from tkinter import *
import tkinter.font

# 2 dimensions list with data


game=[[0,2,4,8],
      [16,32,2048,128],
      [256,512,1024,2048],
      [4096,8192,0,0]]
colors={
    0: "#ffffff",
    2: "#f7e50c",
    4: "#f5d99e",
    8: "#f7ac78",
    16: "#de876a",
    32: "#b35231",
    64: "#a40f26",
    128: "#c1efa8",
    256: "#348109",
    512: "#38761d",
    1024: "#9fc5f8",
    2048: "#6fa8dc",
    4096: "#b4a7d6",
    8192: "#c27ba0" ,
}

# 2 dimensions list (empty, with labels in the future)
labels=[[None,None,None,None],
        [None,None,None,None],
        [None,None,None,None],
        [None,None,None,None]]

dx=10 # horizontal distance between labels
dy=10 # vertical distance between labels

# réaffiche les bons textes et couleurw
def display():
    for line in range(len(game)):
        for col in range(len(game[line])):
            bg_color = colors[game[line][col]]
            if game[line][col] >0:
                labels[line][col].config( text=game[line][col], bg=bg_color , borderwidth=1)
            else:
                labels[line][col].config( text="", bg=bg_color, borderwidth=0)


def pack3(a,b,c):
    if a==0:
        a,b,c=b,c,0
    if b==0:
        b,c=c,0
    if a==b:
        a*=2
        b,c=c,0
    if b==c:
        b*=2
        c=0
    return [a,b,c]


#print(pack3(2, 2, 4))
#print(pack3(0, 2, 2))
#print(pack3(2, 2, 2))
#print(pack3(2, 2, 4))

def pack4(a,b,c,d):
    nm=0
    ''' counter=0
    while a==0 and counter<4:
        a,b,c,d=b,c,d,0
        nm+=1
        counter+=1'''

    if c == 0 and d>0:
        c, d = d, 0
        nm+=1
    if b==0 and c>0:
        b,c,d=c,d,0
        nm+=1
    if a==0 and b>0:
        a,b,c,d =b,c,d,0
        nm += 1

    if a==b and a>0:
        nm+=1
        a*=2
        b,c,d=c,d,0
    if b==c and b>0:
        nm+=1
        b*=2
        c,d=d,0
    if c==d and d>0:
        nm += 1
        c*=2
        d=0

    return [a,b,c,d],nm


print(pack4(0, 0, 0,0))
print(pack4(0, 0, 2,2))
print(pack4(2, 0, 2,2))
print(pack4(2, 2, 2,2))
print(pack4(2, 2, 4,0))

test_datas=[[0,0,0,0],[0,0,0,2],[0,0,2,2]]
test_reponses=[[0,0,0,0,0],[2,0,0,0,3],[4,0,0,3]]




def test():
    for i in range (len(test_datas)):
        data=test_datas[i]
        temp=pack4(data[0],data[1],data[2],data[3])

        for j in range(3):
            if test_reponses[i][j]==temp[j]:
                print("Ok pour le test " )

# Windows creation
win = Tk()
win.geometry("800x480")
win.title('2048')

# Title
lbl_title=Label(win,text="2048", height=3,   font=("Arial", 15))
lbl_title.pack()

frm_main=Frame(win,bd=5, relief="ridge", bg="lightblue")
frm_main.pack()


#ce boucle pour le game
for line in range(len(game)):
    frm= Frame(frm_main)# temporary frame
    frm.pack()

    # labels creation and position (1. Creation 2. position)
    for col in range(len(game[line])):
        # creation without placement
        labels[line][col] = Label (frm, width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15))
        # label positionning in the windows
        labels[line][col].pack (side=LEFT, padx=dx, pady=dy)
        #print(labels[line][col])

display() #texte et couleurs
test()


win.mainloop()
