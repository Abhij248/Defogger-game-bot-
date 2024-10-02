import tkinter as tk
from tkinter import messagebox
from fog_bot import defogging, stop_event
import threading

bot_thread = None

def run_bot():
    global bot_thread
    if bot_thread and bot_thread.is_alive():
        messagebox.showinfo("Info", "Bot is already running")
        return

    stop_event.clear()
    bot_thread = threading.Thread(target=defogging)
    bot_thread.start()

def stop_bot():
    stop_event.set()
    if bot_thread:
        bot_thread.join()  # Wait for the bot thread to finish
    app.quit()  # Gracefully close the Tkinter window

print("Creating Tkinter app")
app = tk.Tk()
app.title("Bot GUI")
app.geometry("400x300")

print("Adding buttons")
run_button = tk.Button(app, text="Run Bot", command=run_bot)
run_button.pack(pady=20)

stop_button = tk.Button(app, text="Stop Bot", command=stop_bot)
stop_button.pack(pady=20)

print("Starting Tkinter main loop")
app.mainloop()
