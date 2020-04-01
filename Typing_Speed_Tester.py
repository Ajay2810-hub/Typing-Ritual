import os
from tkinter import ttk
import pyperclip
import PIL
from PIL import Image,ImageTk
import random
from threading import Thread
from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
import datetime

###########################################################################################################################################################################################################################
global universal,tmpu,tmpp
universal=['user']
tmpu=''
tmpp=''

global copi
copi=[]

global yes_no
yes_no=['no']

global loguser
loguser=[]

global logpass
logpass=[]

global globe
globe=[]

global yes_no1
yes_no1=['no']

global inj
inj=1

global inj_
inj_=1

global timer
timer=[]

global photo_l
photo_l=[]

current_=os.getcwd()
image_url=rf"{current_}"

##global highgwpm

con=sq.connect("TypingRitual.db")
cur=con.cursor()

##cor=cur.execute('select name from sqlite_master where type="table"')
##print(cor.fetchall())
try:
    cur.execute("create table login('yes_no' varchar(10));")
    cur.execute("insert into login values('no');")
    cur.execute("create table current_login('username' varchar(10),'password' varchar(10));")
    cur.execute("create table details('name' varchar(50),'username' varchar(10),'password' varchar(10));")
    cur.execute("create table timer('time' int);")
    cur.execute("insert into timer values(60);")
    cur.execute("create table yaar('tag' varchar(10));")
    cur.execute("create table tmp('tmpu' varchar(10),'tmpp' varchar(10));")
    cur.execute("create table cur_show('username' varchar(10));")
    cur.execute("create table words('wrd' varchar(50));")
    cur.execute("create table fol('username' varchar(10),'password' varchar(10));")
except:
    pass

cur.execute("insert into yaar values('no');")
slt=cur.execute("select * from current_login;")
for d in slt:
    loguser.append(d[0])
    logpass.append(d[1])

con.commit()

if (not loguser)==False and (not logpass)==False:
   sold=cur.execute(f"select * from {loguser[-1]}{logpass[-1]}photo;")
   for ui in sold:
       universal.append(ui[0])
   
############################################################################################################################################################################################################################################################################################################################################################################

win=Tk()
win.geometry("1400x800")
win.title("Type Speed Tester")
win['bg']="orange"
win.resizable(width=False,height=False)

head=Label(win,width=72,text="Welcome To Typing Ritual",fg="orange",bg="#fff",bd=0,font="helvetica 25 bold")
head.place(x=0,y=0)

photo=PhotoImage(file=rf"{image_url}\TST_Images\keyboard.png")
logo=Label(win,image=photo,bg="orange",bd=0)
logo.place(x=550,y=140)

logo1=Label(win,text="Typing Ritual",fg="#fff",bg='orange',bd=0,font="helvetica 30 bold")
logo1.place(x=550,y=400)

def start1():
    start2()
    
start=Button(win,cursor="hand2",command=start1,text="Start Using Typing Ritual",fg="orange",bg="#fff",bd=0,activeforeground="#fff",activebackground="orange",font="helvetica 20 bold",width=68)
start.place(x=100,y=550)

########################################################################################################################################################################################

user__=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\user.png",mode='r'))
user1=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\user1.png",mode='r'))
user2=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\user2.png",mode='r'))
user3=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\user3.png",mode='r'))
user4=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\user4.png",mode='r'))
men=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\men.png",mode='r'))
beard=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\beard.png",mode='r'))
man=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\man.png",mode='r'))
boy=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\boy.png",mode='r'))
girl=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\girl.png",mode='r'))
donuts=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\donuts.png",mode='r'))
happy=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\happy.png",mode='r'))
happy1=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\happy1.png",mode='r'))
ice_cream=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\ice-cream.png",mode='r'))
sweet=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\sweet.png",mode='r'))
umbrella=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\umbrella.png",mode='r'))

global uni
uni={'user':user__,'user1':user1,'user2':user2,'beard':beard,'men':men,'man':man,"boy":boy,"girl":girl,'donuts':donuts,'happy':happy,'happy1':happy1,'ice-cream':ice_cream,'sweet':sweet,'umbrella':umbrella,'user3':user3,"user4":user4}

_user__=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\user.png",mode='r'))
_user1=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\user1.png",mode='r'))
_user2=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\user2.png",mode='r'))
_user3=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\user3.png",mode='r'))
_user4=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\user4.png",mode='r'))
_men=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\men.png",mode='r'))
_beard=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\beard.png",mode='r'))
_man=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\man.png",mode='r'))
_boy=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\boy.png",mode='r'))
_girl=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\girl.png",mode='r'))
_donuts=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\donuts.png",mode='r'))
_happy=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\happy.png",mode='r'))
_happy1=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\happy1.png",mode='r'))
_ice_cream=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\ice-cream.png",mode='r'))
_sweet=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\sweet.png",mode='r'))
_umbrella=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\TST_Images1\umbrella.png",mode='r'))

global uni1
uni1={'user':_user__,'user1':_user1,'user2':_user2,'beard':_beard,'men':_men,'man':_man,"boy":_boy,"girl":_girl,'donuts':_donuts,'happy':_happy,'happy1':_happy1,'ice-cream':_ice_cream,'sweet':_sweet,'umbrella':_umbrella,'user3':_user3,"user4":_user4}

################################################################################################################################################################################

lbl1=Label(win,text="none",fg="#fff",bg="#fff",bd=0,width=20,height=13,font="helvetica 20")

login_lbl=Label(win,text="User Login",fg="orange",bg="#fff",bd=0,font="helvetica 20 underline bold")

uname=Entry(win,fg="#fff",bg="orange",font="helvetica 18",bd=0,width=21)
uname.insert(END,"        Enter Username")

def uname1(event):
    if str(uname.get())=="        Enter Username":
       uname.delete(first=0,last=len(str(uname.get())))
    
uname.bind("<FocusIn>",uname1)

def uname2(event):
    if not str(uname.get()):
       uname.insert(END,"        Enter Username")
    
uname.bind("<FocusOut>",uname2)

pwd=Entry(win,fg="#fff",bg="orange",font="helvetica 18",bd=0,width=21)
pwd.insert(END,"        Enter Password")

def show__():
    show___()
    
show_=PhotoImage(file=rf"{image_url}\TST_Images\visibility.png")
show_btn=Button(win,cursor="hand2",command=show__,image=show_,bg="orange",activebackground="orange",bd=0)

def blind__():
    blind___()
    
blind_=PhotoImage(file=rf"{image_url}\TST_Images\blind.png")
blind_btn=Button(win,cursor="hand2",command=blind__,image=blind_,bg="orange",activebackground="orange",bd=0)

def show___():
    yes_no.append('no')
    show_btn.place(x=-1500,y=352)
    blind_btn.place(x=648,y=352)
    pwd.config(show="*")

def blind___():
    yes_no.append('yes')
    blind_btn.place(x=-1500,y=352)
    show_btn.place(x=648,y=352)
    pwd.config(show="")
    
def pwd1(event):
    if str(pwd.get())=="        Enter Password":
       pwd.delete(first=0,last=len(str(pwd.get())))
       if inj==0:
          blind_btn.place(x=648,y=352)
       show_btn.place(x=-1500,y=0)
       yes_no.append('no')
       pwd.config(show="*")
    
pwd.bind("<FocusIn>",pwd1)

def pwd2(event):
    if not str(pwd.get()):
       pwd.insert(END,"        Enter Password")
       pwd.config(show="")
    
pwd.bind("<FocusOut>",pwd2)

def login():
    login1()

log_btn=Button(win,cursor="hand2",command=login,text="LOGIN",width=10,bg="orange",fg="#fff",bd=0,font="helvetica 20 bold",activebackground="#fff",activeforeground="orange")

##################################################################################################################################################################################################################

lbl2=Label(win,text="none",fg="#fff",bg="#fff",bd=0,width=20,height=13,font="helvetica 20")

register_lbl=Label(win,text="Registration",fg="orange",bg="#fff",bd=0,font="helvetica 20 underline bold")

name_=Entry(win,fg="#fff",bg="orange",bd=0,font="helvetica 18",width=21)
name_.insert(END,"           Enter Name")

uname_=Entry(win,fg="#fff",bg="orange",bd=0,font="helvetica 18",width=21)
uname_.insert(END,"        Enter Username")

pwd_=Entry(win,fg="#fff",bg="orange",bd=0,font="helvetica 18",width=21)
pwd_.insert(END,"        Enter Password")

def show1__():
    show1___()

show1_btn=Button(win,cursor="hand2",command=show1__,image=show_,bg="orange",activebackground="orange",bd=0)

def blind1__():
    blind1___()

blind1_btn=Button(win,cursor="hand2",command=blind1__,image=blind_,bg="orange",activebackground="orange",bd=0)

def show1___():
    yes_no1.append('no')
    show1_btn.place(x=-1500,y=352)
    blind1_btn.place(x=970,y=390)
    pwd_.config(show="*")

def blind1___():
    yes_no1.append('yes')
    blind1_btn.place(x=-1500,y=352)
    show1_btn.place(x=970,y=390)
    pwd_.config(show="")

def register():
    register1()
    
reg_btn=Button(win,command=register,cursor="hand2",text="Register",width=10,bg="orange",fg="#fff",bd=0,font="helvetica 20 bold",activebackground="#fff",activeforeground="orange")

def pwd_1(event):
    if str(pwd_.get())=="        Enter Password":
       pwd_.delete(first=0,last=len(str(pwd_.get())))
       if inj_==0:
          blind1_btn.place(x=970,y=390)
       show1_btn.place(x=-1500,y=0)
       yes_no1.append('no')
       pwd_.config(show="*")
    
pwd_.bind("<FocusIn>",pwd_1)

def pwd_2(event):
    if not str(pwd_.get()):
       pwd_.insert(END,"        Enter Password")
       pwd_.config(show="")
    
pwd_.bind("<FocusOut>",pwd_2)

def uname_1(event):
    if str(uname_.get())=="        Enter Username":
       uname_.delete(first=0,last=len(str(uname_.get())))
    
uname_.bind("<FocusIn>",uname_1)

def uname_2(event):
    if not str(uname_.get()):
       uname_.insert(END,"        Enter Username")
    
uname_.bind("<FocusOut>",uname_2)

def name_1(event):
    if str(name_.get())=="           Enter Name":
       name_.delete(first=0,last=len(str(name_.get())))
    
name_.bind("<FocusIn>",name_1)

def name_2(event):
    if not str(name_.get()):
       name_.insert(END,"           Enter Name")
    
name_.bind("<FocusOut>",name_2)

def on_lbl2(event):
    lbl1.config(bg="orange",fg="orange")
    login_lbl.place(x=-1500,y=0)
    uname.place(x=-1500,y=0)
    pwd.place(x=-1500,y=0)
    log_btn.place(x=-1500,y=0)
    show_btn.place(x=-1500,y=352)
    blind_btn.place(x=-1500,y=352)
    inj=1
    inj_=0
    #reg
    lbl2.config(bg="#fff",fg="#fff")
    register_lbl.place(x=787,y=180)
    name_.place(x=722,y=270)
    uname_.place(x=722,y=330)
    if yes_no1[-1]=='yes':
       show1_btn.place(x=970,y=390)
    else:
       blind1_btn.place(x=970,y=390)
    pwd_.place(x=722,y=390)
    reg_btn.place(x=772,y=470)
    
lbl2.bind("<Enter>",on_lbl2)

def on_lbl1(event):
    lbl1.config(bg="#fff",fg="#fff")
    login_lbl.place(x=465,y=180)
    uname.place(x=400,y=270)
    pwd.place(x=400,y=350)
    log_btn.place(x=450,y=450)
    inj=0
    inj_=1
    if yes_no[-1]=='yes':
       show_btn.place(x=648,y=352)
    else:
       blind_btn.place(x=648,y=352)
    #reg
    lbl2.config(bg="orange",fg="orange")
    register_lbl.place(x=-1500,y=180)
    name_.place(x=-1500,y=270)
    uname_.place(x=-1500,y=330)
    pwd_.place(x=-1500,y=390)
    reg_btn.place(x=-1500,y=470)
    show1_btn.place(x=-1500,y=352)
    blind1_btn.place(x=-1500,y=352)
    
lbl1.bind("<Enter>",on_lbl1)

######################################################################################################################################################################################################################################################

head1=Label(win,width=72,text="Typing Ritual",fg="orange",bg="#fff",bd=0,font="helvetica 25 bold",height=1)

def navigate():
    if (not timer)==False:
       win.after_cancel(timer[-1])
    clock.config(text="01:00")
    cur.execute("insert into timer values(59);")
    con.commit()
    navigation()
    
navimg=PhotoImage(file=rf"{image_url}\TST_Images\nav_bar.png")
nav_btn=Button(win,cursor="hand2",command=navigate,image=navimg,bg="#fff",activebackground="#fff",bd=0)

sent_win=Label(win,text="",wraplength=840,bd=0,borderwidth=1,relief=SOLID,fg="grey",bg="#fff",font="helvetica 20 bold",width=50,height=7)

txt=Entry(win,bd=0,font="helvetica 20",borderwidth=2,relief=SOLID,fg="#000",bg="#fff",width=57)

clock=Label(win,text="01:00",bg="#000",font="helvetica 20 bold",fg="orange",bd=0,width=10,height=2)

def null():
    messagebox.showinfo("Typing Ritual","Time's Up!")

def on(event):
    uu1=[]
    sel=cur.execute("select * from yaar;")
    for uu in sel:
        uu1.append(uu)
    if uu1[-1][0]=='no':
       countdown1()

def countdown1():
    t=[]
    sel=cur.execute("select * from timer;")
    for i in sel:
        t.append(int(i[0]))
    cur.execute(f"insert into timer values({int(t[-1])-1});")
    con.commit()
    countdown(t[-1])
    
def countdown(x):
    cur.execute("insert into yaar values('yes');")
    if x==60:
       clock.config(text="01:00")
    elif x<10 and x!=0:
       clock.config(text=f"00:0{x}")
    elif x>10 and x!=60 and x!=0:
       clock.config(text=f"00:{x}")
    if x<=0:
       clock.configure(text="00:00")
       cur.execute("insert into timer values(59);")
       cur.execute("insert into yaar values('yes');")
       con.commit()
       win.after_cancel(timer[-1])
       messagebox.showinfo("Typing Ritual","time's Up!")
       chk()
    else:
       fh=win.after(1000,countdown1)
       timer.append(fh)
       
txt.bind("<FocusIn>",on)

def chk():
    a=str(txt.get())
    txt.delete(first=0,last=len(a))
    txt.config(state=DISABLED)
    win.after_cancel(timer[-1])
    clock.config(text="01:00")
    result(a)

def reset():
    if (not timer)==False:
       win.after_cancel(timer[-1])
    clock.config(text="01:00")
    cur.execute("insert into timer values(59);")
    cur.execute("insert into yaar values('no');")
    con.commit()
    txt.delete(first=0,last=len(str(txt.get())))
    txt.config(state=DISABLED)
    txt.config(state=NORMAL)
    win.after(1000,countdown1)
    null1234()
    sentence()
    
reset_btn=Button(win,text="Restart",command=reset,font="helvetica 25",fg="orange",bg="#fff",width=10,bd=0,activebackground="orange",activeforeground="#fff",cursor="hand2",borderwidth=1,relief=SOLID)

##########################################################################################################################################################

side_nav=Label(win,text="",fg="#fff",bg="#fff",font="helvetica 20",width=15,height=25,bd=0,borderwidth=2,relief=SOLID)

line=Label(win,text="",font="helvetica 20",bg="#fff",width=15,height=4,bd=0,borderwidth=1,relief=SOLID)

def profil():
    profil1()

prof=PIL.ImageTk.PhotoImage(PIL.Image.open(rf"{image_url}\TST_Images\{universal[-1]}.png",mode='r'))
profile=Button(win,image=prof,command=profil,bg="#fff",activebackground="#fff",bd=0,cursor="hand2")

def home_():
    if (not timer)==False:
       win.after_cancel(timer[-1])
    clock.config(text="01:00")
    txt.config(state=DISABLED)
    cur.execute("insert into timer values(59);")
    con.commit()
    gayab()

home_btn=Button(win,activeforeground="#fff",activebackground="orange",cursor="hand2",command=home_,anchor=W,justify=LEFT,text="  Home",fg="orange",bg="#fff",bd=0,font="helvetica 18",width=17,height=2)

def home(event):
    home_btn.config(fg="#fff",bg="orange")
    
home_btn.bind('<Enter>',home)

def home1(event):
    home_btn.config(bg="#fff",fg="orange")
    
home_btn.bind('<Leave>',home1)

def quick_():
    if (not timer)==False:
       win.after_cancel(timer[-1])
    clock.config(text="01:00")
    txt.config(state=DISABLED)
    cur.execute("insert into timer values(59);")
    con.commit()
    quick1_()

quick_btn=Button(win,activeforeground="#fff",activebackground="orange",command=quick_,cursor="hand2",anchor=W,justify=LEFT,text="  Quick Sentences",fg="orange",bg="#fff",bd=0,font="helvetica 18",width=17,height=2)

def quick(event):
    quick_btn.config(fg="#fff",bg="orange")
    
quick_btn.bind('<Enter>',quick)

def quick1(event):
    quick_btn.config(bg="#fff",fg="orange")
    
quick_btn.bind('<Leave>',quick1)

def rank_():
    if (not timer)==False:
       win.after_cancel(timer[-1])
    txt.config(state=DISABLED)
    clock.config(text="01:00")
    cur.execute("insert into timer values(59);")
    con.commit()
    ranks()

rank_btn=Button(win,command=rank_,cursor="hand2",anchor=W,justify=LEFT,activeforeground="#fff",activebackground="orange",text="  Scoreboard",fg="orange",bg="#fff",bd=0,font="helvetica 18",width=17,height=2)

def rank(event):
    rank_btn.config(fg="#fff",bg="orange")
    
rank_btn.bind('<Enter>',rank)

def rank1(event):
    rank_btn.config(bg="#fff",fg="orange")
    
rank_btn.bind('<Leave>',rank1)

def fre_():
    if (not timer)==False:
       win.after_cancel(timer[-1])
    clock.config(text="01:00")
    txt.config(state=DISABLED)
    cur.execute("insert into timer values(59);")
    con.commit()
    fre1_()
 
fre_btn=Button(win,command=fre_,cursor="hand2",anchor=W,justify=LEFT,activeforeground="#fff",activebackground="orange",text="  Find Friends",fg="orange",bg="#fff",bd=0,font="helvetica 18",width=17,height=2)

def fre(event):
    fre_btn.config(fg="#fff",bg="orange")
    
fre_btn.bind('<Enter>',fre)

def fre1(event):
    fre_btn.config(bg="#fff",fg="orange")
    
fre_btn.bind('<Leave>',fre1)

def sin_out_():
    if (not timer)==False:
       win.after_cancel(timer[-1])
    clock.config(text="01:00")
    txt.config(state=DISABLED)
    cur.execute("insert into timer values(59);")
    con.commit()
    log_out()
 
sin_out_btn=Button(win,command=sin_out_,cursor="hand2",anchor=W,justify=LEFT,activeforeground="#fff",activebackground="orange",text="  Sign Out",fg="orange",bg="#fff",bd=0,font="helvetica 18",width=17,height=2)

def sin_out(event):
    sin_out_btn.config(fg="#fff",bg="orange")
    
sin_out_btn.bind('<Enter>',sin_out)

def sin_out1(event):
    sin_out_btn.config(bg="#fff",fg="orange")
    
sin_out_btn.bind('<Leave>',sin_out1)

def renavigate():
    renavigation()

nav1img=PhotoImage(file=rf"{image_url}\TST_Images\nav_bar_1.png")
re_nav_btn=Button(win,cursor="hand2",command=renavigate,image=nav1img,bg="#fff",activebackground="#fff",bd=0)

##############################################################################################################################################################################

result_patch=Label(win,text="",fg="#fff",bg="#fff",width=50,font="helvetica 20",height=12,bd=0)

gwpm=Label(win,text="GROSS WPM",fg="crimson",bg="#fff",bd=0,font="helvetica 25 underline")
gwpm1=Label(win,text="",fg="lightgreen",bg="#fff",bd=0,font="helvetica 80")

Acc=Label(win,text="ACCURACY",fg="crimson",bg="#fff",bd=0,font="helvetica 25 underline")
Acc1=Label(win,text="",fg="lightgreen",bg="#fff",bd=0,font="helvetica 60")

net_wpm=Label(win,text="NET WPM",fg="crimson",bg="#fff",bd=0,font="helvetica 25 underline")
net_wpm1=Label(win,text="",fg="lightgreen",bg="#fff",bd=0,font="helvetica 80")

def _back_():
    _back1_()

back__=PhotoImage(file=rf"{image_url}\TST_Images\back.png")
back_btn=Button(win,image=back__,bg="#fff",command=_back_,bd=0,activebackground="#fff",cursor="hand2")

###########################################################################################################################################################################################################################

white=Label(win,text="",font="helvetica 20",fg="#fff",bg="#fff",bd=0,width=50,height=15)

__name__=Label(win,text="NAME : ",fg="crimson",bg="#fff",bd=0,font="helvetica 25 bold")
__name1__=Entry(win,fg="orange",bg="#fff",font="helvetica 20 bold",bd=0,width=18)

edit_=PhotoImage(file=rf"{image_url}\TST_Images\edit.png")

def ed1():
    ed1_1()
    
edit1=Button(win,image=edit_,bg="#fff",activebackground="#fff",bd=0,command=ed1,cursor="hand2")

__uname__=Label(win,text="USERNAME : ",fg="crimson",bg="#fff",bd=0,font="helvetica 25 bold")
__uname1__=Entry(win,fg="orange",bg="#fff",font="helvetica 20 bold",bd=0,width=13)

if (not loguser)==False:
   select_=cur.execute(f"select * from details where username='{loguser[-1]}';")
   for tu in select_:
       nam_e=tu[0]
       use_r=tu[1]
   tmpu=f" {nam_e}"
   tmpp=f' {use_r}'
   __name1__.insert(END,f' {nam_e}')
   __uname1__.insert(END,f' {use_r}')

__name1__.config(state=DISABLED)
__uname1__.config(state=DISABLED)

def ed2():
    ed2_1()
    
edit2=Button(win,image=edit_,bg="#fff",activebackground="#fff",cursor="hand2",bd=0,command=ed2)

def ed1_1():
    __name1__.config(state=NORMAL,borderwidth=1,relief=SOLID)
    __uname1__.delete(first=0,last=len(__uname1__.get()))
    __uname1__.insert(END,tmpp)
    __uname1__.config(state=DISABLED,borderwidth=0)

def ed2_1():
    __uname1__.config(state=NORMAL,borderwidth=1,relief=SOLID)
    __name1__.delete(first=0,last=len(str(__name1__.get())))
    __name1__.insert(END,tmpu)
    __name1__.config(state=DISABLED,borderwidth=0)

def save_name(event):
    a=str(__name1__.get())
    if len(a)!=0:
       __name1__.config(state=DISABLED,bd=0)
       tmpu=f" {a}"
       cur.execute(f"update details set name='{a.strip()}' where username='{loguser[-1]}';")
       con.commit()
    elif len(a)==0:
       selfh=cur.execute("select * from tmp;")
       for tu in selfh:
           tu=tu
       __name1__.insert(END,tu[0])
       __name1__.config(state=DISABLED,bd=0)

__name1__.bind('<Return>',save_name)

def save_uname(event):
    a=str(__uname1__.get())
    if len(a)!=0 and len(a)>4 and len(a)<10:
       __uname1__.config(state=DISABLED,bd=0)
       tmpp=f" {a}"
       cur.execute(f"create table {a.strip()}{logpass[-1]}code('_code_' varchar(12));")
       sed=cur.execute(f"select * from {loguser[-1]}{logpass[-1]}code;")
       for i in sed:
           cur.execute(f"insert into {a.strip()}{logpass[-1]}code values('{i[0]}');")
       cur.execute(f"drop table {loguser[-1]}{logpass[-1]}code;")
       cur.execute(f"update details set username='{a.strip()}' where username='{loguser[-1]}';")
       cur.execute(f"create table {a.strip()}{logpass[-1]}photo('url' varchar(10));")
       sed1=cur.execute(f"select * from {loguser[-1]}{logpass[-1]}photo;")
       for i1 in sed1:
           cur.execute(f"insert into {a.strip()}{logpass[-1]}photo values('{i1[0]}');")
       cur.execute(f"drop table {loguser[-1]}{logpass[-1]}photo")
       cur.execute(f"create table {a.strip()}{logpass[-1]}scores('gross wpm' int,'net wpm' int,'accuracy' float,'date' varchar(10),'time' varchar(10));")
       sed2=cur.execute(f"select * from {loguser[-1]}{logpass[-1]}scores;")
       for i2 in sed2:
           cur.execute(f"insert into {a.strip()}{logpass[-1]}scores values({i2[0]},{i2[1]},{i2[2]},'{i2[3]}','{i2[4]}');")
       cur.execute(f"drop table {loguser[-1]}{logpass[-1]}scores;")
       cur.execute(f"insert into current_login values('{a.strip()}','{logpass[-1]}');")
       cur.execute(f"create table {a.strip()}{logpass[-1]}followers('username' varchar(10));")
       sed3=cur.execute(f"select * from {loguser[-1]}{logpass[-1]}followers;")
       for i3 in sed3:
           cur.execute(f"insert into {a.strip()}{logpass[-1]}followers values('{i3[0]}');")
       cur.execute(f"drop table {loguser[-1]}{logpass[-1]}followers;")
       cur.execute(f"create table {a.strip()}{logpass[-1]}following('username' varchar(10));")
       sed4=cur.execute(f"select * from {loguser[-1]}{logpass[-1]}following;")
       for i4 in sed4:
           cur.execute(f"insert into {a.strip()}{logpass[-1]}following values('{i4[0]}');")
       cur.execute(f"drop table {loguser[-1]}{logpass[-1]}following;")
       con.commit()

       ###

       users_=[]
       passs_=[]
       sed5=cur.execute("select username,password from details;")
       for iot in sed5:
           if iot[0]!=a.strip():
              users_.append(iot[0])
              passs_.append(iot[1])
       for iot1 in users_:
           for iot2 in cur.execute(f"select * from {iot1}{passs_[users_.index(iot1)]}followers;"):
               if loguser[-1] in iot2:
                  cur.execute(f"update {iot1}{passs_[users_.index(iot1)]}followers set username='{a.strip()}' where username='{loguser[-1]}';")
                  con.commit()
       for uu in users_:
           for uu1 in cur.execute(f"select * from {uu}{passs_[users_.index(uu)]}following;"):
               if loguser[-1] in uu1:
                  cur.execute(f"update {iot1}{passs_[users_.index(uu)]}following set username='{a.strip()}' where username='{loguser[-1]}';")
                  con.commit()

       ###
       
       loguser.append(f'{a.strip()}')
    else:
       __uname1__.delete(first=0,last=len(a))
       __uname1__.insert(END,f" {loguser[-1]}")
       __uname1__.config(state=DISABLED,bd=0)

__uname1__.bind('<Return>',save_uname)

ref_code=Label(win,text="",bg="orange",fg="#fff",bd=0,borderwidth=1,relief=SOLID,font="helvetica 20",width=15)

if (not loguser)==False:
   sele=cur.execute(f"select * from {loguser[-1]}{logpass[-1]}code;")
   for huge in sele:
       ref_code.config(text=f"{huge[0]}")
       copi.append(huge)

def copy_():
    __name1__.delete(first=0,last=len(str(__name1__.get())))
    __name1__.insert(END,tmpu)
    __name1__.config(state=DISABLED,borderwidth=0)
    pyperclip.copy(copi[-1][0])
    __uname1__.delete(first=0,last=len(__uname1__.get()))
    __uname1__.insert(END,tmpp)
    __uname1__.config(state=DISABLED,borderwidth=0)

imdb=PhotoImage(file=rf"{image_url}\TST_Images\copy.png")
copy_btn=Button(win,image=imdb,cursor="hand2",bg="orange",bd=0,command=copy_,activebackground="orange",borderwidth=1,relief=SOLID)

prof_image=Label(win,bg="#fff",bd=0)

def get_back():
    get_back1()

back_btn1=Button(win,command=get_back,cursor="hand2",image=back__,bg="#fff",activebackground="#fff",bd=0)

def pic():
    pic1()
    
edit1_=PhotoImage(file=rf"{image_url}\TST_Images\edit1.png")
edit_btn=Button(win,image=edit1_,command=pic,cursor="hand2",bg="#fff",activebackground="#fff",bd=0)

def show_it(event):
    edit_btn.place(x=479,y=229)

prof_image.bind('<Enter>',show_it)

def hide_it(event):
    edit_btn.place(x=-1500,y=249)

prof_image.bind('<Leave>',hide_it)
edit_btn.bind('<Leave>',hide_it)
edit_btn.bind('<Enter>',show_it)

follower=Label(win,text="Followers",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
follower1=Label(win,text="0",fg="crimson",bg="#fff",bd=0,font="helvetica 20")

following1=Label(win,text="0",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
following=Label(win,text="Following",fg="crimson",bg="#fff",bd=0,font="helvetica 20")

avg_gwpm=Label(win,text="Average\nGross WPM",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
avg_gwpm1=Label(win,text="0",fg="lightgreen",bg="#fff",bd=0,font="helvetica 30")

avg_acc=Label(win,text="Average\nAccuracy",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
avg_acc1=Label(win,text="0",fg="lightgreen",bg="#fff",bd=0,font="helvetica 30")

avg_nwpm=Label(win,text="Average\nNet WPM",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
avg_nwpm1=Label(win,text="0",fg="lightgreen",bg="#fff",bd=0,font="helvetica 30")

##############################################################################################################################################################################################################################################

white1=Label(win,text="",font="helvetica 20",fg="#fff",bg="#fff",bd=0,width=50,height=15)

def pics_(a):
    cur.execute(f"update {loguser[-1]}{logpass[-1]}photo set url='{a}' where url='{universal[-1]}';")
    universal.append(str(a))
    profile.config(image=uni[str(a)])
    prof_image.config(image=uni1[str(a)])
    con.commit()

beard_img=Button(win,command=lambda : pics_("beard"),cursor="hand2",image=uni1['beard'],bg="#fff",activebackground="#fff",bd=0)
boy_img=Button(win,command=lambda : pics_("boy"),cursor="hand2",image=uni1['boy'],bg="#fff",activebackground="#fff",bd=0)
donuts_img=Button(win,command=lambda : pics_("donuts"),cursor="hand2",image=uni1['donuts'],bg="#fff",activebackground="#fff",bd=0)
girl_img=Button(win,command=lambda : pics_("girl"),cursor="hand2",image=uni1['girl'],bg="#fff",activebackground="#fff",bd=0)
happy_img=Button(win,command=lambda : pics_("happy"),cursor="hand2",image=uni1['happy'],bg="#fff",activebackground="#fff",bd=0)
happy1_img=Button(win,command=lambda : pics_("happy1"),cursor="hand2",image=uni1['happy1'],bg="#fff",activebackground="#fff",bd=0)
ice_cream_img=Button(win,command=lambda : pics_("ice-cream"),cursor="hand2",image=uni1['ice-cream'],bg="#fff",activebackground="#fff",bd=0)
man_img=Button(win,command=lambda : pics_("man"),cursor="hand2",image=uni1['man'],bg="#fff",activebackground="#fff",bd=0)

def a(event):
    beard_img.config(bg="orange")
beard_img.bind("<Enter>",a)
def b(event):
    beard_img.config(bg="#fff")
beard_img.bind("<Leave>",b)
def c(event):
    boy_img.config(bg="orange")
boy_img.bind("<Enter>",c)
def d(event):
    boy_img.config(bg="#fff")
boy_img.bind("<Leave>",d)

def e(event):
    donuts_img.config(bg="orange")
donuts_img.bind("<Enter>",e)
def f(event):
    donuts_img.config(bg="#fff")
donuts_img.bind("<Leave>",f)
def g(event):
    girl_img.config(bg="orange")
girl_img.bind("<Enter>",g)
def h(event):
    girl_img.config(bg="#fff")
girl_img.bind("<Leave>",h)

#reg

def a1(event):
    happy_img.config(bg="orange")
happy_img.bind("<Enter>",a1)
def b1(event):
    happy_img.config(bg="#fff")
happy_img.bind("<Leave>",b1)
def c1(event):
    ice_cream_img.config(bg="orange")
ice_cream_img.bind("<Enter>",c1)
def d1(event):
    ice_cream_img.config(bg="#fff")
ice_cream_img.bind("<Leave>",d1)

def e1(event):
    man_img.config(bg="orange")
man_img.bind("<Enter>",e1)
def f1(event):
    man_img.config(bg="#fff")
man_img.bind("<Leave>",f1)
def g1(event):
    happy1_img.config(bg="orange")
happy1_img.bind("<Enter>",g1)
def h1(event):
    happy1_img.config(bg="#fff")
happy1_img.bind("<Leave>",h1)

def nxt_():
    nxt1_()

next__=PhotoImage(file=rf"{image_url}\TST_Images\chevron-r.png")
nxt_btn=Button(win,bg="#fff",image=next__,bd=0,command=nxt_,cursor="hand2")

def pre_():
    pre1_()

prev__=PhotoImage(file=rf"{image_url}\TST_Images\chevron-l.png")
prev_btn=Button(win,bg="#fff",image=prev__,bd=0,command=pre_,cursor="hand2")


men_img=Button(win,command=lambda : pics_("men"),cursor="hand2",image=uni1['men'],bg="#fff",activebackground="#fff",bd=0)
sweet_img=Button(win,command=lambda : pics_("sweet"),cursor="hand2",image=uni1['sweet'],bg="#fff",activebackground="#fff",bd=0)
umbrella_img=Button(win,command=lambda : pics_("umbrella"),cursor="hand2",image=uni1['umbrella'],bg="#fff",activebackground="#fff",bd=0)
user_img=Button(win,command=lambda : pics_("user"),cursor="hand2",image=uni1['user'],bg="#fff",activebackground="#fff",bd=0)
user1_img=Button(win,command=lambda : pics_("user1"),cursor="hand2",image=uni1['user1'],bg="#fff",activebackground="#fff",bd=0)
user2_img=Button(win,command=lambda : pics_("user2"),cursor="hand2",image=uni1['user2'],bg="#fff",activebackground="#fff",bd=0)
user3_img=Button(win,command=lambda : pics_("user3"),cursor="hand2",image=uni1['user3'],bg="#fff",activebackground="#fff",bd=0)
user4_img=Button(win,command=lambda : pics_("user4"),cursor="hand2",image=uni1['user4'],bg="#fff",activebackground="#fff",bd=0)

def a2(event):
    men_img.config(bg="orange")
men_img.bind("<Enter>",a2)
def b2(event):
    men_img.config(bg="#fff")
men_img.bind("<Leave>",b2)
def c2(event):
    sweet_img.config(bg="orange")
sweet_img.bind("<Enter>",c2)
def d2(event):
    sweet_img.config(bg="#fff")
sweet_img.bind("<Leave>",d2)

def e2(event):
    umbrella_img.config(bg="orange")
umbrella_img.bind("<Enter>",e2)
def f2(event):
    umbrella_img.config(bg="#fff")
umbrella_img.bind("<Leave>",f2)
def g2(event):
    user_img.config(bg="orange")
user_img.bind("<Enter>",g2)
def h2(event):
    user_img.config(bg="#fff")
user_img.bind("<Leave>",h2)

#reg

def a3(event):
    user1_img.config(bg="orange")
user1_img.bind("<Enter>",a3)
def b3(event):
    user1_img.config(bg="#fff")
user1_img.bind("<Leave>",b3)
def c3(event):
    user2_img.config(bg="orange")
user2_img.bind("<Enter>",c3)
def d3(event):
    user2_img.config(bg="#fff")
user2_img.bind("<Leave>",d3)

def e3(event):
    user3_img.config(bg="orange")
user3_img.bind("<Enter>",e3)
def f3(event):
    user3_img.config(bg="#fff")
user3_img.bind("<Leave>",f3)
def g3(event):
    user4_img.config(bg="orange")
user4_img.bind("<Enter>",g3)
def h3(event):
    user4_img.config(bg="#fff")
user4_img.bind("<Leave>",h3)

def _cancel_():
    cancel_()

cancel_btn=Button(win,text="Cancel",command=_cancel_,bg="#fff",fg="orange",bd=0,font="helvetica 15",cursor="hand2",activeforeground="#fff",activebackground="orange")

def onn(event):
    cancel_btn.config(fg="#fff",bg="orange")

cancel_btn.bind('<Enter>',onn)

def off(event):
    cancel_btn.config(bg="#fff",fg="orange")

cancel_btn.bind('<Leave>',off)

############################################################################################################################################################################################################

search_bar=Entry(win,fg="orange",bg="#fff",bd=0,borderwidth=1,relief=SOLID,width=30,font="helvetica 30",justify=CENTER)
search_bar.insert(END,"Search Here...")

search_list=Listbox(win,bg="#fff",fg="crimson",bd=0,width=39,font="helvetica 23",height=1)

def search_(event):
    for jk in range(0,search_list.size()):
        for iu in range(0,search_list.size()):
            search_list.delete(jk)
    win.after(1,search1_)

def cyum(event):
    cyum1()

search_list.bind('<Double-1>',cyum)

def search1_():
    a=str(search_bar.get())
    for jk in range(0,search_list.size()):
        search_list.delete(jk)
    if len(a)!=0:
        search_list.place(x=400,y=149)
        s_e_l=cur.execute("select username,password from details;")
        user_s=[]
        pass_s=[]
        for ug in s_e_l:
            user_s.append(ug[0])
            pass_s.append(ug[1])
        codes=[]
        coder=[]
        for ti in user_s:
            try:
              selh=cur.execute(f"select _code_ from {ti}{pass_s[user_s.index(ti)]}code;")
              for tj in selh:
                  codes.append(str(tj[0]).replace(' ',''))
            except:
              continue
        k=0
        for ty in user_s:
            if a.lower() in ty.lower() or a==codes[user_s.index(str(ty))]:
               coder.append(ty)
               k+=1
            elif a=="*":
               coder.append(ty)
               k+=1
            elif a=="@":
               coder.append(codes[user_s.index(str(ty))])
               k+=1
        if k!=0:
           for gp in coder:
               search_list.insert(END,f" {gp}")
           if search_list.size()>13:
              search_list.config(height=13)
           else:
              search_list.config(height=search_list.size())
        else:
           search_list.place(x=-1500,y=0)
    else:
       search_list.config(height=1)
       search_list.place(x=-1500,y=0)
y=65
while y<=90:
    search_bar.bind(f'{chr(y)}',search_)
    search_bar.bind(f'{chr(y+32)}',search_)
    y+=1
search_bar.bind('<BackSpace>',search_)
for yt in range(0,10):
    search_bar.bind(f'{yt}',search_)
search_bar.bind('_',search_)
search_bar.bind('*',search_)
search_bar.bind('@',search_)

def clg(event):
    dc=str(search_bar.get())
    if len(dc)!="Search Here...":
       search_bar.delete(first=0,last=len('Search Here...'))

search_bar.bind('<FocusIn>',clg)

def clg1(event):
    dc=str(search_bar.get())
    if len(dc)!="Search Here..." and len(dc)==0:
       search_bar.insert(END,'Search Here...')

search_bar.bind('<FocusOut>',clg1)

################################################################################################################################################################################################################################

white2=Label(win,text="",font="helvetica 20",fg="#fff",bg="#fff",bd=0,width=50,height=15)

__name_1_=Label(win,text="NAME : ",fg="crimson",bg="#fff",bd=0,font="helvetica 25 bold")
__name1_1_=Label(win,text="",fg="orange",bg="#fff",bd=0,font="helvetica 23")

__uname_1_=Label(win,text="USERNAME : ",fg="crimson",bg="#fff",bd=0,font="helvetica 25 bold")
__uname1_1_=Label(win,text="",fg="orange",bg="#fff",bd=0,font="helvetica 23")

ref_code1=Label(win,text="",bg="orange",fg="#fff",bd=0,borderwidth=1,relief=SOLID,font="helvetica 20",width=15)

def cop_():
    selp_l=[]
    selp=cur.execute("select * from cur_show;")
    for gon in selp:
        selp_l.append(gon[0])
    pyperclip.copy(str(selp_l[-1]).replace(' ',''))

copy_btn_1=Button(win,image=imdb,command=cop_,cursor="hand2",bg="orange",bd=0,activebackground="orange",borderwidth=1,relief=SOLID)

avg_gwpm_1=Label(win,text="Average\nGross WPM",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
avg_gwpm1_1=Label(win,text="0",fg="lightgreen",bg="#fff",bd=0,font="helvetica 30")

avg_acc_1=Label(win,text="Average\nAccuracy",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
avg_acc1_1=Label(win,text="0",fg="lightgreen",bg="#fff",bd=0,font="helvetica 30")

avg_nwpm_1=Label(win,text="Average\nNet WPM",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
avg_nwpm1_1=Label(win,text="0",fg="lightgreen",bg="#fff",bd=0,font="helvetica 30")

prof_image1=Label(win,bg="#fff",bd=0)

follower_1=Label(win,text="Followers",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
follower1_1=Label(win,text="0",fg="crimson",bg="#fff",bd=0,font="helvetica 20")

following1_1=Label(win,text="0",fg="crimson",bg="#fff",bd=0,font="helvetica 20")
following_1=Label(win,text="Following",fg="crimson",bg="#fff",bd=0,font="helvetica 20")

def back_n():
    back_n1()

back_button=Button(win,image=back__,bg="#fff",activebackground="#fff",bd=0,cursor="hand2",command=back_n)

def back_n2():
    back_n3()

back_button1=Button(win,image=back__,bg="#fff",activebackground="#fff",bd=0,cursor="hand2",command=back_n2)

##################################################################################################################################################################################################################################################################

frame=Frame(win,bg="#fff",bd=0,width=800,height=550)

x=Scrollbar(frame,orient=HORIZONTAL)
y=Scrollbar(frame,orient=VERTICAL)

style = ttk.Style()
style.configure("mystyle.Treeview",rowheight=30,highlightthickness=0,font=('Calibri', 20))
style.configure("mystyle.Treeview.Heading", font=('Calibri', 16,'bold'))
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

new=ttk.Treeview(frame,style="mystyle.Treeview",columns=("no","name","wpm"),height=18,xscrollcommand=x.set,yscrollcommand=y.set)
x.pack(side=BOTTOM,fill=X)
y.pack(side=RIGHT,fill=Y)
x.config(command=new.xview)
y.config(command=new.yview)
new.heading("no",text="RANK")
new.heading("name",text="USERNAME")
new.heading("wpm",text="WPM")
new['show']='headings'
new.column('no',width=100,anchor="center")
new.column('name',width=500,anchor="center")
new.column('wpm',width=100,anchor="center")
new.pack(fill=BOTH,expand=1)

def log_out():
    log_out1()

sign=PhotoImage(file=rf"{image_url}\TST_Images\exit.png")
sign_out=Button(win,image=sign,bg="#fff",activebackground="#fff",bd=0,command=log_out,cursor="hand2")

def onf(event):
    call_upon()

new.bind("<Double-1>",onf)

################################################################################################################################################################################################################

comp=PhotoImage(file=rf"{image_url}\TST_Images\monitor.png")
compu=Label(win,image=comp,bg="orange")

sent_show=Label(win,text="",bg="#4da6ff",fg="#fff",wraplength=400,bd=0,font="helvetica 25 bold",width=22,height=8)

txt1=Entry(win,bd=0,font="helvetica 30",justify=CENTER,borderwidth=2,relief=SOLID,fg="crimson",bg="#fff",width=34)
txt1.insert(END,"Type Here...")

accy=Label(win,text="Accuracy : ",fg="red",bg="#4da6ff",bd=0,font="helvetica 17 bold")

def txts(event):
    a=str(txt1.get())
    if not a:
       accy.config(text="Accuracy : 0%")
       accy.place(x=600,y=355)
       cancer1()
    else:
       txt1.delete(first=0,last=len(a))
       ls=[]
       ops=cur.execute("select * from words;")
       for it in ops:
           ls.append(it[0])
       wrd=str(ls[-1]).split(' ')
       a=a.replace("'",'')
       a=a.split(' ')
       t=0
       for iut in a:
           if iut in wrd:
              t+=1
       ac_c=t/len(wrd)
       ac_c=ac_c*100
       if '.' in str(ac_c) and int(str(ac_c)[str(ac_c).find('.')+1:str(ac_c).find('.')+3])==0:
          ac_c=str(ac_c)[:str(ac_c).find('.')]
       else:
          ac_c=str(ac_c)[:str(ac_c).find('.')+2]
       accy.config(text=f"Accuracy : {ac_c}%")
       accy.place(x=600,y=355)
       cancer1()

txt1.bind("<Return>",txts)

def txt1_(event):
    a=str(txt1.get())
    if a=="Type Here...":
       txt1.delete(first=0,last=len("Type Here..."))

txt1.bind("<FocusIn>",txt1_)

def _txt1_(event):
    a=str(txt1.get())
    if not a:
       txt1.insert(END,"Type Here...")

txt1.bind("<FocusOut>",_txt1_)

################################################################################################################################################################################################################

def follow_kar():
    folwer=str(loguser[-1])
    foling=str(logpass[-1])
    use=[]
    pas=[]
    sel=cur.execute(f"select * from fol;")
    for it in sel:
        use.append(it[0])
        pas.append(it[1])
    a=use[-1]
    b=pas[-1]
    cur.execute(f"insert into {a}{b}followers values('{loguser[-1]}');")
    cur.execute(f"insert into {loguser[-1]}{logpass[-1]}following values('{a}');")
    follow_btn.place(x=-1500,y=0)
    unfollow_btn.place(x=380,y=360)
    con.commit()
    
follow_btn=Button(win,command=follow_kar,text="Follow",fg="#fff",bg="crimson",bd=0,font="helvetica 18",activebackground="#fff",activeforeground="crimson",width=10,cursor="hand2")

def unfollow_kar():
    folwer=str(loguser[-1])
    foling=str(logpass[-1])
    use=[]
    pas=[]
    sel=cur.execute(f"select * from fol;")
    for it in sel:
        use.append(it[0])
        pas.append(it[1])
    a=use[-1]
    b=pas[-1]
    cur.execute(f"delete from {a}{b}followers where username='{loguser[-1]}';")
    cur.execute(f"delete from {loguser[-1]}{logpass[-1]}following where username='{a}';")
    con.commit()
    unfollow_btn.place(x=-1500,y=0)
    follow_btn.place(x=380,y=360)

unfollow_btn=Button(win,command=unfollow_kar,text="Unfollow",fg="#fff",bg="crimson",bd=0,font="helvetica 18",activebackground="#fff",activeforeground="crimson",width=10,cursor="hand2")

################################################################################################################################################################################################################

def start2():
    sel=cur.execute("select * from login;")
    for i in sel:
        i=i
    #reg
    logo.place(x=-1500,y=0)
    logo1.place(x=-1500,y=0)
    start.place(x=-1500,y=0)
    #reg1
    if str(i[0])=='no':
       lbl1.place(x=380,y=150)
       login_lbl.place(x=465,y=180)
       uname.place(x=400,y=270)
       if yes_no[-1]=='yes':
          show_btn.place(x=648,y=352)
       else:
          blind_btn.place(x=648,y=352)
       pwd.place(x=400,y=350)
       log_btn.place(x=450,y=450)
       #reg
       lbl2.place(x=702,y=150)
       register_lbl.place(x=787,y=180)
       name_.place(x=722,y=270)
       uname_.place(x=722,y=330)
       if yes_no1[-1]=='yes':
          show1_btn.place(x=970,y=390)
       else:
          blind1_btn.place(x=970,y=390)
       pwd_.place(x=722,y=390)
       reg_btn.place(x=772,y=470)
    else:
       head.place(x=-1500,y=0)
       head1.place(x=0,y=0)
       sent_win.place(x=300,y=170)
       txt.place(x=299,y=450)
       clock.place(x=630,y=80)
       nav_btn.place(x=5,y=0)
       reset_btn.place(x=620,y=550)
       sign_out.place(x=1320,y=3)
       sentence()

def register1():
    a=str(name_.get())
    b=str(uname_.get())
    c=str(pwd_.get())
    users=[]
    pases=[]
    select=cur.execute("select * from details;")
    for t in select:
        users.append(t[1])
        pases.append(t[2])
    if a=="           Enter Name" or not a:
       messagebox.showerror("Typing Ritual","Please Enter Your Name!")
    elif len(a)>50 and (a!="           Enter Name" or len(a)!=0):
       messagebox.showerror("Typing Ritual","Name Limit Exceeded!")
    elif b=="        Enter Username" or not b:
       messagebox.showerror("Typing Ritual","Please Enter The Username!")
    elif len(b)<4 and (b!="        Enter Password" or len(b)!=0):
       messagebox.showerror("Typing Ritual","Username is Too Short!")
    elif b.replace('_','').isalnum()!=True:
       messagebox.showerror("Typing Ritual","Special Characters Except Underscores are not allowed!")
    elif len(b)>10 and (b!="        Enter Username" or len(b)!=0):
       messagebox.showerror("Typing Ritual","Username cannot be more than 10 Characters!")
    elif b in users:
       messagebox.showerror("Typing Ritual","Username Is Already used by Other User!")
    elif c=="        Enter Password" or not c:
       messagebox.showerror("Typing Ritual","Please Enter The Password!")
    elif len(c)>10 and (c!="        Enter Password" or len(c)!=0):
       messagebox.showerror("Typing Ritual","Password cannot be more than 10 Characters!")
    elif c.replace('_','').isalnum()!=True:
       messagebox.showerror("Typing Ritual","Special Characters Except Underscores are not allowed!")
    elif len(c)<8 and (c!="        Enter Password" or len(c)!=0):
       messagebox.showerror("Typing Ritual","Password is Too Short!")
    else:
       s=str(datetime.datetime.now())
       cur.execute(f"insert into details values('{a}','{b}','{c}');")
       code=str(random.sample('qwertyuiop67890ASDFGHJKL7890zxcvbnm1890QWERTYUIOP1290asdfghjkl1234567890ZXCVBNM',12)).replace(',','').replace('[','').replace(']','').replace("'",'').replace(' ','')
       cur.execute(f"create table {b}{c}code('_code_');")
       cur.execute(f"insert into {b}{c}code values('{code}');")
       cur.execute(f"create table {b}{c}photo('url' varchar(10));")
       cur.execute(f"insert into {b}{c}photo values('user');")
       cur.execute(f"create table {b}{c}scores('gross wpm' int,'net wpm' int,'accuracy' float,'date' varchar(10),'time' varchar(10));")
       cur.execute(f"create table {b}{c}followers('username' varchar(10));")
       cur.execute(f"create table {b}{c}following('username' varchar(10));")
       con.commit()
       messagebox.showinfo("Typing Ritual","Account Registered,\nNow Head To Login...")
       name_.delete(first=0,last=len(a))
       uname_.delete(first=0,last=len(b))
       pwd_.delete(first=0,last=len(c))
       name_.insert(END,'           Enter Name')
       uname_.insert(END,'        Enter Username')
       pwd_.insert(END,'        Enter Password')
       pwd_.config(show="")

def login1():
    b=str(uname.get())
    c=str(pwd.get())
    users=[]
    pases=[]
    select=cur.execute("select * from details;")
    for t in select:
        users.append(t[1])
        pases.append(t[2])
    if b=="        Enter Username" or not b:
       messagebox.showerror("Typing Ritual","Please Enter The Username!")
    elif b not in users and (b!="        Enter Password" or len(b)!=0):
       messagebox.showerror("Typing Ritual","Invalid Username!")
    elif c=="        Enter Password" or not c:
       messagebox.showerror("Typing Ritual","Please Enter The Password!")
    elif b in users and c!=pases[users.index(b)] and (b!="        Enter Password" or len(b)!=0):
       messagebox.showerror("Typing Ritual","Incorrect Password!")
    else:
       cur.execute("insert into login values('yes');")
       cur.execute(f"insert into current_login values('{b}','{c}');")
       con.commit()
       ool=cur.execute(f"select * from {b}{c}photo;")
       loguser.append(f"{b}")
       logpass.append(f"{c}")
       for ij in ool:
           photo_l.append(ij[0])
       universal.append(photo_l[-1])
       messagebox.showinfo("Typing Ritual","Login Successfull...")
       profile.config(image=uni[str(universal[-1])])
       select_=cur.execute(f"select * from details where username='{loguser[-1]}';")
       for tu in select_:
           nam_e=tu[0]
           use_r=tu[1]
       __name1__.config(state=NORMAL)
       __uname1__.config(state=NORMAL)
       __name1__.delete(first=0,last=len(__name1__.get()))
       __uname1__.delete(first=0,last=len(__uname1__.get()))
       __name1__.insert(END,f' {nam_e}')
       __uname1__.insert(END,f' {use_r}')
       __name1__.config(state=DISABLED)
       __uname1__.config(state=DISABLED)
       sele_=cur.execute(f"select * from {b}{c}code;")
       for hugh in sele_:
           ref_code.config(text=hugh)
           copi.append(hugh)
       gayab()

def gayab2():
    gayab1()
    
def gayab():
    lbl1.place(x=-1500,y=150)
    login_lbl.place(x=-1500,y=180)
    uname.place(x=-1500,y=270)
    show_btn.place(x=-1500,y=352)
    blind_btn.place(x=-1500,y=352)
    pwd.place(x=-1500,y=350)
    log_btn.place(x=-1500,y=450)
    #reg
    lbl2.place(x=-1500,y=150)
    register_lbl.place(x=-1500,y=180)
    name_.place(x=-1500,y=270)
    uname_.place(x=-1500,y=330)
    show1_btn.place(x=-1500,y=390)
    blind1_btn.place(x=-1500,y=390)
    pwd_.place(x=-1500,y=390)
    reg_btn.place(x=-1500,y=470)
    win.after(500,gayab2)

def gayab1():
    head1.config(text="Typing Ritual")
    compu.place(x=-1500,y=50)
    sent_show.place(x=-1500,y=110)
    txt1.place(x=-1500,y=590)
    frame.place(x=-1500,y=90)
    search_bar.place(x=-1500,y=100)
    search_list.place(x=-1500,y=0)
    nav_btn.place(x=5,y=0)
    #reg
    head.place(x=-1500,y=0)
    head1.place(x=0,y=0)
    sent_win.place(x=300,y=170)
    txt.place(x=299,y=450)
    clock.place(x=630,y=80)
    nav_btn.place(x=5,y=0)
    sign_out.place(x=1320,y=3)
    reset_btn.place(x=620,y=550)
    side_nav.place(x=-1500,y=-2)
    line.place(x=-1500,y=-1)
    home_btn.place(x=-1500,y=131)
    quick_btn.place(x=-1500,y=201)
    rank_btn.place(x=-1500,y=271)
    fre_btn.place(x=-1500,y=0)
    sin_out_btn.place(x=-1500,y=0)
    re_nav_btn.place(x=-1500,y=0)
    profile.place(x=-1500,y=50)
    sentence()

def sentence():
    l_list=[]
    file=open(rf"{image_url}\sentences.txt",'r')
    for i in file:
        l_list.append(str(i).strip())
    choosed_sentence=random.choice(l_list)
    globel=choosed_sentence.split(' ')
    for ghl in globel:
        globe.append(ghl)
    sent_win.config(text=choosed_sentence)

def navigation():
    side_nav.place(x=-2,y=-2)
    line.place(x=-1,y=-1)
    home_btn.place(x=-2,y=131)
    quick_btn.place(x=-2,y=201)
    rank_btn.place(x=-2,y=271)
    fre_btn.place(x=-2,y=341)
    sin_out_btn.place(x=-2,y=411)
    re_nav_btn.place(x=190,y=-5)
    profile.place(x=10,y=50)

def renavigation():
    side_nav.place(x=-1500,y=-2)
    line.place(x=-1500,y=-1)
    home_btn.place(x=-1500,y=131)
    quick_btn.place(x=-1500,y=201)
    rank_btn.place(x=-1500,y=271)
    fre_btn.place(x=-1500,y=0)
    sin_out_btn.place(x=-1500,y=0)
    re_nav_btn.place(x=-1500,y=0)
    profile.place(x=-1500,y=50)

def result(a):
    sent_win.place(x=-1500,y=170)
    txt.place(x=-1500,y=450)
    clock.place(x=-1500,y=80)
    nav_btn.place(x=-1500,y=0)
    side_nav.place(x=-1500,y=-2)
    line.place(x=-1500,y=-1)
    home_btn.place(x=-1500,y=131)
    quick_btn.place(x=-1500,y=201)
    rank_btn.place(x=-1500,y=271)
    fre_btn.place(x=-1500,y=0)
    sin_out_btn.place(x=-1500,y=411)
    re_nav_btn.place(x=-1500,y=0)
    profile.place(x=-1500,y=50)
    reset_btn.place(x=635,y=550)
    sign_out.place(x=-1500,y=3)
    result_cal(a)

def result_cal(a):
    head1.config(text="RESULT")
    result_patch.place(x=320,y=100)
    gwpm.place(x=375,y=350)
    gwpm1.place(x=430,y=200)
    Acc.place(x=645,y=350)
    Acc1.place(x=640,y=200)
    net_wpm.place(x=885,y=350)
    net_wpm1.place(x=910,y=200)
    back_btn.place(x=5,y=3)
    #reg
    list1=a.split(' ')
    input_len=len(a)
    if input_len==0:
       gross_wpm=0
       net_WPM=0
       Accuracy=0.0
       s=str(datetime.datetime.now())
       cur.execute(f"insert into {loguser[-1]}{logpass[-1]}scores values({gross_wpm},{net_WPM},{Accuracy},'{s[8:10]}-{s[5:7]}-{s[0:4]}','{s[11:19]}');")
       con.commit()
    if input_len!=0:
       wrd_count=len(list1)
       gfh=[]
       globe_len=len(globe)
       if globe_len<wrd_count:
          for jgh in range(0,globe_len):
              gfh.append(globe[jgh])
       else:
          for jgh in range(0,wrd_count):
              gfh.append(globe[jgh])
       mistakes=0
       for blg in list1:
           if blg not in gfh:
              mistakes+=1
       gross_wpm=int(input_len/5)
       net_WPM=int(gross_wpm-mistakes)
       Accuracy=(net_WPM/gross_wpm)*100
       Accuracy=str(Accuracy)[:str(Accuracy).find('.')+2]
       s=str(datetime.datetime.now())
       if (not loguser)==False and (not logpass)==False:
          cur.execute(f"insert into {loguser[-1]}{logpass[-1]}scores values({gross_wpm},{net_WPM},{Accuracy},'{s[8:10]}-{s[5:7]}-{s[0:4]}','{s[11:19]}');")
          con.commit()
       if Accuracy[-1]=='0':
          Accuracy=int(float(Accuracy))
       if len(str(gross_wpm))==2:
          gwpm1.config(text=f"{gross_wpm}")
       else:
          gwpm1.config(text=f"{gross_wpm}")
          gwpm1.place(x=460,y=200)
       if gross_wpm<50:
          gwpm1.config(fg="red")
       else:
          gwpm1.config(fg="lightgreen")
       if len(str(Accuracy))==4:
          Acc1.config(text=f"{Accuracy}%",font="helvetica 60")
          Acc1.place(x=640,y=220)
       elif len(str(Accuracy))==3:
          Acc1.place(x=630,y=220)
          Acc1.config(text=f"{Accuracy}%")
       elif len(str(Accuracy))==2:
          Acc1.place(x=630,y=220)
          Acc1.config(text=f"{Accuracy}%")
       else:
          Acc1.config(text=f"{Accuracy}%")
          Acc1.place(x=710,y=200)
       if float(Accuracy)<50:
          Acc1.config(fg="red")
       else:
          Acc1.config(fg="lightgreen")
       if len(str(net_WPM))==2:
          net_wpm1.config(text=f"{net_WPM}")
       else:
          net_wpm1.config(text=f"{net_WPM}")
          net_wpm1.place(x=940,y=200)
       if net_WPM<50:
          net_wpm1.config(fg="red")
       else:
          net_wpm1.config(fg="lightgreen")
    else:
       gwpm1.config(text="0",fg="red")
       gwpm1.place(x=460,y=200)
       Acc1.config(text="0%",fg="red",font="helvetica 80")
       Acc1.place(x=680,y=200)
       net_wpm1.config(text="0",fg="red")

def null1234():
    head1.config(text="Typing Ritual")
    result_patch.place(x=-1500,y=100)
    gwpm.place(x=-1500,y=350)
    gwpm1.place(x=-1500,y=200)
    Acc.place(x=-1500,y=350)
    Acc1.place(x=-1500,y=200)
    net_wpm.place(x=-1500,y=350)
    net_wpm1.place(x=-1500,y=200)
    back_btn.place(x=-1500,y=0)
    #reg
    sent_win.place(x=300,y=170)
    txt.place(x=299,y=450)
    clock.place(x=630,y=80)
    nav_btn.place(x=5,y=0)
    sign_out.place(x=1320,y=3)

def _back1_():
    head1.config(text="Typing Ritual")
    result_patch.place(x=-1500,y=100)
    gwpm.place(x=-1500,y=350)
    gwpm1.place(x=-1500,y=200)
    Acc.place(x=-1500,y=350)
    Acc1.place(x=-1500,y=200)
    net_wpm.place(x=-1500,y=350)
    net_wpm1.place(x=-1500,y=200)
    back_btn.place(x=-1500,y=0)
    #reg
    sent_win.place(x=300,y=170)
    txt.place(x=299,y=450)
    sign_out.place(x=1320,y=3)
    clock.place(x=630,y=80)
    nav_btn.place(x=5,y=0)

def profil1():
    head1.config(text="PROFILE")
    frame.place(x=-1500,y=90)
    compu.place(x=-1500,y=50)
    sent_show.place(x=-1500,y=110)
    txt1.place(x=-1500,y=590)
    sent_win.place(x=-1500,y=170)
    txt.place(x=-1500,y=450)
    clock.place(x=-1500,y=80)
    nav_btn.place(x=-1500,y=0)
    sign_out.place(x=-1500,y=3)
    side_nav.place(x=-1500,y=-2)
    line.place(x=-1500,y=-1)
    home_btn.place(x=-1500,y=131)
    quick_btn.place(x=-1500,y=201)
    rank_btn.place(x=-1500,y=271)
    fre_btn.place(x=-1500,y=0)
    sin_out_btn.place(x=-1500,y=411)
    re_nav_btn.place(x=-1500,y=0)
    profile.place(x=-1500,y=50)
    reset_btn.place(x=-1500,y=550)
    search_bar.place(x=0-1500,y=100)
    search_list.place(x=-1500,y=0)
    nav_btn.place(x=-1500,y=0)
    #reg
    white.place(x=300,y=100)
    __name__.place(x=600,y=150)
    __name1__.place(x=750,y=153)
    edit1.place(x=1030,y=153)
    __uname__.place(x=600,y=220)
    __uname1__.place(x=822,y=223)
    edit2.place(x=1030,y=223)
    ref_code.place(x=600,y=320)
    copy_btn.place(x=850,y=320)
    prof_image.config(image=uni1[universal[-1]])
    prof_image.place(x=380,y=130)
    back_btn1.place(x=5,y=3)
    follower.place(x=320,y=320)
    following.place(x=450,y=320)
    follower1.place(x=370,y=285)
    following1.place(x=500,y=285)
    avg_gwpm.place(x=450,y=480)
    avg_acc.place(x=670,y=480)
    avg_nwpm.place(x=850,y=480)
    avg_gwpm1.place(x=510,y=430)
    avg_acc1.place(x=720,y=430)
    avg_nwpm1.place(x=890,y=430)
    averager()
    try:
       cur.execute(f"insert into tmp values('{nam_e}','{use_r}');")
       con.commit()
    except:
        pass
    tmpu=nam_e[-1]
    tmpp=use_r[-1]

def get_back1():
    head1.config(text="Typing Ritual")
    sent_win.place(x=300,y=170)
    txt.place(x=299,y=450)
    clock.place(x=630,y=80)
    nav_btn.place(x=5,y=0)
    reset_btn.place(x=620,y=550)
    sign_out.place(x=1320,y=3)
    #reg
    white.place(x=-1500,y=100)
    __name__.place(x=-1500,y=150)
    __name1__.place(x=-1500,y=153)
    edit1.place(x=-1500,y=153)
    __uname__.place(x=-1500,y=220)
    __uname1__.place(x=-1500,y=223)
    edit2.place(x=-1500,y=223)
    ref_code.place(x=-1500,y=300)
    copy_btn.place(x=-1500,y=300)
    prof_image.place(x=-1500,y=150)
    back_btn1.place(x=-1500,y=3)
    edit_btn.place(x=-1500,y=249)
    follower.place(x=-1500,y=320)
    following.place(x=-1500,y=320)
    follower1.place(x=-1500,y=285)
    following1.place(x=-1500,y=285)
    avg_gwpm.place(x=-1500,y=480)
    avg_acc.place(x=-1500,y=480)
    avg_nwpm.place(x=-1500,y=480)
    avg_gwpm1.place(x=-1500,y=430)
    avg_acc1.place(x=-1500,y=430)
    avg_nwpm1.place(x=-1500,y=430)

def pic1():
    head1.config(text="PROFILE PICTURE")
    __name1__.delete(first=0,last=len(str(__name1__.get())))
    __name1__.insert(END,tmpu)
    __name1__.config(state=DISABLED,borderwidth=0)
    __uname1__.delete(first=0,last=len(__uname1__.get()))
    __uname1__.insert(END,tmpp)
    __uname1__.config(state=DISABLED,borderwidth=0)
    white.place(x=-1500,y=100)
    __name__.place(x=-1500,y=150)
    __name1__.place(x=-1500,y=153)
    edit1.place(x=-1500,y=153)
    __uname__.place(x=-1500,y=220)
    __uname1__.place(x=-1500,y=223)
    edit2.place(x=-1500,y=223)
    ref_code.place(x=-1500,y=300)
    copy_btn.place(x=-1500,y=300)
    prof_image.place(x=-1500,y=150)
    back_btn1.place(x=-1500,y=3)
    edit_btn.place(x=-1500,y=249)
    follower.place(x=-1500,y=320)
    following.place(x=-1500,y=320)
    follower1.place(x=-1500,y=285)
    following1.place(x=-1500,y=285)
    avg_gwpm.place(x=-1500,y=480)
    avg_acc.place(x=-1500,y=480)
    avg_nwpm.place(x=-1500,y=480)
    avg_gwpm1.place(x=-1500,y=430)
    avg_acc1.place(x=-1500,y=430)
    avg_nwpm1.place(x=-1500,y=430)
    #reg
    white1.place(x=300,y=100)
    beard_img.place(x=340,y=150)
    boy_img.place(x=540,y=150)
    donuts_img.place(x=740,y=150)
    girl_img.place(x=940,y=150)
    happy_img.place(x=340,y=350)
    happy1_img.place(x=540,y=350)
    ice_cream_img.place(x=740,y=350)
    man_img.place(x=940,y=350)
    nxt_btn.place(x=1050,y=530)
    cancel_btn.place(x=320,y=530)

def nxt1_():
    beard_img.place(x=-1500,y=150)
    boy_img.place(x=-1500,y=150)
    donuts_img.place(x=-1500,y=150)
    girl_img.place(x=-1500,y=150)
    happy_img.place(x=-1500,y=350)
    happy1_img.place(x=-1500,y=350)
    ice_cream_img.place(x=-1500,y=350)
    man_img.place(x=-1500,y=350)
    nxt_btn.place(x=-1500,y=530)
    #reg
    prev_btn.place(x=320,y=530)
    men_img.place(x=340,y=150)
    sweet_img.place(x=540,y=150)
    umbrella_img.place(x=740,y=150)
    user_img.place(x=940,y=150)
    user1_img.place(x=340,y=350)
    user2_img.place(x=540,y=350)
    user3_img.place(x=740,y=350)
    user4_img.place(x=940,y=350)
    nxt_btn.place(x=-1500,y=530)
    cancel_btn.place(x=1000,y=530)

def pre1_():
    beard_img.place(x=340,y=150)
    boy_img.place(x=540,y=150)
    donuts_img.place(x=740,y=150)
    girl_img.place(x=940,y=150)
    happy_img.place(x=340,y=350)
    happy1_img.place(x=540,y=350)
    ice_cream_img.place(x=740,y=350)
    man_img.place(x=940,y=350)
    nxt_btn.place(x=1050,y=530)
    cancel_btn.place(x=320,y=530)
    #reg
    prev_btn.place(x=-1500,y=530)
    men_img.place(x=-1500,y=150)
    sweet_img.place(x=-1500,y=150)
    umbrella_img.place(x=-1500,y=150)
    user_img.place(x=-1500,y=150)
    user1_img.place(x=-1500,y=350)
    user2_img.place(x=-1500,y=350)
    user3_img.place(x=-1500,y=350)
    user4_img.place(x=-1500,y=350)

def cancel_():
    head1.config(text="PROFILE")
    prev_btn.place(x=-1500,y=530)
    men_img.place(x=-1500,y=150)
    sweet_img.place(x=-1500,y=150)
    umbrella_img.place(x=-1500,y=150)
    user_img.place(x=-1500,y=150)
    user1_img.place(x=-1500,y=350)
    user2_img.place(x=-1500,y=350)
    user3_img.place(x=-1500,y=350)
    user4_img.place(x=-1500,y=350)
    beard_img.place(x=-1500,y=150)
    boy_img.place(x=-1500,y=150)
    donuts_img.place(x=-1500,y=150)
    girl_img.place(x=-1500,y=150)
    happy_img.place(x=-1500,y=350)
    happy1_img.place(x=-1500,y=350)
    ice_cream_img.place(x=-1500,y=350)
    man_img.place(x=-1500,y=350)
    nxt_btn.place(x=-1500,y=530)
    white1.place(x=-1500,y=0)
    cancel_btn.place(x=-1500,y=0)
    #reg
    white.place(x=300,y=100)
    __name__.place(x=600,y=150)
    __name1__.place(x=750,y=153)
    edit1.place(x=1030,y=153)
    __uname__.place(x=600,y=220)
    __uname1__.place(x=822,y=223)
    edit2.place(x=1030,y=223)
    ref_code.place(x=600,y=320)
    copy_btn.place(x=850,y=320)
    prof_image.config(image=uni1[universal[-1]])
    prof_image.place(x=380,y=130)
    back_btn1.place(x=5,y=3)
    follower.place(x=320,y=320)
    following.place(x=450,y=320)
    follower1.place(x=370,y=285)
    following1.place(x=500,y=285)
    avg_gwpm.place(x=450,y=480)
    avg_acc.place(x=670,y=480)
    avg_nwpm.place(x=850,y=480)
    avg_gwpm1.place(x=510,y=430)
    avg_acc1.place(x=720,y=430)
    avg_nwpm1.place(x=890,y=430)
    averager()

def fre1_():
    compu.place(x=-1500,y=50)
    sent_show.place(x=-1500,y=110)
    txt1.place(x=-1500,y=590)
    sign_out.place(x=-1500,y=3)
    sent_win.place(x=-1500,y=170)
    txt.place(x=-1500,y=450)
    clock.place(x=-1500,y=80)
    nav_btn.place(x=-1500,y=0)
    side_nav.place(x=-1500,y=-2)
    line.place(x=-1500,y=-1)
    home_btn.place(x=-1500,y=131)
    quick_btn.place(x=-1500,y=201)
    rank_btn.place(x=-1500,y=271)
    fre_btn.place(x=-1500,y=0)
    sin_out_btn.place(x=-1500,y=411)
    re_nav_btn.place(x=-1500,y=0)
    profile.place(x=-1500,y=50)
    reset_btn.place(x=-1500,y=550)
    #reg
    head1.config(text="Typing Ritual")
    search_bar.place(x=400,y=100)
    search_list.place(x=-1500,y=0)
    nav_btn.place(x=5,y=0)
    #reg1
    frame.place(x=-1500,y=90)

def averager():
    for ct in cur.execute(f"select count(*) from {loguser[-1]}{logpass[-1]}followers;"):
        count=int(ct[0])
    for ct1 in cur.execute(f"select count(*) from {loguser[-1]}{logpass[-1]}following;"):
        count1=int(ct1[0])
    follower1.config(text=f"{count}")
    following1.config(text=f"{count1}")
    for ytu in cur.execute(f"select count(*) from {loguser[-1]}{logpass[-1]}scores;"):
        counter=int(ytu[0])
    if counter==0:
       avg_gwpm1.config(text="0")
       avg_acc1.config(text="0")
       avg_nwpm1.config(text="0")
    else:
       gwpm_list=[]
       nwpm_list=[]
       acc_list=[]
       swl=cur.execute(f"select * from {loguser[-1]}{logpass[-1]}scores;")
       for ooty in swl:
           gwpm_list.append(int(ooty[0]))
           nwpm_list.append(int(ooty[1]))
           acc_list.append(float(ooty[2]))
       gwpm_avg=int(int(sum(gwpm_list))/counter)
       avg_gwpm1.config(text=f"{gwpm_avg}")
       nwpm_avg=int(int(sum(nwpm_list))/counter)
       avg_nwpm1.config(text=f"{nwpm_avg}")
       acc_avg=str(sum(acc_list)/counter)
       acc_avg=acc_avg[:acc_avg.find('.')+2]
       avg_acc1.config(text=f"{acc_avg}%")
       if len(str(acc_avg))==4 or len(str(acc_avg))==3 or len(str(acc_avg))==2:
          avg_acc1.place(x=680,y=430)
       elif len(str(acc_avg))==5:
          avg_acc1.place(x=680,y=430)
          avg_acc1.config(text=f"{str(acc_avg)[:3]}%")

def cyum1():
    a=search_list.curselection()
    if (not a)==False:
        a=str(search_list.get(a[0]))
        a=a.strip()
        search_bar.place(x=-1500,y=100)
        search_list.place(x=-1500,y=0)
        nav_btn.place(x=-1500,y=0)
        search_bar.delete(first=0,last=len(search_bar.get()))
        search_bar.insert(END,"Search Here...")
        for gijoe in range(0,search_list.size()):
            search_list.delete(gijoe)
        psel=cur.execute(f"select * from details where username='{a}';")
        for git in psel:
            na_me=git[0]
            pa_ss=git[2]
        psel1=cur.execute(f"select * from {a}{pa_ss}code;")
        for git1 in psel1:
            co_de=git1[0]
            break
        psel2=cur.execute(f"select * from {a}{pa_ss}photo;")
        for git2 in psel2:
            phoho=git2[0]
        phoho=phoho
        white2.place(x=300,y=100)
        __name_1_.place(x=600,y=150)
        __name1_1_.place(x=750,y=153)
        __name1_1_.config(text=f"{na_me[:20]}")
        __uname_1_.place(x=600,y=220)
        __uname1_1_.place(x=822,y=223)
        __uname1_1_.config(text=f"{a}")
        ref_code1.place(x=600,y=320)
        ref_code1.config(text=f"{co_de}")
        copy_btn_1.place(x=850,y=320)
        avg_gwpm_1.place(x=450,y=480)
        avg_acc_1.place(x=670,y=480)
        avg_nwpm_1.place(x=850,y=480)
        avg_gwpm1_1.place(x=510,y=430)
        avg_acc1_1.place(x=720,y=430)
        avg_nwpm1_1.place(x=890,y=430)
        follower_1.place(x=320,y=320)
        following_1.place(x=450,y=320)
        follower1_1.place(x=370,y=285)
        following1_1.place(x=500,y=285)
        prof_image1.config(image=uni1[phoho])
        prof_image1.place(x=380,y=130)
        back_button.place(x=5,y=3)
        cur.execute(f"insert into cur_show values('{co_de}');")
        con.commit()
        side_nav.place(x=-1500,y=-2)
        line.place(x=-1500,y=-1)
        home_btn.place(x=-1500,y=131)
        quick_btn.place(x=-1500,y=201)
        rank_btn.place(x=-1500,y=271)
        fre_btn.place(x=-1500,y=0)
        sin_out_btn.place(x=-1500,y=0)
        re_nav_btn.place(x=-1500,y=0)
        profile.place(x=-1500,y=50)
        averager1(a,pa_ss)

def averager1(a,b):
    if loguser[-1]!=a:
       sell=cur.execute(f"select * from {a}{b}followers;")
       fwer=[]
       for kt in sell:  
           fwer.append(kt[0])
       if loguser[-1] in fwer:
          unfollow_btn.place(x=380,y=360)
       else:
          follow_btn.place(x=380,y=360)
    cur.execute(f"insert into fol values('{a}','{b}');")
    con.commit()
    for ct in cur.execute(f"select count(*) from {a}{b}followers;"):
        count=int(ct[0])
    for ct1 in cur.execute(f"select count(*) from {a}{b}following;"):
        count1=int(ct1[0])
    follower1_1.config(text=f"{count}")
    following1_1.config(text=f"{count1}")
    for ytu in cur.execute(f"select count(*) from {a}{b}scores;"):
        counter=int(ytu[0])
    if counter==0:
       avg_gwpm1_1.config(text="0")
       avg_acc1_1.config(text="0")
       avg_nwpm1_1.config(text="0")
    else:
       gwpm_list=[]
       nwpm_list=[]
       acc_list=[]
       swl=cur.execute(f"select * from {a}{b}scores;")
       for ooty in swl:
           gwpm_list.append(int(ooty[0]))
           nwpm_list.append(int(ooty[1]))
           acc_list.append(float(ooty[2]))
       gwpm_avg=int(int(sum(gwpm_list))/counter)
       avg_gwpm1_1.config(text=f"{gwpm_avg}")
       nwpm_avg=int(int(sum(nwpm_list))/counter)
       avg_nwpm1_1.config(text=f"{nwpm_avg}")
       acc_avg=str(sum(acc_list)/counter)
       acc_avg=acc_avg[:acc_avg.find('.')+2]
       avg_acc1_1.config(text=f"{acc_avg}%")
       if len(str(acc_avg))==4 or len(str(acc_avg))==3 or len(str(acc_avg))==2:
          avg_acc1_1.place(x=680,y=430)
       elif len(str(acc_avg))==5:
          avg_acc1_1.place(x=680,y=430)
          avg_acc1_1.config(text=f"{str(acc_avg)[:3]}%")

def back_n1():
    white2.place(x=-1500,y=100)
    __name_1_.place(x=-1500,y=150)
    __name1_1_.place(x=-1500,y=153)
    __uname_1_.place(x=-1500,y=220)
    __uname1_1_.place(x=-1500,y=223)
    ref_code1.place(x=-1500,y=320)
    copy_btn_1.place(x=-1500,y=320)
    avg_gwpm_1.place(x=-1500,y=480)
    avg_acc_1.place(x=-1500,y=480)
    avg_nwpm_1.place(x=-1500,y=480)
    avg_gwpm1_1.place(x=-1500,y=430)
    avg_acc1_1.place(x=-1500,y=430)
    avg_nwpm1_1.place(x=-1500,y=430)
    follower_1.place(x=-1500,y=320)
    following_1.place(x=-1500,y=320)
    follower1_1.place(x=-1500,y=285)
    following1_1.place(x=-1500,y=285)
    unfollow_btn.place(x=-1500,y=360)
    follow_btn.place(x=-1500,y=360)
    prof_image1.place(x=-1500,y=130)
    back_button.place(x=-1500,y=3)
    #reg
    search_bar.place(x=400,y=100)
    search_list.place(x=-1500,y=0)
    nav_btn.place(x=5,y=0)

def ranks():
    compu.place(x=-1500,y=50)
    sent_show.place(x=-1500,y=110)
    txt1.place(x=-1500,y=590)
    search_bar.place(x=-1500,y=100)
    search_list.place(x=-1500,y=0)
    nav_btn.place(x=5,y=0)
    sign_out.place(x=-1500,y=3)
    #reg
    sent_win.place(x=-1500,y=170)
    txt.place(x=-1500,y=450)
    clock.place(x=-1500,y=80)
    side_nav.place(x=-1500,y=-2)
    line.place(x=-1500,y=-1)
    home_btn.place(x=-1500,y=131)
    quick_btn.place(x=-1500,y=201)
    rank_btn.place(x=-1500,y=271)
    fre_btn.place(x=-1500,y=0)
    sin_out_btn.place(x=-1500,y=411)
    re_nav_btn.place(x=-1500,y=0)
    profile.place(x=-1500,y=50)
    reset_btn.place(x=-1500,y=550)
    head1.config(text="ScoreBoard")
    #reg1
    frame.place(x=350,y=90)
    nil=new.get_children()
    for row in nil:
        new.delete(row)
    score={}
    us=[]
    pa=[]
    sele=cur.execute("select * from details;")
    for ids in sele:
        us.append(ids[1])
        pa.append(ids[2])
    max_nums=[]
    for i in range(0,len(us)):
        maxes=[]
        sew=cur.execute(f"select * from {us[i]}{pa[i]}scores;")
        for uj in sew:
            maxes.append(int(uj[0]))
        if not maxes:
           max_nums.append(0)
        else:
           max_nums.append(max(maxes))    
    for ius in range(0,len(us)):
        score[max_nums[ius]]=us[ius]
    score_={}
    for k,v in sorted(score.items(),reverse=True):
        if k!=0:
           score_[k]=v
    d=1
    for data in score_:
        new.insert('',END,values=f'{d}  {score_[data]}   {data}')
        d+=1

def log_out1():
    if messagebox.askyesno("Typing Ritual","Do you want to Sign Out?"):
       yes_no.append('yes')
       show_btn.place(x=-1500,y=352)
       blind_btn.place(x=648,y=352)
       pwd.config(show="")
       yes_no1.append('yes')
       show1_btn.place(x=-1500,y=352)
       blind1_btn.place(x=970,y=390)
       pwd_.config(show="")
       uname.delete(first=0,last=len(uname.get()))
       pwd.delete(first=0,last=len(pwd.get()))
       name_.delete(first=0,last=len(name_.get()))
       uname_.delete(first=0,last=len(uname_.get()))
       pwd_.delete(first=0,last=len(pwd_.get()))
       uname.insert(END,"        Enter Username")
       pwd.insert(END,"        Enter Password")
       name_.insert(END,"           Enter Name")
       uname_.insert(END,"        Enter Username")
       pwd_.insert(END,"        Enter Password")
       cur.execute("insert into login values('no');")
       con.commit()
       search_bar.place(x=-1500,y=100)
       search_list.place(x=-1500,y=0)
       nav_btn.place(x=-1500,y=0)
       sign_out.place(x=-1500,y=3)
       frame.place(x=-1500,y=0)
       head1.place(x=-1500,y=0)
       head.place(x=0,y=0)
       #reg
       compu.place(x=-1500,y=50)
       sent_show.place(x=-1500,y=110)
       txt1.place(x=-1500,y=590)
       #reg2
       sent_win.place(x=-1500,y=170)
       txt.place(x=-1500,y=450)
       clock.place(x=-1500,y=80)
       side_nav.place(x=-1500,y=-2)
       line.place(x=-1500,y=-1)
       home_btn.place(x=-1500,y=131)
       quick_btn.place(x=-1500,y=201)
       rank_btn.place(x=-1500,y=271)
       fre_btn.place(x=-1500,y=0)
       sin_out_btn.place(x=-1500,y=411)
       re_nav_btn.place(x=-1500,y=0)
       profile.place(x=-1500,y=50)
       reset_btn.place(x=-1500,y=550)
       #reg1
       lbl1.place(x=380,y=150)
       login_lbl.place(x=465,y=180)
       uname.place(x=400,y=270)
       if yes_no[-1]=='yes':
          show_btn.place(x=648,y=352)
       else:
          blind_btn.place(x=648,y=352)
       pwd.place(x=400,y=350)
       log_btn.place(x=450,y=450)
       #reg
       lbl2.place(x=702,y=150)
       lbl2.config(bg="#fff",fg="#fff")
       register_lbl.place(x=787,y=180)
       name_.place(x=722,y=270)
       uname_.place(x=722,y=330)
       if yes_no1[-1]=='yes':
          show1_btn.place(x=970,y=390)
       else:
          blind1_btn.place(x=970,y=390)
       pwd_.place(x=722,y=390)
       reg_btn.place(x=772,y=470)

def call_upon():
    side_nav.place(x=-1500,y=-2)
    line.place(x=-1500,y=-1)
    home_btn.place(x=-1500,y=131)
    quick_btn.place(x=-1500,y=201)
    rank_btn.place(x=-1500,y=271)
    fre_btn.place(x=-1500,y=0)
    sin_out_btn.place(x=-1500,y=0)
    re_nav_btn.place(x=-1500,y=0)
    profile.place(x=-1500,y=50)
    head1.config(text="Typing Ritual")
    frame.place(x=-1500,y=0)
    a=new.focus()
    a=new.item(a)
    a=a['values']
    a=a[1]
    nav_btn.place(x=-1500,y=0)
    psel=cur.execute(f"select * from details where username='{a}';")
    for git in psel:
        na_me=git[0]
        pa_ss=git[2]
        break
    psel1=cur.execute(f"select * from {a}{pa_ss}code;")
    for git1 in psel1:
        co_de=git1[0]
        break
    psel2=cur.execute(f"select * from {a}{pa_ss}photo;")
    for git2 in psel2:
        phoho=git2[0]
    phoho=phoho
    white2.place(x=300,y=100)
    __name_1_.place(x=600,y=150)
    __name1_1_.place(x=750,y=153)
    __name1_1_.config(text=f"{na_me}")
    __uname_1_.place(x=600,y=220)
    __uname1_1_.place(x=822,y=223)
    __uname1_1_.config(text=f"{a}")
    ref_code1.place(x=600,y=320)
    ref_code1.config(text=f"{co_de}")
    copy_btn_1.place(x=850,y=320)
    avg_gwpm_1.place(x=450,y=480)
    avg_acc_1.place(x=670,y=480)
    avg_nwpm_1.place(x=850,y=480)
    avg_gwpm1_1.place(x=510,y=430)
    avg_acc1_1.place(x=720,y=430)
    avg_nwpm1_1.place(x=890,y=430)
    follower_1.place(x=320,y=320)
    following_1.place(x=450,y=320)
    follower1_1.place(x=370,y=285)
    following1_1.place(x=500,y=285)
    prof_image1.config(image=uni1[phoho])
    prof_image1.place(x=380,y=130)
    back_button1.place(x=5,y=3)
    cur.execute(f"insert into cur_show values('{co_de}');")
    con.commit()
    averager1(a,pa_ss)

def back_n3():
    frame.place(x=350,y=90)
    nav_btn.place(x=5,y=0)
    #reg
    white2.place(x=-1500,y=100)
    __name_1_.place(x=-1500,y=150)
    __name1_1_.place(x=-1500,y=153)
    __uname_1_.place(x=-1500,y=220)
    __uname1_1_.place(x=-1500,y=223)
    ref_code1.place(x=-1500,y=320)
    copy_btn_1.place(x=-1500,y=320)
    avg_gwpm_1.place(x=-1500,y=480)
    avg_acc_1.place(x=-1500,y=480)
    avg_nwpm_1.place(x=-1500,y=480)
    avg_gwpm1_1.place(x=-1500,y=430)
    avg_acc1_1.place(x=-1500,y=430)
    avg_nwpm1_1.place(x=-1500,y=430)
    follower_1.place(x=-1500,y=320)
    following_1.place(x=-1500,y=320)
    follower1_1.place(x=-1500,y=285)
    following1_1.place(x=-1500,y=285)
    follow_btn.place(x=-1500,y=0)
    unfollow_btn.place(x=-1500,y=0)
    prof_image1.place(x=-1500,y=130)
    back_button1.place(x=-1500,y=3)
    head1.config(text="ScoreBoard")

def quick1_():
    search_bar.place(x=-1500,y=100)
    search_list.place(x=-1500,y=0)
    sign_out.place(x=-1500,y=3)
    frame.place(x=-1500,y=0)
    #reg
    sent_win.place(x=-1500,y=170)
    txt.place(x=-1500,y=450)
    clock.place(x=-1500,y=80)
    side_nav.place(x=-1500,y=-2)
    line.place(x=-1500,y=-1)
    home_btn.place(x=-1500,y=131)
    quick_btn.place(x=-1500,y=201)
    rank_btn.place(x=-1500,y=271)
    fre_btn.place(x=-1500,y=0)
    sin_out_btn.place(x=-1500,y=411)
    re_nav_btn.place(x=-1500,y=0)
    profile.place(x=-1500,y=50)
    reset_btn.place(x=-1500,y=550)
    quick2_()

def quick2_():
    compu.place(x=450,y=50)
    sent_show.place(x=491,y=110)
    txt1.place(x=327,y=590)
    cancer()

def cancer2():
    accy.place(x=-1500,y=0)
    cancer()

def cancer():
    file=open(rf"{image_url}\quicks.txt",'r')
    textx=[]
    for uty in file:
        textx.append(uty.strip())
    bull=textx[random.choice(list(range(0,len(textx))))]
    sent_show.config(text=bull)
    bull=bull.replace("'",'')
    cur.execute(f"insert into words values('{bull}');")
    con.commit()

def cancer1():
    win.after(2000,cancer2)
win.mainloop()
cur.execute("insert into timer values(59);")
con.commit()
