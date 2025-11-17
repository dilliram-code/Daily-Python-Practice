import tkinter as tk
from tkinter import messagebox, filedialog  

root = tk.Tk()
root.geometry("400x300")
root.title("Tkinter part 4")

def open_file():
  file = filedialog.askopenfilename()
  messagebox.showinfo("Selected file", file)
  

root.mainloop()