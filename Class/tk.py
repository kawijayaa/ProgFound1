from tkinter import *

class ProcessButton:
    def __init__(self):
        window = Tk()
        label = Label(window, text=count)
        btInc = Button(window, text="Increment", bg="cyan", command=self.increase)
        btDec = Button(window, text="Decrement", bg="yellow", command=self.decrease)
        label.pack()
        btInc.pack()
        btDec.pack()

        window.mainloop()

    def increase(self):
        count += 1
    def decrease(self):
        count -= 1

ob = ProcessButton()