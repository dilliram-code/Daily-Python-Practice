from tkinter import *

class NLPApp:
  def __init__(self):
    
    # login page load
    self.root = Tk()
    self.root.title("NLP App")
    # self.root.iconbitmap("resources\image.ico")
    self.root.geometry("300x600")
    self.root.configure(bg='#34495E')
    self.root.mainloop()
  
nlp = NLPApp()