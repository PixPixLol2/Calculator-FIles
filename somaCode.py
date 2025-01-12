import tkinter as tk

 

root = tk.Tk()

root.geometry("300x300")

root.config(bg="light blue")

 

root.rowconfigure(0, weight=1)

root.rowconfigure(1, weight=1)

root.rowconfigure(2, weight=1)

root.rowconfigure(3, weight=1)

root.rowconfigure(4, weight=1)

root.rowconfigure(5, weight=1)

 

root.columnconfigure(0, weight=1)

root.columnconfigure(1, weight=1)

root.columnconfigure(2, weight=1)

root.columnconfigure(3, weight=1)

 

inputField = tk.Entry(root, justify="center")

inputField.grid(row=0, column=0, sticky="NESW", columnspan=4)

 

root.title("Calculator")

 

lastKey = ""

memory = None

 

def clear():
    inputField.delete(0, len(inputField.get()))

root.title("Calculator")

 

def evaluateResult():
    global memory
    
    tempStorageCalculate = inputField.get()

 

try:
    result = eval(tempStorageCalculate)
    
    inputField.insert(0, str(result))

 

except Exception as e:
    inputField.insert(0, str(e))

 

def insertInput(input):
    global lastKey

    if inputField.get() != "":

        if input in ["+", "*", "/", "-"]:

            if lastKey in ["+", "-", "*", "/"]:

                inputField.delete(len(inputField.get()) - 1)

    inputField.insert(tk.END, input)

    lastKey = input

     

    pass

 

def equal_operation():

    read_data = inputField.get()

    inputField.delete(0,tk.END)

    result = eval(read_data)

    inputField.insert(tk.END,result)

 

def deleteLast():

    current_text = inputField.get()

    inputField.delete(0, len(current_text))

 

def percentage():

    current_text = inputField.get()

    try:

        result = eval(current_text) / 100

        clear()

        inputField.insert(0, str(result))

    except Exception as e:

        inputField.insert(0, str(e))

 

def memoryRecall():

    global memory

    clear()

    if memory is not None:

        inputField.insert(0, str(memory))

    else:

        inputField.insert(0, "0")

 

button1 = tk.Button(root, text="1", bg="light blue", command=lambda: insertInput("1"))

 

button2 = tk.Button(root, text="2", bg="light blue", command=lambda: insertInput("2"))

 

button3 = tk.Button(root, text="3", bg="light blue", command=lambda: insertInput("3"))

 

buttonDivision = tk.Button(root, text="÷", bg="light blue", command=lambda: insertInput("/"))

 

button4 = tk.Button(root, text="4", bg="light blue", command=lambda: insertInput("4"))

 

button5 = tk.Button(root, text="5", bg="light blue", command=lambda: insertInput("5"))

 

button6 = tk.Button(root, text="6", bg="light blue", command=lambda: insertInput("6"))

 

buttonMultiplication = tk.Button(root, text="x", bg="light blue", command=lambda: insertInput("*"))

 

button7 = tk.Button(root, text="7", bg="light blue", command=lambda: insertInput("7"))

 

button8 = tk.Button(root, text="8", bg="light blue", command=lambda: insertInput("8"))

 

button9 = tk.Button(root, text="9", bg="light blue", command=lambda: insertInput("9"))

 

buttonSubtraction = tk.Button(root, text="-", bg="light blue", command=lambda: insertInput("-"))

 

buttonClear = tk.Button(root, text="C", bg="red", command=lambda: insertInput("C"))

 

button0 = tk.Button(root, text="0", bg="light blue", command=lambda: insertInput("0"))

 

buttonEquals = tk.Button(root, text="=", bg="light green", command=equal_operation)

 

buttonAddition = tk.Button(root, text="+", bg="light blue", command=lambda: insertInput("+"))

 

buttonDelete = tk.Button(root, text="DEL", bg="orange", command=lambda: deleteLast())

 

buttonPercentage = tk.Button(root, text="%", bg="orange", command=lambda: percentage())

 

buttonDecimal = tk.Button(root, text=".", bg="orange", command=lambda: insertInput("."))

 

buttonMemory = tk.Button(root, text="M", bg="orange", command=lambda: inputField.insert("end", str(memory)))

  #positioning 

button1.grid(row=1, column=0, sticky="NESW")

button2.grid(row=1, column=1, sticky="NESW")

button3.grid(row=1, column=2, sticky="NESW")

buttonDivision.grid(row=1, column=3, sticky="NESW")

button4.grid(row=2, column=0, sticky="NESW")

button5.grid(row=2, column=1, sticky="NESW")

button6.grid(row=2, column=2, sticky="NESW")

buttonMultiplication.grid(row=2, column=3, sticky="NESW")

button7.grid(row=3, column=0, sticky="NESW")

button8.grid(row=3, column=1, sticky="NESW")

button9.grid(row=3, column=2, sticky="NESW")

buttonSubtraction.grid(row=3, column=3, sticky="NESW")

buttonClear.grid(row=4, column=0, sticky="NESW")

button0.grid(row=4, column=1, sticky="NESW")

buttonEquals.grid(row=4, column=2, sticky="NESW")

buttonAddition.grid(row=4, column=3, sticky="NESW")

 

buttonDelete.grid(row=5, column=0, sticky="NESW")

buttonPercentage.grid(row=5, column=1, sticky="NESW")

buttonDecimal.grid(row=5, column=2, sticky="NESW")

 

button8.config(command=lambda: insertInput("8"))

buttonEquals.config(command=lambda: evaluateResult()) 

root.mainloop()