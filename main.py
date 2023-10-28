from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
from ntebook import Window
from string import ascii_letters, punctuation, digits
import pyperclip
from rightclicker import RightClicker

# root window
root = Tk()
# notebook, its frames and labels (all that is without command) are on ntebook.py under class Window
window = Window(root)
root.geometry('470x500-500+50')
root.title('PASSWORD GENERATOR')
FONT = ('Arial', 9, 'normal')

# TODO: Maybe make Themes, put them in Option tab for user to choose (e.g. light and dark with menu options)
style = ttk.Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background='light sea green', focuscolor='#d9d9d9')
style.map("TNotebook", background=[("selected", "#d9d9d9")])


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    if checkbox_state.get() == 0:
        no_choice_pass = list(ascii_letters + digits + punctuation)
        random.shuffle(no_choice_pass)

        password_list = [random.choice(no_choice_pass) for _ in range(int(window.slider.get()))]

        password = "".join(password_list)
        window.entry_password.insert(0, password)
        pyperclip.copy(password)
    else:
        upper = [chr(random.randint(65, 90)) for _ in range(int(spin_upper.get()))]
        lower = [chr(random.randint(65, 90)).lower() for _ in range(int(spin_lower.get()))]
        pass_num = [random.choice(digits) for _ in range(int(spin2.get()))]
        pass_char = [random.choice(punctuation) for _ in range(int(spin3.get()))]
        passw = (upper + lower + pass_num + pass_char)
        random.shuffle(passw)

        fin_pass = "".join(passw)
        window.entry_password.insert(0, fin_pass)
        pyperclip.copy(fin_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file():
    web_info = window.entry_website.get()
    email_info = window.entry_username.get()
    pass_info = window.entry_password.get()

    # this is to highlight if there is missing input from user + pop-up error box
    if len(web_info) == 0:
        window.website_label.config(foreground='red')
    else:
        window.website_label.config(foreground="black")
    if len(email_info) == 0:
        window.username_label.config(foreground='red')
    else:
        window.username_label.config(foreground="black")
    if len(pass_info) == 0:
        window.password_label.config(foreground='red')
    else:
        window.password_label.config(foreground="black")

    if len(web_info) == 0 or len(pass_info) == 0 or len(email_info) == 0:
        messagebox.showerror(message="Please enter all required fields")
    else:
        answer = messagebox.askokcancel(title=web_info, message=f"Email: {email_info}\n\n"
                                                                f"Password: {pass_info}\n\nReady to "
                                                                f"save?")
        if answer:
            with open('data.txt', "a") as fp:
                fp.write(f"{web_info} | {email_info} | {pass_info}\n")
            window.entry_website.delete(0, END)
            window.entry_password.delete(0, END)
            messagebox.showinfo(message="Information saved to Data")


# ------------------------------GENERATOR TAB (tab1): --------------------------------#

# RESET button
def reset():
    window.entry_password.delete(0, END)


# BUTTONS with commands on tab1
button_generate = Button(window.tab1, text='Generate Password', command=gen_pass)
button_generate.grid(row=3, column=2, sticky='ew')

button_add = Button(window.tab1, text='Add', command=write_to_file)
button_add.grid(row=4, column=1, columnspan=2, sticky='ew')

button_reset = Button(window.tab1, text='Reset Password', command=reset)
button_reset.grid(row=6, column=1, sticky='e')


# ------------------------------ OPTION TAB (tab2)-------------------------------------#

# If user chooses to make choices on Option tab - disable slider (THICKBOX with command on tab2)
def check_button_used():
    if checkbox_state.get():
        window.slider.config(state='disabled')
    else:
        window.slider.config(state='normal')


checkbox_state = IntVar()
checkbutton = Checkbutton(window.tab2, text='Select for choices', variable=checkbox_state, bg='#d9d9d9',
                          activebackground='light sea green', command=check_button_used, font=FONT, pady=10)
checkbutton.grid(row=0, column=0)


# This is to show password length on Option tab, when user making own choices
def pas_length():
    a = str(int(spin_upper.get()) + int(spin3.get()) + int(spin2.get()) + int(spin_lower.get()))
    choice_length.delete(1.0, END)
    choice_length.insert(1.0, a)


choice_length = Text(window.tab2, background='#d9d9d9', width=3, height=1)
choice_length.grid(row=0, column=3)

# SPINs with commands on Option tab
spin_upper = Spinbox(window.tab2, from_=0, to=20, width=4, command=pas_length)
spin_upper.grid(row=2, column=2)

spin_lower = Spinbox(window.tab2, from_=0, to=20, width=4, command=pas_length)
spin_lower.grid(row=2, column=4)

spin2 = Spinbox(window.tab2, from_=0, to=10, width=4, command=pas_length)
spin2.grid(row=4, column=1)

spin3 = Spinbox(window.tab2, from_=0, to=10, width=4, command=pas_length)
spin3.grid(row=5, column=1)


# this is for RADIO buttons on Option tab, to change color of img, tab and some buttons
def radio_used():
    if radio_state.get() == 1:
        window.tab1_label.config(background='light sea green')
        checkbutton.config(activebackground='light sea green')
        window.slider.config(activebackground='light sea green')
        button_update.config(background='light sea green')
        button_save.config(bg='light sea green')
        style.configure('TNotebook.Tab', background='light sea green', focuscolor='#d9d9d9')

    else:
        window.tab1_label.config(background='dodger blue')
        checkbutton.config(activebackground='dodger blue')
        window.slider.config(activebackground='dodger blue')
        button_update.config(background='dodger blue')
        button_save.config(bg='dodger blue')
        style.configure('TNotebook.Tab', background='dodger blue', focuscolor='#d9d9d9')


radio_state = IntVar(value=1)
radio_b1 = Radiobutton(window.tab2, text="Green", value=1, variable=radio_state,
                       command=radio_used, bg='#d9d9d9', pady=50)
radio_b2 = Radiobutton(window.tab2, text="Blue", value=2, variable=radio_state, command=radio_used, bg='#d9d9d9')
radio_b1.grid(row=7, column=1)
radio_b2.grid(row=7, column=2)


# ---------------------------------------- DATA TAB (tab3)------------------------------------#

# Textbox for Data tab - to hide it - not used - will explore this idea more later
# window.notebook.tab(window.tab3, state='hidden')  # normal, disabled, and hidden

# This is for Data tab, to load/update txt file, save if changes made by user (need to be careful not to overwrite other
# passwords (well, like in any other editing file). Here,  set up is on 'r+'. Append 'a' didn't work properly)
def text_update():
    window.text.delete(1.0, END)
    with open('data.txt', 'r') as fp:
        t = fp.read()
        window.text.insert(1.0, t)


def save():
    with open('data.txt', 'r+') as fp:
        fp.write(window.text.get(1.0, END))


# Textbox Buttons with commands for Data tab
button_update = Button(window.tab3, text='Update', command=text_update, background='light sea green', width=10)
button_update.grid(row=0, column=0)

button_save = Button(window.tab3, text='Save', command=save, background='light sea green', width=10)
button_save.grid(row=0, column=1)

# This is to be able to select, right click and copy/paste from Data tab texbox.
window.text.bind("<Button-3>", RightClicker)

root.mainloop()
