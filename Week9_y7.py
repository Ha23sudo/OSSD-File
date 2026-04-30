
import tkinter as  tk

def add():
    val1=float(n1.get())
    val2=float(n2.get())
    res=val1+val2
    print(res)
    result.config(text="Result: "+str(res))

root=tk.Tk()
root.title("Calculator")
root.geometry("300x250")
root.resizable(False,False)
root.config(bg="lightblue")
root.iconphoto(False, tk.PhotoImage(file="im.png"))

tk.Label(root, text="Enter Value 1").pack()
n1=tk.Entry(root)
n1.pack()
tk.Label(root, text="Enter Value 2").pack()
n2=tk.Entry(root)
n2.pack()
tk.Button(root, text="Add",command=add).pack()
tk.Button(root, text="-").pack()

result=tk.Label(root, text="Result:")
result.pack()

root.mainloop()




