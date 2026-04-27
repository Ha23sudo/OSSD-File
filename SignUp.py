import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Login System")
root.geometry("400x400")
root.configure(bg="#1e1e2f")  


FONT = ("Arial", 12)
BG_COLOR = "#1e1e2f"
CARD_COLOR = "#2c2f4a"
BTN_COLOR = "#4CAF50"
TEXT_COLOR = "white"

# ---------- FRAME SWITCHING ----------
def show_frame(frame):
    frame.tkraise()

# ---------- MAIN CONTAINER ----------
container = tk.Frame(root, bg=BG_COLOR)
container.pack(fill="both", expand=True)

# ---------- LOGIN FRAME ----------
login_frame = tk.Frame(container, bg=CARD_COLOR)
signup_frame = tk.Frame(container, bg=CARD_COLOR)

for frame in (login_frame, signup_frame):
    frame.place(relwidth=1, relheight=1)

# ---------- LOGIN UI ----------
tk.Label(login_frame, text="Login", font=("Arial", 18, "bold"),
         bg=CARD_COLOR, fg=TEXT_COLOR).pack(pady=20)

login_user = tk.Entry(login_frame, font=FONT)
login_user.pack(pady=10)

login_pass = tk.Entry(login_frame, show="*", font=FONT)
login_pass.pack(pady=10)

# ---------- FILE FUNCTIONS ----------
def read_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass
    return users

def write_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

# ---------- LOGIN FUNCTION ----------
def login():
    username = login_user.get()
    password = login_pass.get()

    users = read_users()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# ---------- LOGIN BUTTON ----------
tk.Button(login_frame, text="Login", bg=BTN_COLOR, fg="white",
          font=FONT, command=login).pack(pady=15)

tk.Button(login_frame, text="Go to Signup", bg="#2196F3", fg="white",
          command=lambda: show_frame(signup_frame)).pack()

# ---------- SIGNUP UI ----------
tk.Label(signup_frame, text="Signup", font=("Arial", 18, "bold"),
         bg=CARD_COLOR, fg=TEXT_COLOR).pack(pady=20)

signup_user = tk.Entry(signup_frame, font=FONT)
signup_user.pack(pady=10)

signup_pass = tk.Entry(signup_frame, show="*", font=FONT)
signup_pass.pack(pady=10)

# ---------- SIGNUP FUNCTION ----------
def signup():
    username = signup_user.get()
    password = signup_pass.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "Fields cannot be empty")
        return

    users = read_users()

    if username in users:
        messagebox.showerror("Error", "User already exists")
    else:
        write_user(username, password)
        messagebox.showinfo("Success", "Account created!")
        show_frame(login_frame)

# ---------- SIGNUP BUTTON ----------
tk.Button(signup_frame, text="Signup", bg=BTN_COLOR, fg="white",
          font=FONT, command=signup).pack(pady=15)

tk.Button(signup_frame, text="Go to Login", bg="#2196F3", fg="white",
          command=lambda: show_frame(login_frame)).pack()





show_frame(login_frame)
root.mainloop()