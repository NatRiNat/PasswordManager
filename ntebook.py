from tkinter import ttk
import tkinter as tk
from tkinter import PhotoImage

FONT = ('Arial', 9, 'normal')


class Window:
    def __init__(self, master):
        self.master = master

        # Create a NOTEBOOK
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both')

        # Create Notebook FRAMES
        self.tab1 = ttk.Frame(self.notebook, relief='sunken', padding=5, borderwidth=5)
        self.tab2 = ttk.Frame(self.notebook, relief='groove', padding=20, borderwidth=5)
        self.tab3 = ttk.Frame(self.notebook, relief='raised', padding=5, borderwidth=3)

        # ADD frames to notebook
        self.notebook.add(self.tab1, text='Generate', padding=10)
        self.notebook.add(self.tab2, text='Options', padding=10)
        self.notebook.add(self.tab3, text='Data')

        # Add IMAGE to Generate tab (tab1)
        self.img = PhotoImage(file='logo.png')
        self.tab1_label = tk.Label(self.tab1, image=self.img, relief='raised', background='light sea green',
                                   borderwidth=3)
        self.tab1_label.grid(row=0, column=1, sticky='ew')

        # WEBSITE Label and Entry (tab1)
        self.website_label = ttk.Label(self.tab1, text='Website:  ', width=17, anchor='e')
        self.website_label.grid(row=1, column=0)

        self.entry_website = ttk.Entry(self.tab1, width=35)
        self.entry_website.grid(row=1, column=1, columnspan=2, sticky='ew')
        self.entry_website.focus()  # places the cursor inside of this entry 'box' at the starting position - left

        # EMAIL Label and Entry (tab1)
        self.username_label = ttk.Label(self.tab1, text='Email/Username:  ', width=17, anchor='e')
        self.username_label.grid(row=2, column=0)

        self.entry_username = ttk.Entry(self.tab1, width=35)
        self.entry_username.grid(row=2, column=1, columnspan=2, sticky='ew')
        self.entry_username.insert(0, '@gmail.com')

        # PASSWORD Label and Entry (tab1)
        self.password_label = ttk.Label(self.tab1, text='Password:  ', width=17, anchor='e')
        self.password_label.grid(row=3, column=0)

        self.entry_password = ttk.Entry(self.tab1, width=21)
        self.entry_password.grid(row=3, column=1, sticky='ew')

        # SPACERS on all tabs (until I find better way to put space between buttons and labels - in some areas 'pady'
        # didn't work, plus it does look nicer with spacer instead of padding - for some places on y)
        self.spacer1 = ttk.Label(self.tab1, text="")
        self.spacer1.grid(row=5, column=1)

        self.spacer2 = ttk.Label(self.tab1, text="")
        self.spacer2.grid(row=7, column=1)

        self.spacer4 = ttk.Label(self.tab2, text='')
        self.spacer4.grid(row=1, column=0)

        self.spacer6 = ttk.Label(self.tab3, text='')
        self.spacer6.grid(row=0, column=1)

        # SLIDER - label and scale on Generate tab (tab1)
        self.slider_label = ttk.Label(self.tab1, text='Password Length')
        self.slider_label.grid(row=7, column=0)

        self.slider = tk.Scale(self.tab1, from_=6, to=20, orient='horizontal', background='#d9d9d9',
                               activebackground='light sea green', relief='raised', troughcolor='white')
        self.slider.grid(row=8, column=0, columnspan=3, sticky='ew')
        self.slider.set(15)

        #  SPIN labels and password choice label on Option tab (tab2)
        self.letters = tk.Label(self.tab2, text='Letters:', background='#d9d9d9', font=FONT, anchor='w')
        self.letters.grid(row=2, column=0, )

        self.upper = tk.Label(self.tab2, text='Upper', background='#d9d9d9', font=FONT)
        self.upper.grid(row=2, column=1)

        self.lower = tk.Label(self.tab2, text='Lower', background='#d9d9d9', font=FONT, padx=15)
        self.lower.grid(row=2, column=3)

        self.numbers = tk.Label(self.tab2, text='Numbers:', background='#d9d9d9', font=FONT, pady=10)
        self.numbers.grid(row=4, column=0)

        self.char = tk.Label(self.tab2, text='S.Charac:', background='#d9d9d9', font=FONT, pady=10)
        self.char.grid(row=5, column=0)

        self.char_show = tk.Label(self.tab2, text='"£$%^&*', bg='#d9d9d9', font=FONT)
        self.char_show.grid(row=5, column=2)

        self.pass_choice_length = tk.Label(self.tab2, text='Password Length:', background='#d9d9d9', pady=20)
        self.pass_choice_length.grid(row=0, column=2)

        # TEXTBOX on Data tab (tab3)
        self.text = tk.Text(self.tab3, relief='sunken', height=23, width=55)
        self.text.grid(row=2, column=0, columnspan=2)

        # BOTTOM TEXT LABEL tab1, tab2, tab3 - had only one text on root window, but it gets messed up when changing
        # styles or adding/removing widgets so removed it to avoid unnecessary frustration until I finish,
        # and created these 3. Will work on it at later time, probably changing root geometry to something else or
        # TNotebook expand/fill options:
        bottom_text = tk.Label(self.tab1, text='\n\n~~~~!May your account be ever secured and protected!~~~~~',
                               background='#d9d9d9', font=FONT)
        bottom_text.grid(row=9, column=0, columnspan=3, sticky='ew')

        bottom_text = tk.Label(self.tab3, text='\n\n~~~~!May your account be ever secured and protected!~~~~~',
                               background='#d9d9d9', font=FONT)
        bottom_text.grid(row=3, column=0, columnspan=2, sticky='ew')

        bottom_text = tk.Label(self.tab2, text='\n\n~~~~!May your account be ever secured and protected!~~~~~',
                               background='#d9d9d9', font=FONT)
        bottom_text.place(x=20, y=350)
