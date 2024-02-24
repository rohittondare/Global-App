import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("500x500")
root.title("Global Infrastructure")

logo = tk.PhotoImage(file="logo.png")
#tk.Label (root, image=logo,bg = "black") .pack(side="top") 

canvas = tk.Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = tk.PhotoImage(file="logo.png")   
canvas.create_image(20,20, image=img)

app = Application(master=root)
app.mainloop()