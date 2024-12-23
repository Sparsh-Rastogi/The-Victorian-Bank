import mysql.connector
from PIL import Image
import datetime
import tkinter as tk
import customtkinter as ctk
conn = mysql.connector.connect(host="localhost",user="root",password="5020",database="project12")
mycurs = conn.cursor()
data = None
root= None
win = None
login = None
account = None
status = ""
stage = 0
def classic_theme(x):
     for i in x:
          if type(i) == ctk.CTkButton:
               print("hi")
               i.configure(corner_radius=0,fg_color="SystemButtonText")
def root_win():
    global root
    root = ctk.CTk()
    root.title("The Victorians Bank")
    root.geometry("600x400+400+180")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    switchvar = ctk.StringVar(value="Dark")
    def switch_mode(widget):
            switch = widget[0]
            switch.configure(text=switchvar.get())
            ctk.set_appearance_mode(switchvar.get().lower())
            if switchvar.get()=="Dark":
                ctk.set_default_color_theme("green")
            else:
                classic_theme(widget)
                ctk.set_default_color_theme("dark-blue")
    def intro(func):
        wel_text =ctk.CTkLabel(root,text="Welcome",font=("helvetica",80),width=600,height=400,anchor="center")
        wel_text.grid(row=0,column=0)
        root.after("2000",wel_text.destroy)
        root.after("2000",func)
        return None
    def root_layout():
        global status
        def root_work(x):
             global status
             global data
             status = x
             root.state("icon")
             if status=="signin":
               data = signin_win()
             elif status=="login":
               data = login_win()
               print(data)
             if data != None:
                    root.state("icon")
                    root.quit()
        widgets = []
        switch = ctk.CTkSwitch(root,text="Dark",command=lambda:switch_mode(widgets),variable=switchvar,onvalue="Dark",offvalue="Light")
        heading=ctk.CTkLabel(root,text="VICTORIAN \n BANK",font=("algerian",40),height=100,width=400,anchor="center")
        heading.grid(row=1,column=0,columnspan=3)
        bg = ctk.CTkImage(light_image=Image.open("bg_root.jpg"),dark_image=Image.open("image (1).jpg"),size=(600,150))
        bg_root = ctk.CTkLabel(root,image=bg,height=150,width=600,text="")
        bg_root.grid(row=5,column=0,columnspan=3)
        sub_head = ctk.CTkLabel(root,text="Your Safety is Our Priority")
        sub_head.grid(row=2,column=0,columnspan=3)
        button1 = tk.Button(root,text="Create a new account",command=lambda:root_work("signin"))
        button2 = tk.Button(root,text="Login to an existing account",command=lambda:root_work("login"))
        button1.grid(row=3,column=0,pady=12,columnspan=3)
        button2.grid(row=4,column=0,pady=12,columnspan=3)
        #frame.grid(row=3,column=1)
        switch.grid(row=0,column=0,sticky="W")
        widgets = [switch,button1,button2,heading]
    intro(root_layout)
    root.mainloop()
    return status
def signin_win(): 
     global login 
     widgets=[]
     try:
         login.destroy()
     except:
          pass 
     global win
     win = ctk.CTkToplevel(root)
     win.geometry("600x600+400+80")
     win.title("SIGN-IN WINDOW") 
     switchvar = ctk.StringVar(value="Dark")
     def switch_mode(widget):
               switch = widget[0]
               switch.configure(text=switchvar.get())
               ctk.set_appearance_mode(switchvar.get().lower())
               if switchvar.get()=="Dark":
                    ctk.set_default_color_theme("green")
               else:
                    classic_theme(widget)
                    ctk.set_default_color_theme("dark-blue")
     switch = ctk.CTkSwitch(win,text="Dark",command=lambda:switch_mode(widgets),variable=switchvar,onvalue="Dark",offvalue="Light")
     switch.grid(row=0,column=0)
     c1 = ctk.IntVar()
     c2 = ctk.IntVar()
     c3 = ctk.IntVar()
     def checkbox(x):
          global gender
          gender = x
          if x== "M":
               c2.set(0)
               c3.set(0)
          elif x=="F":
               c1.set(0)
               c3.set(0)
          elif x =="O":
               c2.set(0)
               c1.set(0)
     name_ent = ctk.CTkEntry(win,width=180,placeholder_text="Enter full name")
     mob_ent = ctk.CTkEntry(win,width=180,placeholder_text="Enter mobile number")
     dob_ent = ctk.CTkEntry(win,width=180,placeholder_text="DD/MM/YYYY")
     pin_ent = ctk.CTkEntry(win,width=80,placeholder_text="5-digit number")
     the_label = ctk.CTkLabel(win,text="Sign-In",font=("Arial",50),width=600)
     the_label.grid(row=1,column=0,columnspan=6,pady=20)
     name_lab = ctk.CTkLabel(win,text="Full Name: ",font=("Arial",15))
     mob_lab = ctk.CTkLabel(win,text="Mobile No.: ",font=("Arial",15))
     dob_lab = ctk.CTkLabel(win,text="Date of Birth: ",font=("Arial",15))
     gen_lab = ctk.CTkLabel(win,text="Gender: ",font=("Arial",15))
     pin_lab = ctk.CTkLabel(win,text="Set a pin: ",font=("Arial",15))
     name_lab.grid(row=2,column=1,sticky="W")
     mob_lab.grid(row=3,column=1,sticky="W")
     dob_lab.grid(row=4,column=1,sticky="W")
     gen_lab.grid(row=5,column=1,sticky="W")
     pin_lab.grid(row=6,column=1,sticky="W")
     name_ent.grid(row=2,column=2,pady=10,columnspan=3)
     mob_ent.grid(row=3,column=2,pady=10,columnspan=3)
     dob_ent.grid(row=4,column=2,pady=10,columnspan=3)
     pin_ent.grid(row=6,column=2,pady=10,columnspan=3)
     box1= ctk.CTkCheckBox(win,text="Male",font=("Arial",8),command=lambda: checkbox("M"),variable=c1)
     box1.grid(row=5,column=2)
     box2= ctk.CTkCheckBox(win,text="Female",font=("Arial",8),command=lambda: checkbox("F"),variable=c2)
     box2.grid(row=5,column=3)
     box3= ctk.CTkCheckBox(win,text="I identify as pikachu",font=("Arial",10),command=lambda: checkbox("O"),variable=c3)
     box3.grid(row=5,column=4)
     widgets =[switch,name_ent,mob_ent,dob_ent]
     def submit():
          final_label=ctk.CTkLabel(win,text="Your account has been created! :)",font=("Arial",20))
          final_label.grid(row=8,column=0,columnspan=6)
          win.after("2000",win.quit)
     button = ctk.CTkButton(win,text="Submit",command=submit)
     button.grid(row=7,column=0,columnspan=6)
     win.mainloop()
     try:
          global gender
          data = [name_ent.get(),mob_ent.get(),dob_ent.get(),pin_ent.get(),gender]
          win.destroy()
          return data
     except:
          pass
def login_win():
     global win
     widgets= []
     try:
          win.destroy()
     except:
          pass
     global login
     login = ctk.CTkToplevel(root)
     login.geometry("400x400+500+180")
     switchvar = ctk.StringVar(value="Dark")
     def switch_mode(widget):
               switch = widget[0]
               switch.configure(text=switchvar.get())
               ctk.set_appearance_mode(switchvar.get().lower())
               if switchvar.get()=="Dark":
                    ctk.set_default_color_theme("green")
               else:
                    classic_theme(widget)
                    ctk.set_default_color_theme("dark-blue")
     switch = ctk.CTkSwitch(login,text="Dark",command=lambda:switch_mode(widgets),variable=switchvar,onvalue="Dark",offvalue="Light")
     switch.grid(row=0,column=0)
     the_label= ctk.CTkLabel(login,text="Log-In",font=("Arial",40))
     the_label.grid(row=1,column=1,columnspan=3)
     us_lab= ctk.CTkLabel(login,text="Enter name: ")
     pin_lab = ctk.CTkLabel(login,text="Enter pin")
     us_ent = ctk.CTkEntry(login)
     pin_ent= ctk.CTkEntry(login)
     us_lab.grid(row=2,column=1,pady=20)
     pin_lab.grid(row=3,column=1,pady=10)
     us_ent.grid(row=2,column=2)
     pin_ent.grid(row=3,column=2)
     def check_easter(self):
          if us_ent.get().title()=="Master":
               if pin_ent.get()=="00000":
                    mycurs.execute("Select * from acct_data")
                    all_data = mycurs.fetchall()
                    master = ctk.CTk()
                    ro = 0
                    for i in all_data:
                         col = 0
                         for j in i:
                              ctk.CTkLabel(master=master,text=j).grid(row=ro,column=col,padx=20)
                              col +=1
                         ro+=1
                    master.mainloop()
                    master.quit()
     pin_ent.bind("<Return>",check_easter)
     def verify():
          login.state("icon")
          login.quit()
     submit = ctk.CTkButton(login,text="Submit",command=verify)
     submit.grid(row=4,column=1,columnspan=3)
     widgets=[switch]
     login.mainloop()
     try:
          return (us_ent.get(),pin_ent.get())
     except:
          pass
def interface(stuff=["Name","Mobile No.","Date of birth","Pin","Acct no","Gender",10000]):
    global account
    widgets = []
    account= ctk.CTk()
    account.geometry("750x600+325+80")
    head_label = ctk.CTkLabel(account,text="Victorian Bank",font=("Arial",45))
    head_label.grid(row=0,column=1,columnspan=4,padx=80,pady=15)
    switchvar = ctk.StringVar(value="Dark")
    def switch_mode(widget):
               switch = widget[0]
               switch.configure(text=switchvar.get())
               ctk.set_appearance_mode(switchvar.get().lower())
               if switchvar.get()=="Dark":
                    ctk.set_default_color_theme("green")
               else:
                    classic_theme(widget)
                    ctk.set_default_color_theme("dark-blue")
    switch = ctk.CTkSwitch(account,text="Dark",font=("Arial",15),command=lambda:switch_mode(widgets),variable=switchvar,onvalue="Dark",offvalue="Light",switch_width=55,switch_height=25)
    switch.grid(row=0,column=0,padx=20)
    widgets = [switch]
    def frame_change(command):
        try:
          mainframe.destroy()
        except:
          pass
        mainframe = ctk.CTkFrame(account,height=500,width=540,)
        mainframe.grid_propagate(False)
        mainframe.grid(row=1,column=1,columnspan=4,sticky="NSEW",padx=10)
        if command=="bill":
             mycurs.execute(f"select date,person2 from u{stuff[4]} where who = 1 order by date desc")
             data = mycurs.fetchall()
             data_dict = {"mobile":"not paid","electricity":"not paid","water":"not paid"}
             if data!= None: 
               print(data)
               for i in data:
                    if i[1]=="mobile" and data_dict["mobile"]=="not paid":
                         data_dict["mobile"]=i[0]
                    if i[1]=="electricity" and data_dict["electricity"]=="not paid":
                         data_dict["electricity"]=i[0]
                    if i[1]=="water" and data_dict["water"]=="not paid":
                         data_dict["water"]=i[0]
             canva1= ctk.CTkFrame(mainframe,width=500,height=150)
             canva1.grid_propagate(False)
             canva2= ctk.CTkFrame(mainframe,width=500,height=150)
             canva2.grid_propagate(False)
             canva3= ctk.CTkFrame(mainframe,width=500,height=150)
             canva3.grid_propagate(False)
             canva1.grid(row=0,column=0,columnspan=4,pady=10,padx=10)
             canva2.grid(row=1,column=0,columnspan=4,pady=10,padx=10)
             canva3.grid(row=2,column=0,columnspan=4,pady=10,padx=10)
             loop_list = [(canva1,"Mobile Recharge",data_dict["mobile"]),(canva2,"Electricity Recharge",data_dict["electricity"]),(canva3,"Water Bill",data_dict["water"])]
             def been_paid(event,butt):
                  text=butt.cget("text")
                  amt_list = [100,1000,1000]
                  service_list = ["mobile","electricity","water"]
                  text_list = ["Mobile Recharge","Electricity Recharge","Water Bill"]
                  service = service_list[text_list.index(text)]
                  amt = amt_list[text_list.index(text)]
                  mycurs.execute(f"select balance from acct_data where account_no = {stuff[4]}")
                  [(bal,)] = mycurs.fetchall()
                  newbal= bal - amt
                  mycurs.execute(f'''insert into u{stuff[4]} values("{datetime.date.today()}","{service}",{amt},"1",{newbal},"c") ''')
                  conn.commit()
                  frame_change("info")
             for i in loop_list:
                  y =ctk.CTkLabel(i[0],text=i[1],font=("Arial",25))
                  y.grid(row=0,column=0,columnspan=2)
                  ctk.CTkLabel(i[0],text=f"Last paid: {i[2]}",font=("Arial",18)).grid(row=1,column=0,pady=20)
                  x= ctk.CTkButton(i[0],text="PAY",height=35,width=100)
                  x.bind("<1>",command=lambda event,obj=y:been_paid(event,obj))
                  x.grid(row=1,column=1,pady=20,sticky="E")
               
        if command=="hist":
             filt1 = tk.Button(mainframe,text="All",width=15,bg="grey")
             def filt1_func():
                  texts = ["All","Transferred","Recieved","Bills"]
                  cur_text = filt1.cget("text")
                  if cur_text=="Bills":
                       new_text = "All"
                  else:
                       new_text = texts[texts.index(cur_text)+1]
                  filt1.configure(text=new_text)
                  canva_change(new_text)
             filt1.configure(command=filt1_func) 
             filt1.grid(row=0,column=0,padx=10,pady=10)
             def canva_change(commando):
                  try:
                       canvas.destroy()
                  except:
                       pass
                  canvas = ctk.CTkScrollableFrame(mainframe,width=500,height=450,orientation="vertical")
                  canvas.grid(row=1,column=0,columnspan=5,padx=10)
                  if commando=="All":
                       mycurs.execute(f"select * from u{stuff[4]}")
                       data = mycurs.fetchall()
                       data.insert(0,("Date","From/to","Amount","","Balance",""))
                  if commando=="Transferred":  
                       mycurs.execute(f'''select * from u{stuff[4]} where c_d = "c"''')
                       data = mycurs.fetchall()
                       data.insert(0,("Date","To","Amount","","Balance",""))
                  if commando=="Recieved":  
                       mycurs.execute(f'''select * from u{stuff[4]} where c_d = "d"''')
                       data = mycurs.fetchall()
                       data.insert(0,("Date","From","Amount","","Balance",""))
                  if commando=="Bills":
                       mycurs.execute(f'''select * from u{stuff[4]} where who = "1"''')
                       data = mycurs.fetchall()
                       data.insert(0,("Date","From/to","Amount","","Balance",""))
                  r=0
                  c=0
                  for i in data:
                       for j in range(len(i)):
                            if j in [0,1,2,4]:
                                 ctk.CTkLabel(canvas,text=i[j],font=("Arial",18),width=85).grid(row=r,column=c,padx=15)
                                 c+=1
                       r+=1
                       c=0  
             canva_change("All")
        if command=="tran":
             def show_amount(what):
                  x = stuff[6]
                  amt_ent.delete(0,len(amt_ent.get()))
                  amt_ent.insert(0,str(int(x*what)))
             def show_slider(event):
                  value = int(amt_ent.get())
                  x = stuff[6]
                  if value <= x:
                       what =(value/x)
                  if value > x:
                       amt_ent.delete(0,len(amt_ent.get()))
                       amt_ent.insert(0,str(int(x)))
                       what = 1
                  amt_slid.set(what)  
             user_ent = ctk.CTkEntry(mainframe,width=180)
             amt_ent = ctk.CTkEntry(mainframe,width=120,height=56,corner_radius=15,placeholder_text="Amount",font=("Arial",22))
             user_ent.grid(row=1,column=0,padx=10,columnspan=4)
             amt_ent.grid(row=2,column=1,columnspan=2,pady=40,sticky="W",padx=20)
             amt_ent.bind("<Return>",show_slider)
             user_lab = ctk.CTkLabel(mainframe,text="Enter the reciever's account number: ",font=("Arial",20))
             amt_lab = ctk.CTkLabel(mainframe,text="Amount: ",font=("Arial",25))
             user_lab.grid(row=0,column=0,padx=100,pady=10,columnspan=4)
             amt_lab.grid(row=2,column=0,sticky="E")
             amt_slid = ctk.CTkSlider(mainframe,width=300,command=show_amount)
             amt_slid.grid(row=3,column=0,columnspan=4)
             def transfer_done():
                amt_trans = int(amt_ent.get())
                bal = stuff[6]
                newbal = bal-amt_trans
                stuff[6]=newbal
                mycurs.execute(f"update acct_data set balance={newbal} where account_no={stuff[4]}")
                mycurs.execute(f"select balance from acct_data where account_no={user_ent.get()}")
                (rec_bal,) = mycurs.fetchone()
                new_rec_bal = amt_trans+rec_bal
                mycurs.execute(f"update acct_data set balance={new_rec_bal} where account_no={user_ent.get()}")
                mycurs.execute(f'''insert into u{stuff[4]} values("{datetime.date.today()}",{user_ent.get()},{amt_trans},"0",{newbal},"c")''')
                mycurs.execute(f'''insert into u{user_ent.get()} values("{datetime.date.today()}",{stuff[4]},{amt_trans},"0",{new_rec_bal},"d")''')
                conn.commit()
                frame_change("info")
             transbut = ctk.CTkButton(mainframe,text="Transfer",command=transfer_done)
             transbut.grid(row=4,column=0,columnspan=4,pady=15)
        if command == "info":
          name_ent = ctk.CTkLabel(mainframe,width=180,text=stuff[0])
          mob_ent = ctk.CTkLabel(mainframe,width=180,text=stuff[1])
          acct_ent = ctk.CTkLabel(mainframe,width=180,text=stuff[4])
          dob_ent = ctk.CTkLabel(mainframe,width=180,text=stuff[2])
          pin_ent = ctk.CTkButton(mainframe,width=80,text="*****",fg_color="transparent")
          gen_ent = ctk.CTkLabel(mainframe,width=80,text=stuff[5])
          name_lab = ctk.CTkLabel(mainframe,text="Full Name: ",font=("Arial",20))
          acct_lab = ctk.CTkLabel(mainframe,text="Account No.: ",font=("Arial",20))
          mob_lab = ctk.CTkLabel(mainframe,text="Mobile No.: ",font=("Arial",20))
          dob_lab = ctk.CTkLabel(mainframe,text="Date of Birth: ",font=("Arial",20))
          gen_lab = ctk.CTkLabel(mainframe,text="Gender: ",font=("Arial",20))
          pin_lab = ctk.CTkLabel(mainframe,text="Pin: ",font=("Arial",20))
          def show_hide():
               if pin_ent.cget("text")==stuff[3]:
                    pin_ent.configure(text="*****")
               elif pin_ent.cget("text")=="*****":
                    pin_ent.configure(text=stuff[3])
          pin_ent.configure(command=show_hide)
          name_lab.grid(row=2,column=1,sticky="W",padx=10)
          acct_lab.grid(row=3,column=1,sticky="W",padx=10)
          mob_lab.grid(row=4,column=1,sticky="W",padx=10)
          dob_lab.grid(row=5,column=1,sticky="W",padx=10)
          gen_lab.grid(row=6,column=1,sticky="W",padx=10)
          pin_lab.grid(row=7,column=1,sticky="W",padx=10)
          name_ent.grid(row=2,column=2,pady=10,columnspan=3,padx=10)
          acct_ent.grid(row=3,column=2,pady=10,columnspan=3,padx=10)
          mob_ent.grid(row=4,column=2,pady=10,columnspan=3,padx=10)
          dob_ent.grid(row=5,column=2,pady=10,columnspan=3,padx=10)
          gen_ent.grid(row=6,column=2,pady=10,columnspan=3,padx=10)
          pin_ent.grid(row=7,column=2,pady=10,columnspan=3,padx=10)
    frame_change("info")
    sideframe = ctk.CTkFrame(account,height=520,width=180)
    info =ctk.CTkButton(sideframe,font=("Arial",20),text="Your Account",corner_radius=0,fg_color="transparent",text_color=("black","white"),command=lambda: frame_change("info"))
    hist =ctk.CTkButton(sideframe,font=("Arial",20),text="Transaction History",corner_radius=0,fg_color="transparent",text_color=("black","white"),command=lambda: frame_change("hist"))
    tran = ctk.CTkButton(sideframe,font=("Arial",20), text = "Money Transfer",corner_radius=0,fg_color="transparent",text_color=("black","white"),command=lambda: frame_change("tran"))
    bill =ctk.CTkButton(sideframe,font=("Arial",20),text="Bill Payments",corner_radius=0,fg_color="transparent",text_color=("black","white"),command=lambda: frame_change("bill"))
    info.grid(column=0,row=1,pady=15)
    hist.grid(column=0,row=2,pady=15)
    tran.grid(column=0,row=3,pady=15)
    bill.grid(column=0,row=4,pady=15)
    sideframe.grid_propagate(False)
    sideframe.grid(column=0,row=1)
