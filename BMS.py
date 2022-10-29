from time import strftime
from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import time


root = Tk()
root.geometry("1600x700+0+0")
root.title("Billing Management System")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Billing Management System",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)

bill_num = IntVar()
date = StringVar()
bill_reason = StringVar()
bill_amount = IntVar()
bill_staff = StringVar()
role = StringVar()
company_name = StringVar()
used_month = StringVar()
staff_name = StringVar()
c_id = 1

def reset():
    bill_num.set("")
    date.set("")
    bill_reason.set("")
    bill_amount.set("")
    bill_staff.set("")
    role.set("")
    company_name.set("")
    used_month.set("")
    staff_name.set("")

def save():
    bn = bill_num.get()
    d = date.get()
    br = bill_reason.get()
    ba = bill_amount.get()
    bs = bill_staff.get()
    r = role.get()
    cn = company_name.get()
    um = used_month.get()
    sn = staff_name.get()
    
    if (bn == "" or d == "" or br == ""or ba == ""or bs == ""or r == ""or cn == ""or um == ""or sn == ""):
        MessageBox.showinfo("Insert Status", "All Fields are required.")
    else:
        con = mysql.connect(host='localhost', user ='root', password='root', database ='bill1')
        cursor = con.cursor()

        company = "insert into company(Name, Staffname) values(%s,%s)"
        cval = (cn, sn)
        cursor.execute(company, cval)

        billing = "insert into bill(BillingNumber, billingdate, BillingReason, BillAmount, BillStaff, StaffPosition, UsageMonth) values(%s,%s,%s,%s,%s,%s,%s)"
        bval = (bn, d, br, ba, bs, r, um)
        cursor.execute(billing, bval)
        
        con.commit()

        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


lblBillingNumber = Label(f1, font=( 'aria' ,16, 'bold' ),text="Billingနံပါတ်",fg="steel blue",bd=10,anchor='w')
lblBillingNumber.grid(row=0,column=0)
txtBillingနံပါတ် = Entry(f1,font=('ariel' ,16,'bold'), textvariable=bill_num , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtBillingနံပါတ်.grid(row=0,column=1)

lblBillingDate = Label(f1, font=( 'aria' ,16, 'bold' ),text="နေ့စွဲ",fg="steel blue",bd=10,anchor='w')
lblBillingDate.grid(row=1,column=0)
txtBillingDate = Entry(f1,font=('ariel' ,16,'bold'), textvariable=date , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtBillingDate.grid(row=1,column=1)

lblBillingReason = Label(f1, font=( 'aria' ,16, 'bold' ),text="BillingReason",fg="steel blue",bd=10,anchor='w')
lblBillingReason.grid(row=2,column=0)
txtBillingReason = Entry(f1,font=('ariel' ,16,'bold'), textvariable=bill_reason , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtBillingReason.grid(row=2,column=1)

lblBillAmount = Label(f1, font=( 'aria' ,16, 'bold' ),text="BillAmount",fg="steel blue",bd=10,anchor='w')
lblBillAmount.grid(row=3,column=0)
txtBillAmount = Entry(f1,font=('ariel' ,16,'bold'), textvariable=bill_amount , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtBillAmount.grid(row=3,column=1)

lblBillingStaff = Label(f1, font=( 'aria' ,16, 'bold' ),text="Billကောက်ခံသောဝန်ထမ်းအမည်",fg="steel blue",bd=10,anchor='w')
lblBillingStaff.grid(row=4,column=0)
txtBillingStaff = Entry(f1,font=('ariel' ,16,'bold'), textvariable=bill_staff , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtBillingStaff.grid(row=4,column=1)

lblStaffPosition = Label(f1, font=( 'aria' ,16, 'bold' ),text="ရာထူး",fg="steel blue",bd=10,anchor='w')
lblStaffPosition.grid(row=5,column=0)
txtStaffPosition = Entry(f1,font=('ariel' ,16,'bold'), textvariable=role , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtStaffPosition.grid(row=5,column=1)

lblC_name = Label(f1, font=( 'aria' ,16, 'bold' ),text="လုပ်ငန်းအမည်",fg="steel blue",bd=10,anchor='w')
lblC_name.grid(row=0,column=2)
txtC_name = Entry(f1,font=('ariel' ,16,'bold'), textvariable=company_name , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtC_name.grid(row=0,column=3)

lblUsageMonth = Label(f1, font=( 'aria' ,16, 'bold' ),text="သုံးစွဲသောလ",fg="steel blue",bd=10,anchor='w')
lblUsageMonth.grid(row=1,column=2)
txtUsageMonth = Entry(f1,font=('ariel' ,16,'bold'), textvariable=used_month , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtUsageMonth.grid(row=1,column=3)

lblC_staffname = Label(f1, font=( 'aria' ,16, 'bold' ),text="ဝန်ထမ်းအမည်",fg="steel blue",bd=10,anchor='w')
lblC_staffname.grid(row=2,column=2)
txtC_staffname = Entry(f1,font=('ariel' ,16,'bold'), textvariable=staff_name , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtC_staffname.grid(row=2,column=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Save", bg="powder blue",command=save)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=exit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Unit", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1 unit", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="0.75 $", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2 units", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1.5 $", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10 units", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="7.5 $", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50 units", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="37.5 $", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100 units", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="75 $", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=7, column=0)


root.mainloop()
