import tkinter
from tkinter import BOTH, END
from tkinter import StringVar
from PIL import ImageTk, Image

# define root window
root = tkinter.Tk()
root.title('Hello GUI World')
root.iconbitmap('./images/wave.ico')
root.geometry('400x400')
root.resizable(0,0)

# define fonts and colors
root_color = '#224870'
input_color = '#2a4494'
output_color = '#4ea5d9'
root.config(bg=root_color)

# define functions
def submit_name():
    '''print name in output frame'''
    if case_style.get() == 'normal':
        name_label = tkinter.Label(output_frame, text="Hello " + name.get() + "!",
                             bg=output_color)
    elif case_style.get() == 'upper':
        name_label = tkinter.Label(output_frame, text=("Hello " + name.get() + "!").upper(),
                                   bg=output_color)
    name_label.pack()
    name.delete(0,END)


# define layout
# define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

# create widgets
name = tkinter.Entry(input_frame, text='Enter your name', width=20, bg='gray')
submit_button = tkinter.Button(input_frame, text='Submit', bg='gray', command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

# create radio buttons for chosing text casing
case_style = StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text='normal case', variable=case_style,
                                    value='normal', bg =input_color)
upper_button = tkinter.Radiobutton(input_frame, text='UPPER Case', variable=case_style,
                                   value='upper', bg =input_color)
normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button.grid(row=1, column=1, padx=2, pady=2)

# add image to output frame
smile_image = ImageTk.PhotoImage(Image.open('./images/smile.png'))
smile_label = tkinter.Label(output_frame, image=smile_image, bg=output_color)
smile_label.pack()


# run main loop
root.mainloop()