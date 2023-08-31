import tkinter as tk

def pluss_button():
    num1 = float(number1.get())
    num2 = float(number2.get())

    results_option.configure(text=str(num1+num2))
    
def minus_button():
    num1 = float(number1.get())
    num2 = float(number2.get())
    results_option.configure(text=str(num1-num2))

def impact_button():
    num1 = float(number1.get())
    num2 = float(number2.get())
    results_option.configure(text=str(num1*num2))

def divide_button():
    num1 = float(number1.get())
    num2 = float(number2.get())
    results_option.configure(text=str(num1/num2))


window = tk.Tk()

window.title("Calculator")
window.geometry("320x300")


results_option = tk.Label(window,text="Result",font="Courier 16 bold",width=30,justify="center")
results_option.place(x=-50,y=20)


number1=tk.Entry(window,font="Courier 14 bold",width=15,justify="right")
number1.place(x=70,y=50)
number2=tk.Entry(window,font="Courier 14 bold",width=15,justify="right")
number2.place(x=70,y=80)


button_plus = tk.Button(window,text="+",font="Courier 14 bold",width=10,command=pluss_button)
button_plus.place(x=90,y=110)

button_minus = tk.Button(window,text="-",font="Courier 14 bold",width=10,command=minus_button)
button_minus.place(x=90,y=150)

button_impact = tk.Button(window,text="*",font="Courier 14 bold",width=10,command=impact_button)
button_impact.place(x=90,y=190)

button_divide = tk.Button(window,text="/",font="Courier 14 bold",width=10,command=divide_button)
button_divide.place(x=90,y=230)

window.mainloop()



