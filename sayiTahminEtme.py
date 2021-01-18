from tkinter import *
from random import randint
from time import sleep
from time import sleep
from array import *

root = Tk()
root.title("Memory game")

myButton = Button(root, text="Start game", fg="white", bg="purple")

userInput = StringVar()
result = ""

counter = 5
i = 0
level = 1
strLevelText = 'Your level: ' + str(level)


def getInput():
    global counter, i, level, strLevelText

    result = str(userInput.get())
    print("Your input "+result)
    if result == generatedNumbers:
        print("Correct")
        counter += 1
        #print(counter)
        i = 0
        #print(i)
        level += 1
        labelUserInput.place_forget()
        girdi.place_forget()
        btnGetUserInput.place_forget()
        userInput.set('')
        strLevelText = ("You won - Your level is now :  " + str(level))
       # print(level)
        tus()


    else:
        print("False")
        counter = 5
       # print(counter)
        i = 0
       # print(i)
        level = 1
        labelUserInput.place_forget()
        girdi.place_forget()
        btnGetUserInput.place_forget()
        userInput.set('')
        strLevelText = ("You lost! - You start with level " + str(level))
        #print(level)
        tus()



labelUserInput = Label(root, text="Enter your result: ", font=("arial", 12, "bold"), fg="black")
girdi = Entry(root, width=20, borderwidth=5, textvariable=userInput)
btnGetUserInput = Button(root, text="Enter", fg="white", bg="red", command=getInput)

def tus():
    myButton.pack_forget()
    labelLevelHeader = Label(root, text=strLevelText, font=("arial", 12, "bold"), bg="black", fg="white").place(x=10, y=10)
    arrRandomNo = []
    global counter
    global i

    while i != counter:
            for i in range(counter):
                arrRandomNo.append(randint(0, 9))
                sayi = Label(root, text=arrRandomNo[i], fg="black", bg="grey", width=2, height=2)
                sayi.place(x=randint(50, 100), y=randint(50, 100))
                root.update()
                sleep(1)
                sayi.place_forget()
                i += 1
        # display array output as a string
            print(arrRandomNo)
            global generatedNumbers
            generatedNumbers = ''.join(str(e) for e in arrRandomNo)
            print("Result: " + generatedNumbers)
          #  print(counter)
           # print(i)

            labelUserInput.place(x=80, y=80)
            girdi.place(x=80, y=110)
            btnGetUserInput.place(x=120, y=150)



myButton.config(command=tus)
myButton.pack(padx=110, pady=110)

root.mainloop()

