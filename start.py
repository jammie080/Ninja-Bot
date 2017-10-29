import Tkinter as tk
import os
from PIL import ImageTk , Image
from app import app as un_bot


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)
        

class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)

        
        self.grip = tk.Label(self, bitmap="gray25")
        self.grip.pack(side="left", fill="y")
        

        self.grip.bind("<ButtonPress-1>", self.StartMove)
        self.grip.bind("<ButtonRelease-1>", self.StopMove)
        self.grip.bind("<B1-Motion>", self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))

class start_window(tk.Frame):
    def __init__(self, parent=None):
    	self.un_app = un_bot()

        tk.Frame.__init__(self, parent)
        tk.Frame.pack(self)
    	
    	background = r"img/rounded_button.png"
    	img = Image.open(background)

    	self.loadimage = ImageTk.PhotoImage(img)
    	self.roundedbutton = tk.Button(self, image=self.loadimage, command=self.run_app)
    	self.roundedbutton["bg"] = "white"
    	self.roundedbutton["border"] = "0"
    	self.roundedbutton.pack(side="top")

    	self.versionLabel = tk.Label(self, text="Version: 1.0.3")
    	self.versionLabel["width"] = "10"
    	self.versionLabel["height"] = "3"
    	self.versionLabel.pack(side=tk.LEFT)

    	self.latestupdateLabel = tk.Label(self, text="Latest Update: 1.0.3")
    	self.latestupdateLabel["width"] = "15"
    	self.latestupdateLabel["height"] = "3"
    	self.latestupdateLabel.pack(side=tk.RIGHT)

    def run_app(self):
    	
    	self.un_app.set_up()


if __name__ == '__main__':
	
	app=App()
	app.title("UNLIMITED NINJA BOT")
	app.geometry("300x100")
	start_window(app)
	app.mainloop()