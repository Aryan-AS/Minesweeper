from tkinter import Button
class Cell:
 def __init__(self,is_mine=False):
    self.is_mine = is_mine
    self.cell_button = None

 def create_button(self, location):
   btn = Button(
     location,
     text = "TEXT"
   )
   self.cell_button = btn