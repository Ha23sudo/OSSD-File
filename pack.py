import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

tk.Label(root, text="Header", bg="lightblue").pack(fill="x")

tk.Button(root, text="Left").pack(side="left", fill="y")
tk.Button(root, text="Right").pack(side="right", fill="y")

tk.Label(root, text="Center Area", bg="yellow").pack(expand=True, fill="both")

root.mainloop()