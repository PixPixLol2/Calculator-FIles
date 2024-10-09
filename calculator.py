import tkinter as tk


    
    
canvas = tk.Tk()
canvas.geometry("150x100")




    

def ENTER_NUMBER(num):
    Equation_entry.insert(tk.END,str(num))

def enterOperationMinus():
    Equation_entry.insert(tk.END, "-")
def enterOperationPlus():
    Equation_entry.insert(tk.END, "+")
def enterOperationDivision():
    Equation_entry.insert(tk.END, "/")
def enterOperationTimes():
    Equation_entry.insert(tk.END, "*")
def enterOperationEqual():
    data = Equation_entry.get()
    Equation_entry.delete(0,tk.END)
    result = eval(data)
    Equation_entry.insert(tk.END, result)
def clearInputBox():
    Equation_entry.delete(0, tk.END)
    
    
Equation_entry = tk.Entry(canvas)
#------------------------------------
button1 = tk.Button(canvas,
    text="1", 
    command=lambda: ENTER_NUMBER(1))
#-------------------------------------
button2 = tk.Button(canvas,
    text="2",
    command=lambda: ENTER_NUMBER(2))
#-------------------------------------
button3 = tk.Button(canvas,
    text="3",
    command=lambda: ENTER_NUMBER(3))
#-------------------------------------
button4 = tk.Button(canvas,
    text="4",
    command=lambda: ENTER_NUMBER(4))
#-------------------------------------
button5 = tk.Button(canvas,
    text="5",
    command=lambda: ENTER_NUMBER(5))
#-------------------------------------
button6 = tk.Button(canvas,
    text="6",
    command=lambda: ENTER_NUMBER(6))
#-------------------------------------
button7 = tk.Button(canvas,
    text="7",
    command=lambda: ENTER_NUMBER(7))
#-------------------------------------
button8 = tk.Button(canvas,
    text="8", 
    command=lambda: ENTER_NUMBER(8))
#-------------------------------------
button9 = tk.Button(canvas,
    text="9", 
    command=lambda: ENTER_NUMBER(9))
#-------------------------------------
button0 = tk.Button(canvas,
    text="0", 
    command=lambda: ENTER_NUMBER(0))
#-------------------------------------
button_equal = tk.Button(canvas,text="=", bg="#88FFFF", command=enterOperationEqual)
button_equal.grid(row=5,column=2, sticky="NEWS")
button_plus = tk.Button(canvas,text="+", bg="#FF9900", command=enterOperationPlus)
button_plus.grid(row=1,column=3, sticky="NEWS")
buttonMinus = tk.Button(canvas,text="-", bg="#FF9900", command=enterOperationMinus)
buttonMinus.grid(row=4, column=3, sticky="NEWS")
buttonTimes = tk.Button(canvas,text="*", bg="#FF9900", command=enterOperationTimes)
buttonTimes.grid(row=2, column=3, sticky="NEWS")
buttonDivision = tk.Button(canvas,text="/", bg="#FF9900", command=enterOperationDivision)
buttonDivision.grid(row=3, column=3, sticky="NEWS")
buttonClear = tk.Button(canvas,text="C", bg="red", command=clearInputBox)
buttonClear.grid(row=4, column=0, sticky="NEWS")


Equation_entry.grid (row=0, column=0, columnspan=4)
button1.grid        (row=1, column=0, sticky="NEWS")
button2.grid        (row=1, column=1, sticky="NEWS")
button3.grid        (row=1, column=2, sticky="NEWS")
button4.grid        (row=2, column=0, sticky="NEWS")
button5.grid        (row=2, column=1, sticky="NEWS")
button6.grid        (row=2, column=2, sticky="NEWS")
button7.grid        (row=3, column=0, sticky="NEWS")
button8.grid        (row=3, column=1, sticky="NEWS")
button9.grid        (row=3, column=2, sticky="NEWS")
button0.grid        (row=4, column=1, sticky="NEWS")
button_equal.grid   (row=1, column=2, sticky="NEWS")
button_equal.grid   (row=4, column=2, sticky="NEWS")
button_plus.grid    (row=1, column=3, sticky="NEWS")


canvas.mainloop()

'''
NOTES I WAS GIVEN
1. Create an Entry widget to display and edit the input.
2. Create Button widgets for numbers (e.g., 1 and 2).
3. Define a function to handle number button clicks
    - Retrieve the current content of the Entry widget.
    - Clear the Entry widget.
    - Concatenate the current content with the clicked number.
    - Insert the combined text into the Entry widget.
4. Create buttons for addition (`+`) and equal (`=`)
5. Define a function to handle addition button
6. Define a function to insert the numbers 1 and 2
7. Define a function to handle equal button:
    - Get the expression
'''