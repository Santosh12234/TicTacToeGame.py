from tkinter import *
from tkinter import messagebox

matrix = [["1","2","3"],["4","5","6"],["7","8","9"]]

root = Tk()
root.geometry("383x510")
root.title("Tic-Tac-Toe")
root.resizable(False,False)
m = "O"
times = 1

def check(n):
    global m
    global times
    if n == 1:
        if m == "O":
            matrix[0][0] = "X"
            m = "X"
        else:
            matrix[0][0] = "O"
            m = "O"
        button1.config(text=matrix[0][0], state="disabled")
        if (matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2]) or (matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0]) or (matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]):
            label1.config(text=str(matrix[0][0])+" Win's")
            if str(matrix[0][0])=="X":
                messagebox.showinfo("Info", "X Win's")
            else:
                messagebox.showinfo("Info", "O Win's")
            button2.config(state="disabled")
            button3.config(state="disabled")
            button4.config(state="disabled")
            button5.config(state="disabled")
            button6.config(state="disabled")
            button7.config(state="disabled")
            button8.config(state="disabled")
            button9.config(state="disabled")
        elif times == 9:
            label1.config(text="Draw")
    if n == 2:
        if m == "O":
            matrix[0][1] = "X"
            m = "X"
        else:
            matrix[0][1] = "O"
            m = "O"
        button2.config(text=matrix[0][1], state="disabled")
        if (matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2]) or (matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1]):
            label1.config(text=str(matrix[0][1])+" Win's")
            if str(matrix[0][1])=="X":
                messagebox.showinfo("Info", "X Win's")
            else:
                messagebox.showinfo("Info", "O Win's")
            button1.config(state="disabled")
            button3.config(state="disabled")
            button4.config(state="disabled")
            button5.config(state="disabled")
            button6.config(state="disabled")
            button7.config(state="disabled")
            button8.config(state="disabled")
            button9.config(state="disabled")
        elif times == 9:
            label1.config(text="Draw")
    if n == 3:
        if m == "O":
            matrix[0][2] = "X"
            m = "X"
        else:
            matrix[0][2] = "O"
            m = "O"
        button3.config(text=matrix[0][2], state="disabled")
        if (matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2]) or (matrix[0][2] == matrix[1][2] and matrix[0][2]== matrix[2][2]) or (matrix[0][2] == matrix[1][1] and matrix[0][2] == matrix[2][0]):
            label1.config(text=str(matrix[0][2])+" Win's")
            if str(matrix[0][2])=="X":
                messagebox.showinfo("Info", "X Win's")
            else:
                messagebox.showinfo("Info", "O Win's")
            button1.config(state="disabled")
            button2.config(state="disabled")
            button4.config(state="disabled")
            button5.config(state="disabled")
            button6.config(state="disabled")
            button7.config(state="disabled")
            button8.config(state="disabled")
            button9.config(state="disabled")
        elif times == 9:
            label1.config(text="Draw")
    if n == 4:
        if m == "O":
            matrix[1][0] = "X"
            m = "X"
        else:
            matrix[1][0] = "O"
            m = "O"
        button4.config(text=matrix[1][0], state="disabled")
        if (matrix[0][0] == matrix[1][0] and matrix[0][0]== matrix[2][0]) or (matrix[1][0] == matrix[1][1] and matrix[1][0] == matrix[1][2]):
            label1.config(text=str(matrix[1][0])+" Win's")
            if str(matrix[1][0])=="X":
                messagebox.showinfo("Info", "X Win's")
            else:
                messagebox.showinfo("Info", "O Win's")
            button1.config(state="disabled")
            button2.config(state="disabled")
            button3.config(state="disabled")
            button5.config(state="disabled")
            button6.config(state="disabled")
            button7.config(state="disabled")
            button8.config(state="disabled")
            button9.config(state="disabled")
        elif times == 9:
            label1.config(text="Draw")
    if n == 5:
        if m == "O":
            matrix[1][1] = "X"
            m = "X"
        else:
            matrix[1][1] = "O"
            m = "O"
        button5.config(text=matrix[1][1], state="disabled")
        if (matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]) or (matrix[2][0] == matrix[1][1] and matrix[2][0]== matrix[0][2]) or (matrix[1][0] == matrix[1][1] and matrix[1][0]== matrix[1][2]) or (matrix[0][1] == matrix[1][1] and matrix[0][1]== matrix[2][1]):
            label1.config(text=str(matrix[1][1])+" Win's")
            if str(matrix[1][1])=="X":
                messagebox.showinfo("Info", "X Win's")
            else:
                messagebox.showinfo("Info", "O Win's")
            button1.config(state="disabled")
            button2.config(state="disabled")
            button3.config(state="disabled")
            button4.config(state="disabled")
            button6.config(state="disabled")
            button7.config(state="disabled")
            button8.config(state="disabled")
            button9.config(state="disabled")
        elif times == 9:
            label1.config(text="Draw")
    if n == 6:
        if m == "O":
            matrix[1][2] = "X"
            m = "X"
        else:
            matrix[1][2] = "O"
            m = "O"
        button6.config(text=matrix[1][2], state="disabled")
        if (matrix[1][0] == matrix[1][1] and matrix[1][0] == matrix[1][2]) or (matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2]):
            label1.config(text=str(matrix[1][2])+" Win's")
            if str(matrix[1][2])=="X":
                messagebox.showinfo("Info", "X Win's")
            else:
                messagebox.showinfo("Info", "O Win's")
            button1.config(state="disabled")
            button2.config(state="disabled")
            button3.config(state="disabled")
            button4.config(state="disabled")
            button5.config(state="disabled")
            button7.config(state="disabled")
            button8.config(state="disabled")
            button9.config(state="disabled")
        elif times == 9:
            label1.config(text="Draw")
    if n == 7:
        if m == "O":
            matrix[2][0] = "X"
            m = "X"
        else:
            matrix[2][0] = "O"
            m = "O"
        button7.config(text=matrix[2][0], state="disabled")
        if (matrix[0][0] == matrix[1][0]  and matrix[0][0] == matrix[2][0]) or (matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2]) or (matrix[2][0] == matrix[1][1] and matrix[2][0] == matrix[0][2]):
            label1.config(text=str(matrix[2][0])+" Win's")
            if str(matrix[2][0])=="X":
                messagebox.showinfo("Info", "X Win's")
            else:
                messagebox.showinfo("Info", "O Win's")
            button1.config(state="disabled")
            button2.config(state="disabled")
            button3.config(state="disabled")
            button4.config(state="disabled")
            button5.config(state="disabled")
            button6.config(state="disabled")
            button8.config(state="disabled")
            button9.config(state="disabled")
        elif times == 9:
            label1.config(text="Draw")
    if n == 8:
        if m == "O":
            matrix[2][1] = "X"
            m = "X"
        else:
            matrix[2][1] = "O"
            m = "O"
        button8.config(text=matrix[2][1], state="disabled")
        if (matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2]) or (matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1]):
            label1.config(text=str(matrix[2][1])+" Win's")
            if str(matrix[2][1])=="X":
                messagebox.showinfo("Info", "X Win's")
            else:
                messagebox.showinfo("Info", "O Win's")
            button1.config(state="disabled")
            button2.config(state="disabled")
            button3.config(state="disabled")
            button4.config(state="disabled")
            button5.config(state="disabled")
            button6.config(state="disabled")
            button7.config(state="disabled")
            button9.config(state="disabled")
        elif times == 9:
            label1.config(text="Draw")
    if n == 9:
        if m == "O":
            matrix[2][2] = "X"
            m = "X"
        else:
            matrix[2][2] = "O"
            m = "O"
        button9.config(text=matrix[2][2], state="disabled")
        if (matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]) or (matrix[0][2] == matrix[1][2] and matrix[0][2]== matrix[2][2]) or (matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2]):
            label1.config(text=str(matrix[2][2]) + " Win's")
            if str(matrix[2][2])=="X":
                messagebox.showinfo("Info", "X Win's")
            else:
                messagebox.showinfo("Info", "O Win's")
            button1.config(state="disabled")
            button2.config(state="disabled")
            button3.config(state="disabled")
            button4.config(state="disabled")
            button5.config(state="disabled")
            button6.config(state="disabled")
            button7.config(state="disabled")
            button8.config(state="disabled")
        elif times == 9:
            label1.config(text="Draw")
    times = times+1
button1 = Button(root,bg="blue",fg="black",width=7,height=3,font=("Candra",20),disabledforeground="black",command=lambda:check(1))
button1.place(x=5,y=87)
button2 = Button(root,bg="blue",fg="black",width=7,height=3,font=("Candra",20),disabledforeground="black",command=lambda:check(2))
button2.place(x=130,y=87)
button3 = Button(root,bg="blue",fg="black",width=7,height=3,font=("Candra",20),disabledforeground="black",command=lambda:check(3))
button3.place(x=255,y=87)
button4 = Button(root,bg="blue",fg="black",width=7,height=3,font=("Candra",20),disabledforeground="black",command=lambda:check(4))
button4.place(x=5,y=210)
button5 = Button(root,bg="blue",fg="black",width=7,height=3,font=("Candra",20),disabledforeground="black",command=lambda:check(5))
button5.place(x=130,y=210)
button6 = Button(root,bg="blue",fg="black",width=7,height=3,font=("Candra",20),disabledforeground="black",command=lambda:check(6))
button6.place(x=255,y=210)
button7 = Button(root,bg="blue",fg="black",width=7,height=3,font=("Candra",20),disabledforeground="black",command=lambda:check(7))
button7.place(x=5,y=333)
button8 = Button(root,bg="blue",fg="black",width=7,height=3,font=("Candra",20),disabledforeground="black",command=lambda:check(8))
button8.place(x=130,y=333)
button9 = Button(root,bg="blue",fg="black",width=7,height=3,font=("Candra",20),disabledforeground="black",command=lambda:check(9))
button9.place(x=255,y=333)
buttonexit = Button(root,bg="red",fg="black",width=27,height=1,font=("Candra",18),disabledforeground="black",text ="Exit",command=lambda:exit(0))
buttonexit.place(x=0,y=456)



label1 = Label(root,bg="blue",fg="black",font=("Candra",25),height=2,width=20,text="Tic-Tac-Toe")
label1.place(x=0,y=0)

root.mainloop()
