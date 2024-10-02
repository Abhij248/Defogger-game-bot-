import tkinter as tk

app = tk.Tk()
app.title("Test GUI")
app.geometry("400x300")

label = tk.Label(app, text="Hello, Tkinter!")
label.pack(pady=20)

app.mainloop()
