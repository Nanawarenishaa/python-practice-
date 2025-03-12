import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter Window")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Close", command=root.destroy)
button.pack()

root.mainloop()
