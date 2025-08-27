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
    
    label1= Label(self.root, text="Enter email")
    label1.pack(pady=(10,10))
    
    self.email_input = Entry(self.root, width=40)
    self.email_input.pack(pady=(5,10), ipady=4)
    
    label2 = Label(self.root, text="Enter password")
    label2.pack(pady=(10, 10))

    self.password_input = Entry(self.root, width=40)
    self.password_input.pack(pady=(5, 10), ipady=4)
    
    login_btn = Button(self.root, text="Login", width=30, height=2)
    login_btn.pack(pady=(10, 10))
    
    label3 = Label(self.root, text="Not a member?")
    label3.pack(pady=(20, 10))
    
    redirect_btn = Label(self.root, text="Register Now")
    redirect_btn.pack(pady=(10,10))
    
nlp = NLPApp()