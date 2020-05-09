from tkinter import * # Import tkinter

class ScrollText:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Dragonbound ruler: position the 0 under boomer's center")
        window.geometry('1520x40+0+520')
        window.attributes('-alpha', 0.7, "-topmost", 1)
        window.resizable(False, False)



        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1, orient='horizontal')
        scrollbar.pack(side = BOTTOM, fill = X)
        text = Text(frame1, width = 188, height = 10, wrap='none',
                    xscrollcommand = scrollbar.set)
        text.insert('end',
        	"12-------------11-------------10-------------9-------------8-------------7------------6-------------5------------4-------------3------------2-------------1-------------0-------------1-------------2------------3-------------4------------5-------------6------------7-------------8-------------9-------------10-------------11-------------12"
        	)
        text.configure(state='disabled')
        text.pack()
        scrollbar.config(command = text.xview)

        window.mainloop() # Create an event loop

ScrollText() # Create GUI