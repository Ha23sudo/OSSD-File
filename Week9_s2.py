import tkinter as tk

def add():
   
    n1=float(v1.get())
    n2=float(v2.get())
    result=n1+n2
    res.config(text=f"Result: {result}")


root=tk.Tk()
root.title("basic calculator")
root.geometry("400x400")
root.resizable(0,0)
root.configure(bg="#7294e9")
root.iconphoto(False, tk.PhotoImage(file="im.png"))

tk.Label(root, text="Enter first number").pack()
v1=tk.Entry(root)
v1.pack()
tk.Label(root, text="Enter second number").pack()
v2=tk.Entry(root)
v2.pack()

tk.Button(root, text="Add",command=add).pack()
tk.Button(root, text="Subtract").pack()

res=tk.Label(root, text="Result ----")
res.pack()


root.mainloop()



