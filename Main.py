from tkinter import *
import random

time = 0
score = 0

def generateExample():
    num = random.randint(2, 4)
    example = ""
    valid = False
    while not valid:
        example = ""
        for i in range(num - 1):
            example += str(random.randint(0, 10))
            example += random.choice(["+", "-", "/", "*"])
        example += str(random.randint(0, 10))
        try:
            solved = eval(example)
            if isinstance(solved, int):
                valid = True
        except:
            pass
    return example


def addDigit(i):
    if i != "-" and len(answerLabel["text"]) < 30 or answerLabel["text"] == "":
        answerLabel['text'] = answerLabel['text'] + i

def deleteDigit():
    answerLabel["text"] = answerLabel["text"][:-1]

def skipExample():
    global score
    score = score - 1
    exampleLabel["text"] = generateExample()
    answerLabel["text"] = ""
    scoreLabel["text"] = "SCORE: " + str(score)

def checkAnswer():
    global score
    if answerLabel["text"] != "":
        if eval(exampleLabel["text"]) == int(answerLabel["text"]):
            answerLabel["text"] = ""
            exampleLabel["text"] = generateExample()
            score = score + 5
            scoreLabel["text"] = "SCORE: " + str(score)

def startLevel():
    global time
    global score
    showLevel()
    time = 30
    score = 0
    scoreLabel["text"] = "SCORE: " + str(score)
    timeLabel["text"] = "TIME: " + str(time)
    answerLabel["text"] = ""
    exampleLabel["text"] = generateExample()
    updateDisplay()

def hideLevel():
    exampleLabel.grid_remove()
    answerLabel.grid_remove()
    for button in buttons:
        button.grid_remove()
    deleteButton.grid_remove()
    enterButton.grid_remove()
    skipButton.grid_remove()
    timeLabel.grid_remove()
    scoreLabel.grid_remove()
    root["bg"] = "#8faef7"
    startButton.place(x=80, y=350)
    resultLabel.place(x=0, y=150)
    resultLabel["text"] = "YOUR SCORE: " + str(score)


def showLevel():
    exampleLabel.grid()
    answerLabel.grid()
    for button in buttons:
        button.grid()
    deleteButton.grid()
    enterButton.grid()
    skipButton.grid()
    timeLabel.grid()
    scoreLabel.grid()
    root["bg"] = "yellow"
    startButton.place_forget()
    resultLabel.place_forget()

def updateDisplay():
    global time
    if time == -1:
        hideLevel()
    else:
        timeLabel["text"] = "TIME: " + str(time)
        time = time - 1
        root.after(1000, updateDisplay)

def keysControl(event):
    if event.char.isdigit() or event.char == "-":
        addDigit(event.char)

root = Tk()
root.title("Queezes Calculation")
root.resizable(width=False, height=False)
root.geometry("456x650")

exampleLabel = Label(root, height=3, bg="#d9ebf7",
                     font="Arial 20", text=generateExample())
exampleLabel.grid(columnspan=4, row=1,
                  sticky="ew")

answerLabel = Label(root, height=3, bg="yellow",
                   font="Arial 20")
answerLabel.grid(columnspan=4, row=6,
                 sticky="ew")

buttons = ["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9",
           "0", "-"]

currentColumn = 0
currentRow = 2

for i in range(len(buttons)):
    buttons[i] = Button(root, width=10, height=5, bg="#add4db",
                       text=buttons[i], font="Arial 10",
                        command=lambda x=buttons[i]: addDigit(x))
    buttons[i].grid(column=currentColumn,
                    row=currentRow)

    currentColumn = currentColumn + 1
    if currentColumn > 2:
        currentColumn = 0
        currentRow = currentRow + 1

deleteButton = Button(root, bg="#add4db",
                      font="Arial 10", text="DELETE",
                      command=deleteDigit)
deleteButton.grid(column=2, row=5,
                  sticky="ewns")

enterButton = Button(root, width=22, bg="#add4db",
                     font="Arial 10", text="ENTER",
                     command=checkAnswer)
enterButton.grid(column=3, row=2, rowspan=3,
                 sticky="ns")
skipButton = Button(root, bg="#db5e5e",
                    font="Arial 10", text="SKIP",
                    command=skipExample)
skipButton.grid(column=3, row=5,
                sticky="ewns")

timeLabel = Label(root, height=3, bg="yellow",
                  font="Arial 15")
timeLabel.grid(column=0, columnspan=2, row=0,
               sticky="ew")
scoreLabel = Label(root, height=3, bg="yellow",
                   font="Arial 15")
scoreLabel.grid(column=3, row=0,
                sticky="ew")

startButton = Button(root, height=3, width=25, bg="yellow",
                     text="START", font="Arial 15",
                     command=startLevel)
resultLabel = Label(root, height=5, width=42, bg="#9cf78f",
                    font="Arial 15")

hideLevel()
resultLabel.place_forget()

root.bind("<Return>", lambda event: checkAnswer())
root.bind("<BackSpace>", lambda event: deleteDigit())
root.bind("<space>", lambda event: skipExample())
root.bind("<Key>", keysControl)

root.mainloop()