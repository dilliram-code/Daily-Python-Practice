from tkinter import *

class NLPApp:
  def __init__(self):
    
    # login page load
    self.root = Tk()
    self.root.title("NLP App")
    # self.root.iconbitmap("resources\image.ico")
    self.root.geometry("300x600")
    self.root.configure(bg='#34495E')
    
    self.login_gui()
    self.root.mainloop()
    
  def login_gui(self):
    heading = Label(self.root, text='NLP App', bg=  '#34495E', fg='white')
    heading.pack(pady=(30,30))
    heading.configure(font = ('verdana', 24, 'bold'))
nlp = NLPApp()