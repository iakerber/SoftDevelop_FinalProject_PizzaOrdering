'''
This is the beginning of Pizza Ordering App
Ilze Akerbergs, Feb 17, 2024
Module 6
'''

#imports
import tkinter as tk

#Create the main program, the root Window
root = tk.Tk()

#create the title which shows up in the tab of the window
root.title('Pizza Ordering')

#set the window size
root.geometry('640x480+300+300')
root.resizable(False, False)


#change the window background color by configuring root window

root.config(bg = 'light blue')

#widgets

#label main
title = tk.Label(root, text = ('Order your pizzas here'), font="Verdana 16 bold", bg = '#E8EBD2', fg = '#000099')

#define string variables for strings, with label and input field
nameVar = tk.StringVar(root)
nameLabel = tk.Label(root, text = 'Input your name here for ordering: ')
nameInput = tk.Entry(root, textvariable = nameVar)

#define boolean variable for repeat customers 
repeatVar = tk.BooleanVar()
repeatInput = tk.Checkbutton(root, variable = repeatVar, text = 'Check if you are a repeat customer')

#create a spinbox to find out how many pizzas in the order
numVar = tk.IntVar(value = 4)
numLabel = tk.Label(text = 'How many pizzas do you want to order?')
numInput = tk.Spinbox(root, textvariable = numVar, from_= 0, to = 6, increment = 1)

#listbox for the types of pizzas
pizzaVar = tk.StringVar(value = 'Any')
pizzaLabel = tk.Label(root, text = 'What pizza would you like to order?')
pizzaChoices = ('Any', 'Pepperoni', 'Vegetarian', 'Cheese', 'Everything on it')
pizzaInput = tk.OptionMenu(root, pizzaVar, *pizzaChoices)

#radiobutton to find out if they want to purchase anything extra
extrasLabel = tk.Label(root, text = 'Do you wish to purchase anything from our extras menu?')
extrasFrame = tk.Frame(root)
extrasVar = tk.BooleanVar()
extrasYesInput = tk.Radiobutton(extrasFrame, text = 'Yes, please', value = True, variable = extrasVar)
extrasNoInput = tk.Radiobutton(extrasFrame, text = 'No, thank you', value = False, variable = extrasVar)

#submit order
submitBtn = tk.Button(root, text = 'Submit your order')

outputVar = tk.StringVar(value = '')
outputLine = tk.Label(root, textvariable = outputVar, anchor = 'w', justify = 'left')

#geometry of objects inside the window
title.grid(row = 0, columnspan = 3)
nameLabel.grid(row = 1, column = 0)
nameInput.grid(row = 1, column = 1)
#checkbox grid for repeat customer
repeatInput.grid(row = 2, column = 1, columnspan = 2)
#spinbox grid for how many pizzas to order
numLabel.grid(row = 3, sticky = tk.W)
numInput.grid(row = 3, column = 1)

#padx and pady
pizzaLabel.grid(row = 4, columnspan = 2, sticky = tk.W, pady = 10)
pizzaInput.grid(row = 4, columnspan = 2, padx = 25, pady = 10)

#shove it onto the screen
extrasYesInput.pack(side = 'left', fill = 'x', ipadx = 10, ipady = 5)
extrasNoInput.pack(side = 'left', fill = 'x', ipadx = 10, ipady = 5)
extrasLabel.grid(row = 6, columnspan = 2, sticky = tk.W)
extrasFrame.grid(row = 7, columnspan = 2, sticky = tk.W)

#submit button grid
submitBtn.grid(row = 99)
outputLine.grid(row = 100, columnspan = 2, sticky = 'NSEW')

#columnconfigure
root.columnconfigure(1, weight = 1)

#rowconfigure
root.rowconfigure(99, weight = 2)
root.rowconfigure(100, weight = 1)

def on_submit():
    #what happens when the user presses submit
    #Vars all use 'get()'
    name = nameVar.get()
    
    try:
        number = numVar.get()
    except tk.TclError:
        number = 10000

    pizzas = pizzaVar.get()

    repeat = repeatVar.get()
    extras = extrasVar.get()

    message = f'Find out what is the sum of the order and how to input payment information, {name}.\n'

    if not repeat:
        message += 'Welcome to our wonderful pizza store.\n'
    else:
        message += f'Enjoy your {number} {pizzas} pizzas!\n'

    if extras:
        message += 'Thank you for ordering extras'
    else:
        message += 'It is OK not to get any extras. Pizzas alone it is.\n'

    outputVar.set(message)

submitBtn.configure(command = on_submit)

root.mainloop()
