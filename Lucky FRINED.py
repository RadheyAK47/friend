import random
from tkinter import*
root=Tk()

root.title("Lucky friend")
root.geometry("400x400")
root.configure(bg="cyan")

enter_name=Entry(root)
enter_name.place(relx=0.5,rely=0.2,anchor=CENTER)

friend_list=Label(root)
luckyFriend=Label(root)
random_n=Label(root)

list1=[]

def addFriend():
    friend_name=enter_name.get()
    list1.append(friend_name)
    friend_list["text"]="your friend list is : "+str(list1)
    
def randomFriend():
    length=len(list1)
    random_num=random.randint(0,length-1)
    random_n["text"]=str(random_num)
    friend=list1[random_num]
    luckyFriend["text"]="your lucky friend is : "+str(friend)
    
btn1=Button(root,text="add friend list",command=addFriend)
btn1.place(relx=0.5,rely=0.3,anchor=CENTER)
friend_list.place(relx=0.5,rely=0.4,anchor=CENTER)

btn2=Button(root,text="your lucky friend",command=randomFriend)
btn2.place(relx=0.5,rely=0.6,anchor=CENTER)
random_n.place(relx=0.5,rely=0.7,anchor=CENTER)
luckyFriend.place(relx=0.5,rely=0.8,anchor=CENTER)





root.mainloop()