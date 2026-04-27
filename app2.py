import tkinter as t

root = t.Tk()
root.title("Login System")
root.geometry("600x200")
root.configure(bg="lightblue")
root.resizable(False, False)

t.Label(root, text="Username:", bg="lightblue").pack(pady=10)
username_entry = t.Entry(root, width=30)    
username_entry.pack(pady=5)
t.Label(root, text="Password:", bg="lightblue").pack(pady=10)
password_entry = t.Entry(root, width=30, show="*")
password_entry.pack(pady=5)









root.mainloop()



