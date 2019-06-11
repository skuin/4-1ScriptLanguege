import game_framework
import data
from tkinter import *

name = "StartState"

def enter():
    pass

def update():
    pass

def exit():
    window.destroy()
    pass

def process_next():
    game_framework.change_state(data)

def run():
    global window
    window = Tk()
    window.title('병원 정보 서비스')
    window.geometry('550x550')  # width x height + 가로격자+세로격자

    map = 'hospitalMain.png'
    img = PhotoImage(file=map)

    map_label = Label(window, image=img)
    map_label.place(x=15, y=10)
    button1 = Button(window,text="병원 조회",command = process_next)
    button1.place(x=240,y=510)

    window.mainloop()




