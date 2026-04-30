import tkinter as tk
import tkinter.messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        result_label.config(text="Login successful!")
        
    else:
        result_label.config(text="Login failed!")
        tk.messagebox.showerror("Error", "Invalid username or password")






root = tk.Tk()
root.title("Login")
root.geometry("300x200")
root.resizable(0, 0)
root.configure(bg="#95adea")
root.iconphoto(False, tk.PhotoImage(file="im.png"))

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)    

result_label=tk.Label(root, text=" ")
result_label.pack()



root.mainloop()