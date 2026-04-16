#creating a flash card generator for Python LCA3 
#Divya Singh, 16.04.2026

from tkinter import * 
import sqlite3


#function to open window to create a new flashcard set 
def create_new_set():
    window1=Toplevel(root)
    window1.title("Create new set")
    window1.geometry('750x550')
    dispText=Label(window1, text="Edit your sets of flashcards")
    dispText.pack(pady=10)
    Label(window1, text="Enter the desired name of your set: ").pack(pady=5)

    setName=Entry(window1)
    setName.pack(pady=10)

    #storing the name of set in the database
    def set_Name():
        dispText.config(text=setName.get())

    #deleting the set from the database
    def deleteSetName():
        txt=setName.get()+" successfully deleted"
        dispText.config(text=txt)

    Button(window1, text="Submit", command=set_Name).pack(pady=10)
    Button(window1, text="Delete", command=deleteSetName).pack(pady=10)
    Button(window1, text="Return to main menu", command=window1.destroy).pack(pady=10)

#function to create flashcards
def createFlashcards():
    window2=Toplevel(root)
    window2.title("Create flashcards")
    window2.geometry('750x550')

    set_Name=Label(window2, text="Desired set to add/delete flashcards in")
    set_Name.pack(pady=10)
    
    dispText=Label(window2, text="Create your flashcards here: ")
    dispText.pack(pady=10)

    #function to choose set
    def enterSet():
        set_Name.config(text=setName.get())
    #function to store question 
    def storeQ():  
        dispText.config(text=Question.get())

    #function to store answer
    def storeAns():
        dispText.config(text=Ans.get())

    Label(window2, text="Enter desired set:").pack(pady=10)
    setName=Entry(window2)
    setName.pack(pady=10)
    Button(window2, text="Submit", command=enterSet).pack(pady=10)

    Label(window2, text="Enter question number:").pack(pady=10)
    Question=Entry(window2)
    Question.pack(pady=10)
    Button(window2, text="Submit", command=storeQ).pack(pady=10)

    Label(window2, text="Enter answer:").pack(pady=10)
    Ans=Entry(window2)
    Ans.pack(pady=10)
    Button(window2, text='Submit', command=storeAns).pack(pady=10)

    Button(window2, text="Return to main menu", command=window2.destroy).pack(pady=10)
#function to open a window to review flashcards
def review_flash_cards():
    window3=Toplevel(root)
    window3.title("Review flash cards")
    window3.geometry('750x550')

    dispText=Label(window3, text="Review your flashcards here")
    dispText.pack(pady=10)
    
    #function to display question
    def disp_Q_next(): 
        dispText.config(text="You have reached the next Q")

    def disp_Q_prev(): 
        dispText.config(text="You have reached the previous Q")
        
    def disp_Ans():
        dispText.config(text="This is the answer")

    Button(window3, text="Previous Question", command=disp_Q_prev).pack(pady=10)
    Button(window3, text="Next Question", command=disp_Q_next).pack(pady=10)
    Button(window3, text="Display Answer", command=disp_Ans).pack(pady=10)
    Button(window3, text="Return to main menu", command=window3.destroy).pack(pady=10)

#creating root window 
root=Tk()

#root title &dim
root.title("Flash Card Generator")
root.geometry('750x550')

Label(root, text="Welcome to Flash Card Generator App!").pack(pady=25)
Label(root, text="Here will display existing flashcard sets").pack(pady=10)

Button(root, text="Click here to edit your flashcard sets", command=create_new_set).pack(pady=5)
Button(root, text="Click here to edit flashcards in your set", command=createFlashcards).pack(pady=5)
Button(root, text="Click here to review your flashcards", command=review_flash_cards).pack(pady=15)
Button(root, text="Exit application", command=root.destroy).pack(pady=10)
#excute tkinter 
root.mainloop()