from tkinter import *
from cell import Cell

import settings
import utils


root = Tk()
# override the setting of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',  # change later to black
    width=settings.WIDTH,
    height=utils.height_prct(25)
)


top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper game',
    font=('', 48)
)
game_title.place(
    x=utils.width_prct(25),
    y=0
)

left_frame = Frame(
    root,
    bg='black',  # change later to black
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',  # change later to black
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

# btn1 = Button(
#     center_frame,
#     bg='blue',
#     text='First Button'
# )
# btn1.place(x=0, y=0)

# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_ohject.grid(
#     column=0,
#     row=0
# )

# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_ohject.grid(
#     column=0,
#     row=1
# )

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_ohject.grid(
            column=x,
            row=y
        )
# print(Cell.all)

#  Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,
    y=0
)


Cell.randomize_mines()
for c in Cell.all:
    print(c.is_mine)
# run window
root.mainloop()
