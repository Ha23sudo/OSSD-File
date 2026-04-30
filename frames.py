import tkinter as tk

root = tk.Tk()
root.title("Project Layout")
root.geometry("500x400")

#  Header
header = tk.Frame(root, bg="lightblue", height=50)
header.pack(fill="x")

tk.Label(header, text="My App", bg="lightblue", font=("Arial", 16)).pack(pady=10)

#  Main area (contains sidebar + content)
main = tk.Frame(root)
main.pack(fill="both", expand=True)

#  Sidebar
sidebar = tk.Frame(main, bg="lightgray", width=120)
sidebar.pack(side="left", fill="y")

tk.Button(sidebar, text="Home").pack(pady=10, padx=10)
tk.Button(sidebar, text="Settings").pack(pady=10, padx=10)

#  Content area
content = tk.Frame(main, bg="white")
content.pack(side="left", fill="both", expand=True)

tk.Label(content, text="Welcome!", bg="white", font=("Arial", 14)).pack(pady=20)

#  Footer
footer = tk.Frame(root, bg="lightblue", height=30)
footer.pack(fill="x")

tk.Label(footer, text="© 2026", bg="lightblue").pack()

root.mainloop()