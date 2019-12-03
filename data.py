data = {'elf':{'W':{'box1':[1,2],'box2':[],'box3':[],'box4':[]},
               'D':{'box1':[3,4],'box2':[],'box3':[],'box4':[]}
              }
        ,
        'dear':{'W':{'box1':[5,6],'box2':[],'box3':[],'box4':[]},
               'D':{'box1':[7,8],'box2':[],'box3':[],'box4':[]}
              }
              }
# print("box1:",data['elf']['W']['box1'])
# print("----------------------")
# print(data['elf']['D'])

while True:
    user_in = input("name : ")
    if user_in in data:
        print("YES")
        W_D = input("W or D : ")
        print(data[user_in][W_D.upper()])
    else:
        print("NOT FOUND")
    