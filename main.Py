from tkinter import Tk
from controller import YouTubeController

if __name__ == "__main__":
    root = Tk()
    app = YouTubeController(root)
    root.mainloop()