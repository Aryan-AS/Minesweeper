from tkinter import *
from cell import Cell
import meow
import utils


root = Tk()
root.configure(bg="black")
root.geometry(f'{meow.WIDTH}x{meow.HEIGHT}')
root.title("Meow Swipper")
root.resizable(False,False)

top_frame = Frame(
    root,
    bg="snow",
    width=meow.WIDTH,
    height= utils.height_prct(25)

)
top_frame.place(x=0,y=0)
left_frame = Frame(
    root,
    bg="green2",
    width=utils.width_prct(25),
    height=utils.height_prct(75)

)
left_frame.place(x=0,y=utils.height_prct(25))
centre_frame = Frame(
    root,
    bg="plum2",
    width=utils.width_prct(75),
    height= utils.height_prct(75)

)
centre_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))
c1 = Cell()
c1.create_button(centre_frame)

c1.cell_button.grid(column=0,row=0)

c2 = Cell()
c2.create_button(centre_frame)

c2.cell_button.grid(column=0,row=1)
root.mainloop()