import os.path
import random
import tkinter as tk


def generaterandomdish():
    frameAddDish.grid_forget()
    frameViewFile.grid_forget()
    file = open("Food-randomizer/test.txt", "rt")
    filelines = file.read().split("\n")
    currentDish = filelines[random.randint(0, len(filelines)-1)].split(".")
    labelRandomizedDish.grid(row=1, column=0)
    labelRandomizedDish.config(text=currentDish[0])
    file.close()


def adddish():
    labelRandomizedDish.grid_forget()
    frameViewFile.grid_forget()
    frameAddDish.grid(row=1, column=0)


def storedish():
    if not entryAddRatingOfDish.get():
        labelAddDishError.config(fg="red", text="The rating field is empty")
        return
    if not entryAddRatingOfDish.get().isnumeric():
        labelAddDishError.config(fg="red", text="The rating field contains a non number")
        return
    if int(entryAddRatingOfDish.get()) > 5:
        labelAddDishError.config(fg="red", text="The rating is above 5")
        return

    labelAddDishError.config(fg="green", text="Dish successfully added")
    entryAddNameOfDish.delete(first=0, last=128)
    entryAddRatingOfDish.delete(first=0, last=128)
    entryAddStyleOfDish.delete(first=0, last=128)

    file = open("Food-randomizer/test.txt", "a")
    file.write(entryAddNameOfDish.get() + "." + entryAddRatingOfDish.get() + "." + entryAddStyleOfDish.get() + "\n")
    file.close()


def viewfile():
    frameViewFile.grid(row=1, column=0)
    textViewFile.delete("1.0", tk.END)
    file = open("Food-randomizer/test.txt", "rt")
    textViewFile.insert(tk.END, file.read())
    file.close()


def savefile():
    file = open("Food-randomizer/test.txt", "wt")
    file.write(textViewFile.get("1.0", tk.END))
    file.close


window = tk.Tk()
window.title("Fuud")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

frameTopRow = tk.Frame(window, relief=tk.RAISED, bd=2)
frameAddDish = tk.Frame(window)
frameViewFile = tk.Frame(window)

buttonRandomDish = tk.Button(frameTopRow, text="Random dish", command=generaterandomdish)
buttonAddDish = tk.Button(frameTopRow, text="Add dish", command=adddish)
buttonViewFile = tk.Button(frameTopRow, text="View file", command=viewfile)
labelRandomizedDish = tk.Label(window)

entryAddNameOfDish = tk.Entry(frameAddDish)
entryAddRatingOfDish = tk.Entry(frameAddDish)
entryAddStyleOfDish = tk.Entry(frameAddDish)

labelAddNameOfDish = tk.Label(frameAddDish, text="Name of dish")
labelAddRatingOfDish = tk.Label(frameAddDish, text="Rating of dish out of 5")
labelAddStyleOfDish = tk.Label(frameAddDish, text="Style of dish")
buttonStoreDish = tk.Button(frameAddDish, text="Add dish", command=storedish)
labelAddDishError = tk.Label(frameAddDish)

textViewFile = tk.Text(frameViewFile)
buttonSaveFile = tk.Button(frameViewFile, text="Save", command=savefile)

buttonRandomDish.grid(row=0, column=0, sticky="ew")
buttonAddDish.grid(row=0, column=1, sticky="ew")
buttonViewFile.grid(row=0, column=2, sticky="ew")
frameTopRow.grid(row=0, column=0, sticky="ew")
labelRandomizedDish.grid(row=1, column=0, sticky="nsew")

entryAddNameOfDish.grid(row=0, column=1, padx=2, pady=2)
entryAddRatingOfDish.grid(row=1, column=1, padx=2, pady=2)
entryAddStyleOfDish.grid(row=2, column=1, padx=2, pady=2)

labelAddNameOfDish.grid(row=0, column=0, padx=2, pady=2)
labelAddRatingOfDish.grid(row=1, column=0, padx=2, pady=2)
labelAddStyleOfDish.grid(row=2, column=0, padx=2, pady=2)
buttonStoreDish.grid(row=2, column=2, padx=2, pady=2)
labelAddDishError.grid(row=3, column=0, columnspan=3)

textViewFile.grid(row=0, column=0)
buttonSaveFile.grid(row=0, column=1, sticky="s", padx=5, pady=5)

window.mainloop()
