import os.path
import random
import tkinter as tk


def randomdish():
    frameAddDish.grid_forget()
    frameViewFile.grid_forget()
    frameRandomizeDish.grid(row=1, column=0)


def randomizedish():
    print("this doesnt work")
    file = open("Food-randomizer/test.txt", "rt")
    fileLines = file.read().split("\n")
    potentialDishes = []
    print(len(entryRandomStyle.get()))

    file.close()


def adddish():
    frameViewFile.grid_forget()
    frameRandomizeDish.grid_forget()
    frameAddDish.grid(row=1, column=0)


def storedish():
    if not entryAddNameOfDish.get():
        labelAddDishError.config(fg="red", text="The name field is empty")
        return
    if not entryAddStyleOfDish.get():
        labelAddDishError.config(fg="red", text="The style field is empty")
        return

    if not entryAddRatingOfDish.get():
        labelAddDishError.config(fg="red", text="The rating field is empty")
        return
    if not entryAddRatingOfDish.get().isnumeric():
        labelAddDishError.config(fg="red", text="The rating field contains a non number")
        return
    if int(entryAddRatingOfDish.get()) > 5:
        labelAddDishError.config(fg="red", text="The rating is above 5")
        return
    
    if not entryAddTimeToCook.get():
        labelAddDishError.config(fg="red", text="The time to cook field is empty")
        return
    if not "." in entryAddTimeToCook.get():
        labelAddDishError.config(fg="red", text="The time to cook field doesnt contain a period")
        return
    
    timeToCookList = entryAddTimeToCook.get().split(".")

    if len(timeToCookList) > 3:
        labelAddDishError.config(fg="red", text="There are too many periods in the time to cook field")
        return
    if not timeToCookList[0].isnumeric():
        labelAddDishError.config(fg="red", text="There are not just numbers inbetween the periods in the time to cook field")
        return
    if not timeToCookList[1].isnumeric():
        labelAddDishError.config(fg="red", text="There are not just numbers inbetween the periods in the time to cook field")
        return
    if not timeToCookList[2].isnumeric():
        labelAddDishError.config(fg="red", text="There are not just numbers inbetween the periods in the time to cook field")
        return
    
    timeToCook = int(timeToCookList[0]) * 1440 + int(timeToCookList[1]) * 60 + int(timeToCookList[2])

    file = open("Food-randomizer/test.txt", "at")
    file.write(entryAddNameOfDish.get() + "." + entryAddStyleOfDish.get() + "." + entryAddRatingOfDish.get() + "." + str(timeToCook) + "\n")
    file.close()

    entryAddNameOfDish.delete(first=0, last=tk.END)
    entryAddStyleOfDish.delete(first=0, last=tk.END)
    entryAddRatingOfDish.delete(first=0, last=tk.END)
    entryAddTimeToCook.delete(first=0, last=tk.END)

    labelAddDishError.config(fg="green", text="Dish successfully added")


def viewfile():
    frameRandomizeDish.grid_forget()
    frameAddDish.grid_forget()
    frameViewFile.grid(row=1, column=0)
    textViewFile.delete("1.0", tk.END)
    file = open("Food-randomizer/test.txt", "rt")
    textViewFile.insert(tk.END, file.read())
    file.close()


def savefile():
    #file = open("Food-randomizer/test.txt", "wt")
    #file.write(textViewFile.get("1.0", tk.END))
    #file.close
    print("This button is broken")

# create the window
window = tk.Tk()
window.title("Fuud")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

# create the tk frames
frameTopRow = tk.Frame(window, relief=tk.RAISED, bd=2)
frameAddDish = tk.Frame(window)
frameViewFile = tk.Frame(window)
frameRandomizeDish = tk.Frame(window)

frameTopRow.grid(row=0, column=0, sticky="ew")

# create the top row widgets
buttonRandomDish = tk.Button(frameTopRow, text="Random dish", command=randomdish)
buttonAddDish = tk.Button(frameTopRow, text="Add dish", command=adddish)
buttonViewFile = tk.Button(frameTopRow, text="View file", command=viewfile)

buttonRandomDish.grid(row=0, column=0, sticky="ew")
buttonAddDish.grid(row=0, column=1, sticky="ew")
buttonViewFile.grid(row=0, column=2, sticky="ew")

# create the randomized dish screen
labelRandomizedDish = tk.Label(frameRandomizeDish)
buttonRandomizeDish = tk.Button(frameRandomizeDish, text="Randomize dish", command=randomizedish)

entryRandomRating = tk.Entry(frameRandomizeDish)
entryRandomStyle = tk.Entry(frameRandomizeDish)
entryRandomTime = tk.Entry(frameRandomizeDish)
labelRandomRating = tk.Label(frameRandomizeDish, text="Minimum rating of dish")
labelRandomStyle = tk.Label(frameRandomizeDish, text="Required style of dish")
labelRandomTime = tk.Label(frameRandomizeDish, text="Maximum amount of time to cook DAYS.HOURS.MINUTES")

entryRandomRating.grid(row=0, column=1, padx=2, pady=2)
entryRandomStyle.grid(row=1, column=1, padx=2, pady=2)
entryRandomTime.grid(row=2, column=1, padx=2, pady=2)
labelRandomRating.grid(row=0, column=0, padx=2, pady=2)
labelRandomStyle.grid(row=1, column=0, padx=2, pady=2)
labelRandomTime.grid(row=2, column=0, padx=2, pady=2)

labelRandomizedDish.grid(row=3, column=0, sticky="nsew")
buttonRandomizeDish.grid(row=2, column=3)

# create the add dish screen
entryAddNameOfDish = tk.Entry(frameAddDish)
entryAddRatingOfDish = tk.Entry(frameAddDish)
entryAddStyleOfDish = tk.Entry(frameAddDish)
entryAddTimeToCook = tk.Entry(frameAddDish)

labelAddNameOfDish = tk.Label(frameAddDish, text="Name of dish")
labelAddRatingOfDish = tk.Label(frameAddDish, text="Rating of dish out of 5")
labelAddStyleOfDish = tk.Label(frameAddDish, text="Style of dish")
labelAddTimeToCook = tk.Label(frameAddDish, text="Time to cook dish DAYS.HOURS.MINUTES")

buttonStoreDish = tk.Button(frameAddDish, text="Add dish", command=storedish)
labelAddDishError = tk.Label(frameAddDish)

entryAddNameOfDish.grid(row=0, column=1, padx=2, pady=2)
entryAddStyleOfDish.grid(row=1, column=1, padx=2, pady=2)
entryAddRatingOfDish.grid(row=2, column=1, padx=2, pady=2)
entryAddTimeToCook.grid(row=3, column=1, padx=2, pady=2)

labelAddNameOfDish.grid(row=0, column=0, padx=2, pady=2)
labelAddStyleOfDish.grid(row=1, column=0, padx=2, pady=2)
labelAddRatingOfDish.grid(row=2, column=0, padx=2, pady=2)
labelAddTimeToCook.grid(row=3, column=0, padx=2, pady=2)

buttonStoreDish.grid(row=3, column=2, padx=2, pady=2)
labelAddDishError.grid(row=4, column=0, columnspan=3)

# create the view file screen
textViewFile = tk.Text(frameViewFile)
buttonSaveFile = tk.Button(frameViewFile, text="Save", command=savefile)

textViewFile.grid(row=0, column=0)
buttonSaveFile.grid(row=0, column=1, sticky="s", padx=5, pady=5)

# coggers
window.mainloop()
