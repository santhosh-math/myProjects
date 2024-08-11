import tkinter as tk
from tkinter import messagebox
global count                         #count keep tracks of the no of turns passed by
count=0
def start_menu():
    #Let's create the StartMenu
    root=tk.Tk()
    root.geometry("400x200")
    root.title("TicTacToe!")
    label=tk.Label(text="Player1,Select The Option:")
    label.pack()
    global value
    def start_window():
        global value
        options=['X','O']
        value=tk.StringVar(root)
        value.set("Select X or O")
        menu=tk.OptionMenu(root, value, *options)
        menu.pack()
        submit_button = tk.Button(root, text='Submit', command=lambda:setopt(value.get()))
        submit_button.pack()
    global player1
    def destroyf():
        root.destroy()

    #Function for setting the character to the players
    def setopt(b):
        global player1
        global player2
        global a
        a=b
        player1=b
        if b.lower()=='x':
            player2='O'
        else:
            player2='X'
        destroyf()
        game()

    
    start_window()
start_menu()

#all logics for the game is implemented here
def game():
    #Function to check if the selected cell is empty
    def check_empty(c):
        if x[c['row']][c['column']]==None:
            return 1
        else:
            return 0
    #Function to check who won the game
    def whowin(x):
        if x==player1:
            return "Player1 Won!"
        else:
            return "Player2 Won!"
    #Function to start the game again if requested
    def playagain():
        global count
        ans=messagebox.askyesno("Draw!","Play Again?")
        if ans==1:
            root.destroy()
            count=0
            game()
        else:
            exit()
    #function to check if there is a win or draw
    def check_win():
        global count
        if count==9:
            playagain()
        if x[0][0]==x[0][1]==x[0][2] and not(x[0][0]==x[0][1]==x[0][2]==None):
            c=whowin(x[0][0])
            messagebox.showinfo("showinfo",c)
            playagain()
        elif x[1][0]==x[1][1]==x[1][2] and not(x[1][0]==x[1][1]==x[1][2]==None):
            c=whowin(x[1][0])
            messagebox.showinfo("showinfo",c)
            playagain()
        elif x[2][0]==x[2][1]==x[2][2]and not(x[2][0]==x[2][1]==x[2][2]==None):
            c=whowin(x[2][0])
            messagebox.showinfo("showinfo",c)
            playagain()
        elif x[0][0]==x[1][1]==x[2][2] and not(x[0][0]==x[1][1]==x[2][2]==None):
            c=whowin(x[0][0])
            messagebox.showinfo("showinfo",c)
            playagain()
        elif x[0][2]==x[1][1]==x[2][0] and not (x[0][2]==x[1][1]==x[2][0]==None):
            c=whowin(x[0][2])
            messagebox.showinfo("showinfo",c)
            playagain()
        elif x[0][0]==x[1][0]==x[2][0] and not(x[0][0]==x[1][0]==x[2][0]==None):
            c=whowin(x[0][0])
            messagebox.showinfo("showinfo",c)
            playagain()
        elif x[0][1]==x[1][1]==x[2][1] and not(x[0][1]==x[1][1]==x[2][1]==None):
            c=whowin(x[0][1])
            messagebox.showinfo("showinfo",c)
            playagain()
        elif x[0][2]==x[1][2]==x[2][2] and not(x[0][2]==x[1][2]==x[2][2]==None):
            c=whowin(x[0][2])
            messagebox.showinfo("showinfo",c)
            playagain()
    #Function for placing the player's character in the grid
    def pl(b0):
        global count
        c=b0.grid_info()
        if check_empty(c):
            b0.config(text=a)
            x[c['row']][c['column']]=a
            count+=1
            check_win()
            change()
    #Function to change the turn of the players.
    def change():
        global a
        if a=="X":
            a="O"
        else:
            a="X"
    #code for creating the grid
    x=[[None,None,None],[None,None,None],[None,None,None]]
    root=tk.Tk()
    root.title("TicTacToe!")
    root.geometry("400x400")
    b0=tk.Button(root,text='',command=lambda:pl(b0))
    b1 =tk.Button(root,command=lambda:pl(b1))
    b2 =tk.Button(root,command=lambda:pl(b2))
    b3 =tk.Button(root,command=lambda:pl(b3))
    b4 =tk.Button(root,command=lambda:pl(b4))
    b5 =tk.Button(root,command=lambda:pl(b5))
    b6 =tk.Button(root,command=lambda:pl(b6))
    b7 =tk.Button(root,command=lambda:pl(b7))
    b8 =tk.Button(root,command=lambda:pl(b8))
    b9 =tk.Button(root,command=lambda:pl(b9))
    tk.Grid.rowconfigure(root,0,weight=1)
    tk.Grid.columnconfigure(root,0,weight=1)
    tk.Grid.rowconfigure(root,1,weight=1)
    tk.Grid.columnconfigure(root,1,weight=1)
    tk.Grid.rowconfigure(root,2,weight=1)
    tk.Grid.columnconfigure(root,2,weight=1)
    b0.grid(row=0,column=0,sticky='NSEW')
    b2.grid(row=0,column=1,sticky='NSEW')
    b3.grid(row=0,column=2,sticky='NSEW')
    b4.grid(row=1,column=0,sticky='NSEW')
    b5.grid(row=1,column=1,sticky='NSEW')
    b6.grid(row=1,column=2,sticky='NSEW')
    b7.grid(row=2,column=0,sticky='NSEW')
    b8.grid(row=2,column=1,sticky='NSEW')
    b9.grid(row=2,column=2,sticky='NSEW')
