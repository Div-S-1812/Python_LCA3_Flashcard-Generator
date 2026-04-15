#creating a flash card generator for Python LCA3 
#Divya Singh, 15.04.2026

from tkinter import * 

#function to open window to create a new flashcard set 
def create_new_set():
    window1=Toplevel(root)
    window1.title("Create new set")
    window1.geometry('750x550')
    Label(window1, text="Create a new set of flashcards").pack(pady=10)
    Button(window1, text="Return to main menu", command=window1.destroy).pack(pady=10)
  
#function to open a window to review flashcards
def review_flash_cards():
    window2=Toplevel(root)
    window2.title("Review flash cards")
    window2.geometry('750x550')
    Label(window2, text="Review your flashcards here").pack(pady=10)
    Button(window2, text="Return to main menu", command=window2.destroy).pack(pady=10)

#creating root window 
root=Tk()

#root title &dim
root.title("Flash Card Generator")
root.geometry('750x550')

Label(root, text="Welcome to Flash Card Generator App!").pack(pady=25)
Label(root, text="Here will display existing flashcard sets").pack(pady=10)

Button(root, text="Click here to generate new flashcard set", command=create_new_set).pack(pady=5)
Button(root, text="Click here to review your flashcards", command=review_flash_cards).pack(pady=15)
Button(root, text="Exit application", command=root.destroy).pack(pady=10)
#excute tkinter 
root.mainloop()