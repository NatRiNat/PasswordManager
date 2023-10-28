import tkinter as tk


# Found this code on StackO. Included in program even though I do not understand it completely. Need to work on it.
# Decided to take out delete and cut options that were in the code, just used copy and paste.
class RightClicker:
    def __init__(self, e):
        commands = ["Copy", "Paste"]
        menu = tk.Menu(None, tearoff=0, takefocus=0)

        for txt in commands:
            menu.add_command(label=txt, command=lambda e=e, txt=txt: self.click_command(e, txt))

        menu.tk_popup(e.x_root + 40, e.y_root + 10, entry="0")

    def click_command(self, e, cmd):
        e.widget.event_generate(f'<<{cmd}>>')
