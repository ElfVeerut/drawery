import tkinter as tk
from tkinter import font
HEIGHT = 417
WIDTH = 626
root = tk.Tk()
data = {'elf':{'W':{'box1':[{'03.12.2019':['18.00','18.05']}],'box2':[],'box3':[],'box4':[]},
               'D':{'box1':[3,4],'box2':[],'box3':[],'box4':[]}
              }
        ,
        'dear':{'W':{'box1':[5,6],'box2':[],'box3':[],'box4':[]},
               'D':{'box1':[7,8],'box2':[],'box3':[],'box4':[]}
              }
              }
def find_cmd(user_in):
    try:
        form = [name,w_d,box]
        a = user_in.split(' ')
        if len(a) == 1:
            return data[a]

            
    except:
        return False
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

label = tk.Label(lower_frame,font=('Courier',14),anchor='nw',justify='left',bd=4)
label.place(relwidth=1, relheight=1)
root.mainloop()

# try :
#     info = user_in.split(' ')
#     if len(info) == 1:
#         label['text'] = data[user_in]
#     elif len(info) == 2:
#         label['text'] = data[info[0].lower()][info[1].upper()]
#     elif len(info) == 3:
#         label['text'] = data[info[0].lower()][info[1].upper()][info[2].lower()]
# except:
#     print(user_in)
#     label['text'] = str('NO USERNAME IN DATA')