import sys
import settings
import random as rd
from tkinter import Button, Label
from abstract_cell import AbstractCell
import ctypes


class Cell(AbstractCell):
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_ohject = None
        self.x = x
        self.y = y

        # Append the object  to the cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_actions)  # left click
        btn.bind('<Button-3>', self.right_click_actions)  # right click
        self.cell_btn_ohject = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cell left: {Cell.cell_count}",
            font=("", 24)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self):
        # print("I am left clicked!")
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # if mine count is equal to the cells left count, player won
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game over', 0)

        # cancel left and right click events if cell is already opened:
        self.cell_btn_ohject.unbind('<Button-1>')
        self.cell_btn_ohject.unbind('<Button-3>')

    def get_cell_by_axits(self, x, y):
        # return  a cell object based on the value og x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axits(self.x-1, self.y-1),
            self.get_cell_by_axits(self.x-1, self.y),
            self.get_cell_by_axits(self.x-1, self.y+1),
            self.get_cell_by_axits(self.x, self.y-1),
            self.get_cell_by_axits(self.x+1, self.y-1),
            self.get_cell_by_axits(self.x+1, self.y),
            self.get_cell_by_axits(self.x+1, self.y+1),
            self.get_cell_by_axits(self.x, self.y+1)
        ]
        cells = [
            cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            # print(self.surrounded_cells_mines_length)
            self.cell_btn_ohject.configure(text=self.surrounded_cells_mines_length)
            # replance the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cell left: {Cell.cell_count}"
                )
            # if this was a mine candidate, then for safety, we should
            # configure the background color to SystemButtonFace
            self.cell_btn_ohject.configure(
                bg='SystemButtonFace'
            )
        # Mark the cell as opened (use is as the last line of this method)
        self.is_opened = True

    def show_mine(self):
        # Cell.cell_count -= 1

        self.cell_btn_ohject.configure(bg='red')
        # a logic do interrupt the game and display a message that player lost!
        ctypes.windll.user32.MessageBoxW(0, 'You click on a mine', 'Game over', 0)

        sys.exit()

    def right_click_actions(self):
        if not self.is_mine_candidate:
            self.cell_btn_ohject.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_ohject.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        pick_cells = rd.sample(
            Cell.all, settings.MINES_COUNT
        )
        for pick_cell in pick_cells:
            pick_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
