from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Tic Tac Toe Game')
# s

clicked = True
count = 0

#Disable all buttons when there is winners

def computer_move():
    available_buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    empty_buttons = [button for button in available_buttons if button["text"] == " "]

    if empty_buttons:
        # Randomly select an available button and set it to "O"
        computer_choice = random.choice(empty_buttons)
        computer_choice["text"] = "O"
        checkifwon()

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b8.config(state=DISABLED)

#check icheckifwon someone won
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
        computer_move()  # Call the computer's move after the player's move

def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()
    #for O
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "0" and b9["text"] == "0":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()

    elif b3["text"] == "0" and b5["text"] == "X" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo(message="YOU WIN!")
        disable_all_buttons()
def b_click(b):
    global clicked, count

    if b["text"] ==" " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] ==" " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()





#create button
b1 = Button(root, text=" ", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

#create Grid button on our screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

def reset_game():
    global clicked, count, winner

    # Clear the board (reset text and background color)
    b1["text"] = b2["text"] = b3["text"] = " "
    b4["text"] = b5["text"] = b6["text"] = " "
    b7["text"] = b8["text"] = b9["text"] = " "
    b1.config(bg="SystemButtonFace")
    b2.config(bg="SystemButtonFace")
    b3.config(bg="SystemButtonFace")
    b4.config(bg="SystemButtonFace")
    b5.config(bg="SystemButtonFace")
    b6.config(bg="SystemButtonFace")
    b7.config(bg="SystemButtonFace")
    b8.config(bg="SystemButtonFace")
    b9.config(bg="SystemButtonFace")

    # Enable all buttons
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
    b4.config(state=NORMAL)
    b5.config(state=NORMAL)
    b6.config(state=NORMAL)
    b7.config(state=NORMAL)
    b8.config(state=NORMAL)
    b9.config(state=NORMAL)

    # Reset game variables
    clicked = True
    count = 0
    winner = False


reset_button = Button(root, text="Reset", font=("Courier", 20), height=3, width=6, bg="SystemButtonFace", command=reset_game)
reset_button.grid(row=3, column=1)


root.mainloop()