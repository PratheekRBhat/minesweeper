from tkinter import *
from tkmacosx import Button   #Library to make changes to buttons on macOSX
import settings
import random


class Cell:
  all = []

  def __init__(self, x, y, is_mine=False):
      self.is_mine = is_mine
      self.cell_btn_object = None
      self.x = x
      self.y = y

      #Append object to all
      Cell.all.append(self)
  
  def create_btn_object(self, location):
    btn = Button(
      location,
      width=120,
      height=80
    )
    btn.bind('<Button-1>', self.left_click_actions) # Left mouse click
    btn.bind('<Button-2>', self.right_click_actions)  # Right mouse click
    self.cell_btn_object = btn

  def left_click_actions(self, event):
    if self.is_mine:
      self.show_mine()
    else:
      self.show_cell()
  
  def show_cell(self):
    self.cell_btn_object.configure(text=len(self.surrounding_mines))

  @property
  def surrounding_mines(self):
    surrounding_cells_list = []
    x = self.x
    y = self.y
    for col in range(x-1, x+2):
      for row in range(y-1, y+2):
        if self.is_valid(col, row) and self.get_cell_by_axes(col, row).is_mine:
          surrounding_cells_list.append(self.get_cell_by_axes(col, row))
  
    return surrounding_cells_list

  def is_valid(self, x, y):
    return (x >= 0 and x < settings.GRID_SIZE) and (y >=0 and y < settings.GRID_SIZE) and (x != self.x or y != self.y)

  def get_cell_by_axes(self, x, y):
    for cell in Cell.all:
      if cell.x == x and cell.y == y:
        return cell
  
  def show_mine(self):
    #TODO: Add a logic to end the game.
    self.cell_btn_object.configure(bg="red")

  def right_click_actions(self, event):
    print(event)
    print("The right mouse button was clicked.")

  @staticmethod
  def randomize_mines():
    mine_cells = random.sample(Cell.all, settings.MINES_COUNT)
    for cell in mine_cells:
      cell.is_mine = True

  def __repr__(self):
    return f"Cell({self.x}, {self.y})"