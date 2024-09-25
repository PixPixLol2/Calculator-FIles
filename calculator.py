import tkinter as tk


    
    
canvas = tk.Tk()

def enterNumber(num):
    entry1.insert(tk.END,str(num))

def enterNumberOne():
    entry1.insert(tk.END,"1")
def enterNumberTwo():
    entry1.insert(tk.END,"2")
def enterNumberThree():
    entry1.insert(tk.END,"3")
def enterNumberFour():
    entry1.insert(tk.END,"4")
def enterNumberFive():
    entry1.insert(tk.END,"5")
def enterNumberSix():
    entry1.insert(tk.END,"6")
def enterNumberSeven():
    entry1.insert(tk.END,"7")
def enterNumberEight():
    entry1.insert(tk.END,"8")
def enterNumberNine():
    entry1.insert(tk.END,"9")
def enterNumberZero():
    entry1.insert(tk.END,"0")
def enterOperationMinus():
    entry1.insert(tk.END, "-")
def enterOperationPlus():
    entry1.insert(tk.END, "+")
def enterOperationDivision():
    entry1.insert(tk.END, "/")
def enterOperationTimes():
    entry1.insert(tk.END, "*")
def enterOperationEqual():
    data = entry1.get()
    entry1.delete(0,tk.END)
    result = eval(data)
    entry1.insert(tk.END, result)
def clearInputBox():
    entry1.delete(0, tk.END)
    
    
entry1 = tk.Entry(canvas)
entry1.grid()
button1 = tk.Button(canvas,text="1",command=lambda: enterNumber(1))
button1.grid(row=1,column=0, sticky="NEWS")
button2 = tk.Button(canvas,text="2",command=lambda: enterNumber(2))
button2.grid(row=1,column=1, sticky="NEWS")
button3 = tk.Button(canvas,text="3",command=lambda: enterNumber(3))
button3.grid(row=1,column=2, sticky="NEWS")
button4 = tk.Button(canvas,text="4",command=lambda: enterNumber(4))
button4.grid(row=2,column=0, sticky="NEWS")
button5 = tk.Button(canvas,text="5",command=lambda: enterNumber(5))
button5.grid(row=2,column=1, sticky="NEWS")
button6 = tk.Button(canvas,text="6",command=lambda: enterNumber(6))
button6.grid(row=2,column=2, sticky="NEWS")
button7 = tk.Button(canvas,text="7",command=lambda: enterNumber(7))
button7.grid(row=3,column=0, sticky="NEWS")
button8 = tk.Button(canvas,text="8", command=lambda: enterNumber(8))
button8.grid(row=3, column=1, sticky="NEWS")
button9 = tk.Button(canvas,text="9", command=lambda: enterNumber(9))
button9.grid(row=3, column=2, sticky="NEWS")
button0 = tk.Button(canvas,text="0", command=lambda: enterNumber(0))
button0.grid(row=3, column=3, sticky="NEWS")
button_equal = tk.Button(canvas,text="=", command=enterOperationEqual)
button_equal.grid(row=5,column=2, sticky="NEWS")
button_plus = tk.Button(canvas,text="+", command=enterOperationPlus)
button_plus.grid(row=1,column=3, sticky="NEWS")
buttonMinus = tk.Button(canvas,text="-", command=enterOperationMinus)
buttonMinus.grid(row=2, column=3, sticky="NEWS")
buttonTimes = tk.Button(canvas,text="*", command=enterOperationTimes)
buttonTimes.grid(row=3, column=3, sticky="NEWS")
buttonDivision = tk.Button(canvas,text="/", command=enterOperationDivision)
buttonDivision.grid(row=4, column=3, sticky="NEWS")
buttonClear = tk.Button(canvas,text="C", command=clearInputBox)
buttonClear.grid(row=4, column=0, sticky="NEWS")


entry1.grid(row=0,column=0,columnspan=4)
button1.grid(row=1,sticky="NEWS")
button2.grid(row=1,column=1, sticky="NEWS")
button_equal.grid(row=1,column=2, sticky="NEWS")
button_equal.grid(row=1,column=3, sticky="NEWS")
button_plus.grid(row=1, column=2, sticky="NEWS")


canvas.mainloop()


#TODO: make better graphics

#NOTES I WAS GIVEN
# 1. Create an Entry widget to display and edit the input.
# 2. Create Button widgets for numbers (e.g., 1 and 2).
# 3. Define a function to handle number button clicks
# - Retrieve the current content of the Entry widget.
# - Clear the Entry widget.
# - Concatenate the current content with the clicked number.
# - Insert the combined text into the Entry widget.
# 4. Create buttons for addition (`+`) and equal (`=`)
# 5. Define a function to handle addition button
# 6. Define a function to insert the numbers 1 and 2
# 7. Define a function to handle equal button:
# - Get the expression