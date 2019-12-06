import tkinter as tk
from tkinter import font
 
root = tk.Tk()
HEIGHT = int(root.winfo_screenheight())
WIDTH = int(root.winfo_screenwidth())
data = {'elf':[
                {'box1':[{"W":["DATE&TIME_W",'asass','ssd']}
                        ,{"D":["DATE&TIME_D"]}
                        ]
                },
                {'box2':[{"W":["DATE&TIME_W"]}
                        ,{"D":["DATE&TIME_D"]}
                        ]
                },
                {'box3':[{"W":["DATE&TIME_W"]}
                        ,{"D":["DATE&TIME_D"]}
                        ]
                },
                {'box4':[{"W":["DATE&TIME_W"]}
                        ,{"D":["DATE&TIME_D"]}
                        ]
                }
               ]

        }

def find_cmd(user_in):
    lst_word = user_in.split(" ")
    try :
        for i in range(len(lst_word)):
            if i==0:
                data_w = data[lst_word[i].lower()][0]['box1'][0]["W"]
                data_d = data[lst_word[i].lower()][0]['box1'][1]["D"]
                final_str = "box {0} withdraw = {1} \n      deposit  = {2}".format("1",data_w,data_d)

                data_w = data[lst_word[i].lower()][1]['box2'][0]["W"]
                data_d = data[lst_word[i].lower()][1]['box2'][1]["D"]
                final_str2 = "box {0} withdraw = {1} \n      deposit  = {2}".format("2",data_w,data_d)

                data_w = data[lst_word[i].lower()][2]['box3'][0]["W"]
                data_d = data[lst_word[i].lower()][2]['box3'][1]["D"]
                final_str3 = "box {0} withdraw = {1} \n      deposit  = {2}".format("3",data_w,data_d)
                
                data_w = data[lst_word[i].lower()][3]['box4'][0]["W"]
                data_d = data[lst_word[i].lower()][3]['box4'][1]["D"]
                final_str4 = "box {0} withdraw = {1} \n      deposit  = {2}".format("4",data_w,data_d)
                #
                # if lst_word[0].lower() in box_data:
                #
                #     final_str = "{0} withdraw = {1} \n deposit = {2}".format("")

            elif i == 1:
                if lst_word[i].upper() == "W":
                    final_str = "box {0} withdraw = {1}".format("1",data_w)
                    final_str2 = "box {0} withdraw = {1}".format("2",data_w)
                    final_str3 = "box {0} withdraw = {1}".format("3",data_w)
                    final_str4 = "box {0} withdraw = {1}".format("4",data_w)
                elif lst_word[i].upper() == "D":
                    final_str = "box {0} deposit = {1}".format("1",data_d)
                    final_str2 = "box {0} deposit = {1}".format("2",data_d)
                    final_str3 = "box {0} deposit = {1}".format("3",data_d)
                    final_str4 = "box {0} deposit = {1}".format("4",data_d)
                elif "box" in lst_word[i]:
                    # print("this :",data[lst_word[0]][0][lst_word[1]])
                    if lst_word[1] == 'box1':
                        final_str2 = " "
                        final_str4 = " "
                        final_str3 = " "
                    if lst_word[1] == 'box2':
                        final_str = " "
                        final_str3 = " "
                        final_str4 = " "
                    if lst_word[1] == 'box3':
                        final_str = " "
                        final_str2 = " "
                        final_str4 = " "
                    if lst_word[1] == 'box4':
                        final_str = " "
                        final_str2 = " "
                        final_str3 = " "
                else:
                    final_str = "ERROR"
                    final_str2 = " "
                    final_str3 = " "
                    final_str4 = " "


        label['text'] = final_str
        label2['text'] = final_str2
        label3['text'] = final_str3
        label4['text'] = final_str4
    except :
        print(lst_word)
        final_str = "ERROR 404"
        final_str2 = ' '
        label['text'] = final_str
        label2['text'] = final_str2
        label3['text'] = final_str2
        label4['text'] = final_str2
    
canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='asd.png') 
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0,y=0, relwidth=1, relheight=1)

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
label2.place(relwidth=0.5, relheight=0.5,relx=0.5,rely=0)

label3 = tk.Label(lower_frame,font=('Courier',12),anchor='nw',justify='left',bd=4)
label3.place(relwidth=0.5, relheight=0.5,relx=0,rely=0.5)

label4 = tk.Label(lower_frame,font=('Courier',12),anchor='nw',justify='left',bd=4)
label4.place(relwidth=0.5, relheight=0.5,relx=0.5,rely=0.5)

root.bind("<Return>",lambda event: find_cmd(user_in.get()))
root.mainloop()