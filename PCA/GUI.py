import tkinter as tk
from tkinter import font
HEIGHT = 417
WIDTH = 626
root = tk.Tk()
data = {'elf':[{"W":
                   [
                    {"box1":["DATE&TIME-1-W","DATE&TIME-2-W"]},
                    {"box2":["DATE&TIME-1-W","DATE&TIME-2-W"]},
                    {"box3":["DATE&TIME-1-W","DATE&TIME-2-W"]},
                    {"box4":["DATE&TIME-1-W","DATE&TIME-2-W"]}
                   ]   
               },
                {"D":
                   [
                    {"box1":["DATE&TIME-1-D","DATE&TIME-2-D"]},
                    {"box2":["DATE&TIME-1-D","DATE&TIME-2-D"]},
                    {"box3":["DATE&TIME-1-D","DATE&TIME-2-D"]},
                    {"box4":["DATE&TIME-1-D","DATE&TIME-2-D"]}
                   ]
                }
                ]

        }
def find_cmd(user_in):
    try :
        text = user_in.split(" ")
        print(text)
    except:
        print(user_in)
        final_str = str('USERNAME NOT IN DATA')

    label['text'] = final_str
canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='asd.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1 ,relwidth=0.75,relheight=0.1,anchor='n')

user_in = tk.Entry(frame,font=40)
user_in.place(relwidth=0.65, relheight=1)

button = tk.Button(frame,text="ENTER NAME",font=40,command=lambda: find_cmd(user_in.get()))
button.place(relx=0.7,relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,relheight=0.6, anchor='n')

label = tk.Label(lower_frame,font=('Courier',12),anchor='nw',justify='left',bd=4)
label.place(relwidth=0.5, relheight=0.5)

label2 = tk.Label(lower_frame,font=('Courier',12),anchor='nw',justify='left',bd=4)
label2.place(relwidth=0.5, relheight=0.5,relx=0.5,rely=0.5)


root.mainloop()
