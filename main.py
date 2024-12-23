import func
import mysql.connector 
import random
import customtkinter as ctk
master=None
conn = mysql.connector.connect(host="localhost",user="root",password="5020",database="project12")
if conn.is_connected():
    print("connection estabished...")
mycurs = conn.cursor()
mycurs.execute("select account_no from acct_data")
accts = mycurs.fetchall()
enter_method = func.root_win()
def ready_interface(acctno,win=ctk.CTk()):
    mycurs.execute(f'''select * from acct_data where account_no = "{acctno}"''')
    [stuff] = mycurs.fetchall()
    stuff = list(stuff)
    func.interface(stuff)
    func.account.mainloop()
if enter_method=="login":
    mycurs.execute("select name from acct_data")
    names = mycurs.fetchall()
    name = func.data[0].title()
    pin = int(func.data[1])
    if (name,) in names:
        mycurs.execute(f'''select pin from acct_data where name = "{name}" ''')
        correct_pin= mycurs.fetchall()
        if [(pin,)]==correct_pin:
            mycurs.execute(f'''select account_no from acct_data where name= "{name}" and pin={pin}''')
            [(acct_no,)]=mycurs.fetchall()
            print(acct_no)
            func.login.destroy()
            func.root.destroy()
            ready_interface(acct_no,func.account)
if enter_method=="signin":
    data = func.data
    acct_no = random.randrange(10000000,99999999,2)
    while (acct_no,) in accts:
        acct_no = random.randrange(10000000,99999999,2)
    mycurs.execute(f'''insert into acct_data (name,mobile_num,dob,pin,account_no,gender)values("{data[0]}",{data[1]},"{data[2]}",{data[3]},{acct_no},"{data[4]}")''')
    mycurs.execute(f'''create table u{acct_no} (date varchar(12), person2 varchar(20), amount int, who char(1), newbal int, c_d char(1) )''')
    conn.commit()
    func.root.destroy()
    ready_interface(acct_no,func.account)