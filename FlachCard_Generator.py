#creating a flash card generator for Python LCA3 
#Divya Singh, 21.04.2026

from tkinter import * 
import sqlite3

Questions=[]
indx=-1
setID=0 

#function to create the database and table if not exists
def create_db():
    conn = sqlite3.connect('D:\\Sem4_Lab\\Python\\Python_Programs\\LCA3\\Python_LCA3_Flashcard-Generator\\flashcard.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS setDirectory(setID INTEGER PRIMARY KEY AUTOINCREMENT, setName TEXT NOT NULL)'
    )
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS flashCardDirectory(QID INTEGER PRIMARY KEY AUTOINCREMENT, Question TEXT NOT NULL, Answer TEXT NOT NULL, setID INTEGER, FOREIGN KEY (setID) REFERENCES setDirectory(setID))'
    )
    
    conn.commit()
    conn.close()

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
        conn = sqlite3.connect('D:\\Sem4_Lab\\Python\\Python_Programs\\LCA3\\Python_LCA3_Flashcard-Generator\\flashcard.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO setDirectory (setName) VALUES((?))', (setName.get(), ))
            conn.commit()
            Label(window1, text=setName.get()+" successfully added to database").pack(pady=10)
        except sqlite3.IntegrityError:
            Label(window1, text="Error") 
        finally: 
            conn.close()

    #deleting the set from the database
    def deleteSetName():
        conn = sqlite3.connect('D:\\Sem4_Lab\\Python\\Python_Programs\\LCA3\\Python_LCA3_Flashcard-Generator\\flashcard.db')
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM setDirectory WHERE setName=?',(setName.get(), ))
            conn.commit()
            Label(window1, text=setName.get()+" successfully deleted from database").pack(pady=10)
        except sqlite3.IntegrityError:
            Label(window1, text="Error").pack(pady=10)
        finally: 
            conn.close()

    Button(window1, text="Submit", command=set_Name).pack(pady=10)
    Button(window1, text="Delete", command=deleteSetName).pack(pady=10)
    Button(window1, text="Return to main menu", command=window1.destroy).pack(pady=10)

#function to create flashcards
def createFlashcards():
    window2=Toplevel(root)
    window2.title("Create flashcards")
    window2.geometry('750x550')
    create_db()
    set_Name=Label(window2, text="Desired set to add/delete flashcards in")
    set_Name.pack(pady=10)
    
    dispText=Label(window2, text="Create your flashcards here: ")
    dispText.pack(pady=10)

    #function to choose set
    def storeFlashcard():
        conn=sqlite3.connect('D:\\Sem4_Lab\\Python\\Python_Programs\\LCA3\\Python_LCA3_Flashcard-Generator\\flashcard.db')
        cursor=conn.cursor()

        try: 
            cursor.execute("SELECT setID FROM setDirectory WHERE setName= ?", (setName.get(), ))
            setID, =cursor.fetchone()
            cursor.execute('INSERT INTO flashCardDirectory (setID, Question, Answer) VALUES(?, ?, ?)', (setID, Question.get(), Ans.get(), ))
            conn.commit()
        except sqlite3.IntegrityError: 
            Label(window2, text="Error").pack(pady=10)
        finally: 
            conn.close()

    Label(window2, text="Enter desired set:").pack(pady=10)
    setName=Entry(window2)
    setName.pack(pady=10)
    
    Label(window2, text="Enter question number:").pack(pady=10)
    Question=Entry(window2)
    Question.pack(pady=10)
    
    Label(window2, text="Enter answer:").pack(pady=10)
    Ans=Entry(window2)
    Ans.pack(pady=10)
    Button(window2, text='Submit', command=storeFlashcard).pack(pady=10)

    Button(window2, text="Return to main menu", command=window2.destroy).pack(pady=10)

#function to open a window to review flashcards
def review_flash_cards():
    window3=Toplevel(root)
    window3.title("Review flash cards")
    window3.geometry('750x550')

    dispText=Label(window3, text="Review your flashcards here")
    dispText.pack(pady=10)
        
    #function to get setid 
    def get_setID():
        conn=sqlite3.connect('D:\\Sem4_Lab\\Python\\Python_Programs\\LCA3\\Python_LCA3_Flashcard-Generator\\flashcard.db')
        cursor=conn.cursor()

        cursor.execute('SELECT setID FROM setDirectory WHERE setName=?', (setName.get(), ))
        result=cursor.fetchone()

        if result: 
            global setID
            setID=result[0]

            cursor.execute('SELECT Question FROM flashCardDirectory WHERE setID=?', (setID,) )
            global Questions
            Questions=[item[0] for item in cursor.fetchall()]
            #print(Questions)
            conn.close()

        else: 
            print("Error")
    
    #function to display question
    def disp_Q_next(): 
        global indx
        if indx<len(Questions):
            indx+=1
            dispText.config(text=Questions[indx])
        else: 
            dispText.config(text="All done!")
        

    def disp_Q_prev(): 
        global indx
        if indx<0:
            dispText.config(text="All done!")
        else:
            indx-=1 
            dispText.config(text=Questions[indx])

        
                
    def disp_Ans():
        conn=sqlite3.connect('D:\\Sem4_Lab\\Python\\Python_Programs\\LCA3\\Python_LCA3_Flashcard-Generator\\flashcard.db')
        cursor=conn.cursor()
        cursor.execute('SELECT Answer FROM flashCardDirectory WHERE Question=? AND setID=?', (Questions[indx], setID, ))
        ans=cursor.fetchone()
        dispText.config(text=ans)
        conn.close()

    setName=StringVar()
    setName.set("Select the set name: ")
    #create a dropwdown for set name, from setname get the set id, then when diplaying questions use the setid and qid, incremment or decrement the qid accordingly
    try: 
        conn=sqlite3.connect('D:\\Sem4_Lab\\Python\\Python_Programs\\LCA3\\Python_LCA3_Flashcard-Generator\\flashcard.db')
        cursor=conn.cursor()

        cursor.execute('SELECT setName FROM setDirectory')
        allSets=[item[0] for item in cursor.fetchall()]
    except sqlite3.InternalError:
        print("Error")
    finally: 
        conn.close()

    OptionMenu(window3, setName, *allSets).pack(pady=10)
    Button(window3, text="Submit", command=get_setID).pack(pady=10)
    Button(window3, text="Previous Question", command=disp_Q_prev).pack(pady=10)
    Button(window3, text="Next Question", command=disp_Q_next).pack(pady=10)
    Button(window3, text="Display Answer", command=disp_Ans).pack(pady=10)
    Button(window3, text="Return to main menu", command=window3.destroy).pack(pady=10)

#creating root window 
root=Tk()
create_db()
#root title &dim
root.title("Flash Card Generator")
root.geometry('750x550')

Label(root, text="Welcome to Flash Card Generator App!").pack(pady=25)
try: 
    conn=sqlite3.connect('D:\\Sem4_Lab\\Python\\Python_Programs\\LCA3\\Python_LCA3_Flashcard-Generator\\flashcard.db')
    cursor=conn.cursor()

    cursor.execute('SELECT setName FROM setDirectory')
    allSets=cursor.fetchall()
except sqlite3.IntegrityError():
    Label(root, text="Error").pack(pady=10)
finally: 
    conn.close()
Label(root, text=allSets).pack(pady=10)

Button(root, text="Click here to edit your flashcard sets", command=create_new_set).pack(pady=5)
Button(root, text="Click here to edit flashcards in your set", command=createFlashcards).pack(pady=5)
Button(root, text="Click here to review your flashcards", command=review_flash_cards).pack(pady=15)
Button(root, text="Exit application", command=root.destroy).pack(pady=10)

#excute tkinter 
root.mainloop()