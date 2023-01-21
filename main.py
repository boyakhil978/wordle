import os
import os.path
import sys
import random
import tkinter as tk


wordfile = "words.txt"

def choose_random_word(file_name):
    with open(file_name, 'r') as f:
        words = f.read().split()
        return random.choice(words)

correctwordstring = choose_random_word(wordfile)
correctword = tuple(correctwordstring)

root = tk.Tk()
root.geometry("700x600")
root.title("Wordle By Akhil")


entries = [[tk.Entry(root, width=3, font=('Arial',40)) for j in range(6)] for i in range(6)]
submit_button = [tk.Button(root, text="Submit") for i in range(6)] 

for i in range(6):
    for j in range(6):
        statevar = 'normal'
        if i > 0:
            statevar = 'disabled'
        entries[i][j].config(validate='key',state=statevar, validatecommand=(root.register(lambda x: len(x) <= 1), '%P'))


for i in range(6):
    for j in range(6):
        entries[i][j].grid(row=i, column=j, padx=3, pady=3)



submit_button[0].configure(state = 'normal' ,command=lambda: submit_row(0))
submit_button[0].grid(row=0, column=6, sticky="W", padx=10)
submit_button[1].configure(state = 'disabled' ,command=lambda: submit_row(1))
submit_button[1].grid(row=1, column=6, sticky="W", padx=10)
submit_button[2].configure(state = 'disabled' ,command=lambda: submit_row(2))
submit_button[2].grid(row=2, column=6, sticky="W", padx=10)
submit_button[3].configure(state = 'disabled' ,command=lambda: submit_row(3))
submit_button[3].grid(row=3, column=6, sticky="W", padx=10)
submit_button[4].configure(state = 'disabled' ,command=lambda: submit_row(4))
submit_button[4].grid(row=4, column=6, sticky="W", padx=10)
submit_button[5].configure(state = 'disabled' ,command=lambda: submit_row(5))
submit_button[5].grid(row=5, column=6, sticky="W", padx=10)


def submit_row(row):
    global correctword
    word=''
    submit_button[row].configure(state='disabled')
    if row !=5:
        submit_button[row+1].configure(state='normal')
        
    for col in range(6):
        char = entries[row][col].get()
        if char == "":
            char = " "
        word = word + char
    word = tuple(word.lower())

    def check(word,correctword):
        x=0
        correctwordl = list(correctword)
        for i in word:
            letter = correctwordl.pop(0)
            if i == letter:
                entries[row][x].configure(disabledbackground='green',disabledforeground='black')
            else:
                entries[row][x].configure(disabledbackground='red',disabledforeground='black')
            if i in correctword and not(i == letter):
                entries[row][x].configure(disabledbackground='yellow',disabledforeground='black')
            x=x+1
            
    check(word,correctword)
    if word == correctword:
        win = tk.Tk()
        win.geometry('300x300')
        win.eval('tk::PlaceWindow . center')
        l1 = tk.Label(win,text = 'You Win!!')
        l1.pack()

    if row == 5 and word != correctword:
        lose = tk.Tk()
        lose.geometry('300x300')
        lose.eval('tk::PlaceWindow . center')
        l1 = tk.Label(lose,text = ('You Lose the actual word is '+correctwordstring+'!!'))
        l1.pack()
    
    for j in range(6):
        entries[row][j].configure(state='disabled')
        if row != 5:
            entries[row+1][j].configure(state = 'normal')                               

root.mainloop()








