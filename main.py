#import---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyglet
import mysql.connector as ms
from PIL import Image, ImageTk
from subprocess import call


#definitions---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def checking():
    global i, t
    un = username.get()
    pw = password.get()
    if un == 'A' and pw == 'A':
        login_window.destroy()
        t = 1
    elif un == 'Username' and pw == 'Password':
        messagebox.showerror(title='Geo', message='Default fields')
        password_entry.delete(0, END)
        username_entry.delete(0, END)
    elif un == '' or pw == '':
        messagebox.showerror(title='Geo', message='Please enter both fields')
        password_entry.delete(0, END)
    else:
        i += 1
        if i < 3:
            x = 'incorrect password/username, ' + str(i) + ' of 3 tries'
            messagebox.showerror(title='Geo', message=x)
            password_entry.delete(0, END)
            password_entry.focus()
        else:
            messagebox.showerror(title='Geo', message='Too many incorrect attempts....The program will now close')
            login_window.destroy()


def insertingdir():
    global dno, name, phone, job

    insertion_window = Toplevel(main_window)
    insertion_window.geometry('720x300')
    insertion_window.grid_propagate(False)
    insertion_window.resizable(False, False)
    main_window.withdraw()
    dno = StringVar()
    name = StringVar()
    phone = StringVar()
    job = StringVar()

    Label(insertion_window, bg='#bc8dbb', height=1000, width=1000).pack()  #
    x = "INSERT INTO DIRECTORY VALUES(%s,%s,%s,%s)"
    lbl_title = Label(insertion_window, text="INSERTING RECORDS", font=('BOLDs', 25, 'bold',), bg='#e0a8c5',
                      fg='GREY10').place(x=150, y=10)

    dno_entry = Entry(insertion_window, font=('abel', 15), border=1, width=25, bg='#e0a8c5', textvariable=dno)
    dno_entry.place(x=81, y=80)
    Label(insertion_window, text='DNo:', font=('abel', 17), bg='#e0a8c5').place(x=5, y=80)
    name_entry = Entry(insertion_window, font=('abel', 15), border=1, width=25, bg='#e0a8c5', textvariable=name)
    name_entry.place(x=82, y=120)
    Label(insertion_window, text='NAME:', font=('abel', 17), bg='#e0a8c5').place(x=0, y=120)
    phone_entry = Entry(insertion_window, font=('abel', 15), border=1, width=25, bg='#e0a8c5', textvariable=phone)
    phone_entry.place(x=445, y=80)
    Label(insertion_window, text='PHONE:', font=('abel', 17), bg='#e0a8c5').place(x=350, y=80)
    job_entry = Entry(insertion_window, font=('abel', 15), border=1, width=25, bg='#e0a8c5', textvariable=job)
    job_entry.place(x=445, y=120)
    Label(insertion_window, text='JOB:', font=('abel', 17), bg='#e0a8c5').place(x=360, y=120)
    Button(insertion_window, text='SUBMIT', bg='#e0a8c5', width=30, height=2,
           command=lambda: [inserteddir(), dno_entry.delete(0, END), name_entry.delete(0, END),
                            phone_entry.delete(0, END), job_entry.delete(0, END)]).place(x=400, y=180)
    Button(insertion_window, text='CLOSE', bg='#e0a8c5', width=30, height=2,
           command=lambda: [insertion_window.destroy(), main_window.deiconify()]).place(x=70, y=180)


def insertingadd():
    global aid, hno, area, city, pincode, dno
    insertion_window = Toplevel(main_window)
    insertion_window.geometry('600x300')
    aid = StringVar()
    hno = StringVar()
    area = StringVar()
    city = StringVar()
    pincode = StringVar()
    dno = StringVar()
    main_window.withdraw()
    Label(insertion_window, bg='#bc8dbb', height=1000, width=1000).pack()
    x = 'INSERT INTO DIRECTORY VALUES(%s,%s,%s,%s)'
    lbl_title = Label(insertion_window, text="INSERTING RECORDS", font=('BOLDs', 25, 'bold',), bg='#e0a8c5',
                      fg='GREY10').place(x=100, y=10)
    aid_entry = Entry(insertion_window, font=('abel', 15), border=1, width=17, bg='#e0a8c5', textvariable=aid)
    aid_entry.place(x=70, y=80)
    Label(insertion_window, text='AID:', font=('abel', 15), bg='#e0a8c5').place(x=10, y=80)
    hno_entry = Entry(insertion_window, font=('abel', 15), border=1, width=17, bg='#e0a8c5', textvariable=hno)
    hno_entry.place(x=70, y=120)
    Label(insertion_window, text='HNo.:', font=('abel', 15), bg='#e0a8c5').place(x=10, y=120)
    area_entry = Entry(insertion_window, font=('abel', 15), border=1, width=17, bg='#e0a8c5', textvariable=area)
    area_entry.place(x=70, y=160)
    Label(insertion_window, text='AREA:', font=('abel', 15), bg='#e0a8c5').place(x=10, y=160)
    city_entry = Entry(insertion_window, font=('abel', 15), border=1, width=17, bg='#e0a8c5', textvariable=city)
    city_entry.place(x=380, y=80)
    Label(insertion_window, text='CITY:', font=('abel', 15), bg='#e0a8c5').place(x=290, y=80)
    pincode_entry = Entry(insertion_window, font=('abel', 15), border=1, width=17, bg='#e0a8c5', textvariable=pincode)
    pincode_entry.place(x=380, y=120)
    Label(insertion_window, text='PIN CODE:', font=('abel', 15), bg='#e0a8c5').place(x=290, y=120)
    dno_entry = Entry(insertion_window, font=('abel', 15), border=1, width=17, bg='#e0a8c5', textvariable=dno)
    dno_entry.place(x=380, y=160)
    Label(insertion_window, text='DNo.:', font=('abel', 15), bg='#e0a8c5').place(x=290, y=160)

    Button(insertion_window, text='SUBMIT', bg='#e0a8c5', width=30, height=2,
           command=lambda: [insertedadd(), aid_entry.delete(0, END), hno_entry.delete(0, END),
                            area_entry.delete(0, END), city_entry.delete(0, END), pincode_entry.delete(0, END),
                            dno_entry.delete(0, END)]).place(x=50, y=250)
    Button(insertion_window, text='CLOSE', bg='#e0a8c5', width=30, height=2,
           command=lambda: [insertion_window.destroy(), main_window.deiconify()]).place(x=290, y=250)


def inserteddir():
    global dno, name, phone, job, dirdno
    c.execute('SELECT DNO FROM DIRECTORY')
    dirdno = []
    r = c.fetchall()
    for i in r:
        for j in i:
            dirdno.append(j)
    che = 0
    x = 'INSERT INTO DIRECTORY VALUES(%s,%s,%s,%s)'
    dirno = dno.get()
    nam = name.get()
    phoneno = phone.get()
    jobb = job.get()
    saf = 0
    for i in range(len(dirdno)):
        if dirno in str(dirdno[i]):
            messagebox.showerror(title='Geo', message='duplicate key')
            che = 1
    for i in nam:
        if i.isalpha() == False and i != ' ':
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Name cant have special characters or numbers')
    saf = 0
    for i in dirno:
        if not i.isnumeric():
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Dno can only have numbers')
    saf = 0
    for i in jobb:
        if not i.isalpha():
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Job cant have numbers or special characters')
    saf = 0
    for i in phoneno:
        if not i.isnumeric():
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Phone number can only have numbers')

    if len(phoneno) != 10:
        messagebox.showerror(title='Geo', message='invalid phone no, must be 10 digits')
        che = 1
    if len(dirno) > 5:
        messagebox.showerror(title='Geo', message='invalid dno must be 5 or less digits')
        che = 1
    if che != 1:
        v = (dirno, nam, phoneno, jobb)
        c.execute(x, v)
        con.commit()
        dirdno.append(dirno)
        messagebox.showinfo(title='geo', message='inserted')


def insertedadd():
    global aid, hno, area, city, pincode, dno
    che = 0
    x = 'INSERT INTO ADDRESS VALUES(%s,%s,%s,%s,%s,%s)'
    ai = aid.get()
    hn = hno.get()
    are = area.get()
    cit = city.get()
    pin = pincode.get()
    dn = dno.get()
    saf = 0
    for i in ai:
        if not i.isnumeric():
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='AID can only have numbers')

    saf = 0
    for i in hn:
        if not i.isalnum():
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='HNo cant have special characters')
    saf = 0
    for i in are:
        if not i.isalpha():
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Area cant have special characters')
    saf = 0
    for i in cit:
        if not i.isalpha():
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='City cant have special characters')
    saf = 0
    for i in pin:
        if not i.isnumeric():
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Pincode can only have numbers')
    saf = 0
    for i in dn:
        if not i.isnumeric():
            saf = 1
            che = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='DNo cant have special characters')
        che = 1
    if len(hn) > 4:
        messagebox.showerror(title='Geo', message='invalid hn, has to be under 5 digits')
        che = 1
    if len(dn) > 5:
        messagebox.showerror(title='Geo', message='invalid dno, has to be 5 or less digits')
        che = 1
    if len(pin) < 6 < len(pin):
        messagebox.showerror(title='Geo', message='invalid pin, has to be 6 digits')
        che = 1
    if che != 1:
        try:
            v = (dn, str(hn), str(are), str(cit), pin, dn)
            c.execute(x, v)
            con.commit()
            messagebox.showinfo(title='geo', message='inserted')
        except ms.Error:
            messagebox.showinfo(title='geo', message='dno not in other table')


def display():
    display_window = Toplevel(main_window)
    display_window.geometry('835x300')
    main_window.withdraw()
    c.execute('SELECT * FROM ADDRESS')
    r = c.fetchall()
    if not r:
        x = 'SELECT * FROM DIRECTORY'
        c.execute(x)
        tree = ttk.Treeview(display_window, selectmode='browse')
        tree.grid(row=1, column=1, padx=20, pady=20)
        tree['columns'] = ('DNo', 'Name', 'Phone', 'Job')
        tree['show'] = 'headings'
        tree.column("DNo", width=200, anchor='c')
        tree.column("Name", width=200, anchor='c')
        tree.column("Phone", width=200, anchor='c')
        tree.column("Job", width=200, anchor='c')
        tree.heading("DNo", text='DNo')
        tree.heading("Name", text='Name')
        tree.heading("Phone", text='Phone')
        tree.heading("Job", text='Job')
        r = c.fetchall()

        for i in r:
            tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3]))
    else:
        x = 'SELECT D.DNO,NAME,PHONE_NO,JOB,HNO,CITY,PINCODE FROM DIRECTORY D,ADDRESS A WHERE D.DNO=A.DNO'
        c.execute(x)
        tree = ttk.Treeview(display_window, selectmode='browse')
        tree.grid(row=1, column=1, padx=20, pady=20)
        tree['columns'] = ('DNo', 'Name', 'Phone', 'Job', 'HNo', 'City', 'Pincode')
        tree['show'] = 'headings'
        tree.column("DNo", width=200, anchor='c')
        tree.column("Name", width=200, anchor='c')
        tree.column("Phone", width=200, anchor='c')
        tree.column("Job", width=200, anchor='c')
        tree.column("HNo", width=200, anchor='c')
        tree.column("City", width=200, anchor='c')
        tree.column("Pincode", width=200, anchor='c')
        tree.heading("DNo", text='DNo')
        tree.heading("Name", text='Name')
        tree.heading("Phone", text='Phone')
        tree.heading("Job", text='Job')
        tree.heading("HNo", text='HNo')
        tree.heading("City", text='City')
        tree.heading("Pincode", text='Pincode')
        r = c.fetchall()
        for i in r:
            tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        c.execute('SELECT * FROM DIRECTORY')
        r = c.fetchall()
        try:

            for i in r:
                tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3], 'NULL', 'NULL', 'NULL'))
        except:
            dfnaoiwd = 1
    Button(display_window, text='CLOSE', font=('abel', 10), border=0,
           command=lambda: [display_window.destroy(), main_window.deiconify()]).place(x=0, y=250)


def searchname():
    global name
    search_window = Toplevel(main_window)
    search_window.geometry('400x300')
    search_window.resizable(False, False)
    main_window.withdraw()
    name = StringVar()

    Label(search_window, bg='#bc8dbb', height=1000, width=1000).pack()
    Label(search_window, text='NAME:', bg='#e0a8c5', font=('abel', 15)).place(x=80, y=100)
    Entry(search_window, bg='#e0a8c5', border=1, font=('abel', 15), textvariable=name).place(x=135, y=100)

    Button(search_window, text='ENTER', bg='#e0a8c5', width=20,
           command=lambda: [show1(), search_window.withdraw()]).place(x=40, y=170)
    Button(search_window, text='CLOSE', bg='#e0a8c5', width=20,
           command=lambda: [search_window.destroy(), main_window.deiconify()]).place(x=200, y=170)


def searchcity():
    global city
    search_window = Toplevel(main_window)
    search_window.geometry('400x300')
    search_window.resizable(False, False)
    main_window.withdraw()
    city = StringVar()
    Label(search_window, bg='#bc8dbb', height=1000, width=1000).pack()
    Label(search_window, text='CITY:', bg='#e0a8c5', font=('abel', 15)).place(x=80, y=100)
    Entry(search_window, bg='#e0a8c5', border=1, font=('abel', 15), textvariable=city).place(x=135, y=100)
    Button(search_window, text='ENTER', bg='#e0a8c5', width=20,
           command=lambda: [show2(), search_window.withdraw()]).place(x=40, y=170)
    Button(search_window, text='CLOSE', bg='#e0a8c5', width=20,
           command=lambda: [search_window.destroy(), main_window.deiconify()]).place(x=200, y=170)


def searchname1():
    global name
    search_window = Toplevel(main_window)
    search_window.geometry('400x300')
    search_window.resizable(False, False)
    main_window.withdraw()
    name = StringVar()

    Label(search_window, bg='#bc8dbb', height=1000, width=1000).pack()
    Label(search_window, text='Name:', bg='#e0a8c5', font=('abel', 15)).place(x=80, y=100)
    ent = Entry(search_window, bg='#e0a8c5', border=1, font=('abel', 15), textvariable=name)
    ent.place(x=135, y=100)
    Button(search_window, text='ENTER', bg='#e0a8c5', width=20,
           command=lambda: [show3(), search_window.withdraw()]).place(x=40, y=170)
    Button(search_window, text='CLOSE', bg='#e0a8c5', width=20,
           command=lambda: [search_window.destroy(), main_window.deiconify()]).place(x=200, y=170)


def show1():
    global name

    nam = name.get()
    che = 0
    saf = 0
    c.execute('SELECT NAME FROM DIRECTORY')
    ifin = []
    r = c.fetchall()
    for i in r:
        for j in i:
            ifin.append(j)
    if nam not in ifin:
        che = 1
        messagebox.showerror(title='Geo', message='Name not in table')
        searchname()
    saf = 0
    for i in nam:
        if i.isalpha() == False and i != ' ':
            saf = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Name cant have special characters or numbers')
    if saf == 0 and che == 0:
        show_window = Toplevel(main_window)
        show_window.geometry('835x100')
        c.execute('SELECT * FROM ADDRESS')
        r = c.fetchall()
        if not r:
            x = 'SELECT * FROM DIRECTORY WHERE NAME=%s'
            v = (nam,)
            c.execute(x, v)
            tree = ttk.Treeview(show_window, selectmode='browse')
            tree.pack()
            tree['columns'] = ('DNo', 'Name', 'Phone', 'Job')
            tree['show'] = 'headings'
            tree.column("DNo", width=200, anchor='c')
            tree.column("Name", width=200, anchor='c')
            tree.column("Phone", width=200, anchor='c')
            tree.column("Job", width=200, anchor='c')
            tree.heading("DNo", text='DNo')
            tree.heading("Name", text='Name')
            tree.heading("Phone", text='Phone')
            tree.heading("Job", text='Job')
            r = c.fetchall()
            for i in r:
                tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3]))
        else:
            x = 'SELECT D.DNO,NAME,PHONE_NO,JOB,HNO,CITY,PINCODE FROM DIRECTORY D,ADDRESS A WHERE NAME=%s'
            v = (nam,)
            c.execute(x, v)
            tree = ttk.Treeview(show_window, selectmode='browse')
            tree.grid(row=1, column=1, padx=20, pady=20)
            tree['columns'] = ('DNo', 'Name', 'Phone', 'Job', 'HNo', 'City', 'Pincode')
            tree['show'] = 'headings'
            tree.column("DNo", width=200, anchor='c')
            tree.column("Name", width=200, anchor='c')
            tree.column("Phone", width=200, anchor='c')
            tree.column("Job", width=200, anchor='c')
            tree.column("HNo", width=200, anchor='c')
            tree.column("City", width=200, anchor='c')
            tree.column("Pincode", width=200, anchor='c')
            tree.heading("DNo", text='DNo')
            tree.heading("Name", text='Name')
            tree.heading("Phone", text='Phone')
            tree.heading("Job", text='Job')
            tree.heading("HNo", text='HNo')
            tree.heading("City", text='City')
            tree.heading("Pincode", text='Pincode')
            r = c.fetchall()
            for i in r:
                tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
            c.execute('SELECT * FROM DIRECTORY')
            r = c.fetchall()
            try:

                for i in r:
                    tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3], 'NULL', 'NULL', 'NULL'))
            except:
                dfnaoiwd = 1

        Button(show_window, text='CLOSE', bg='white', font=('abel', 12), border=0,
               command=lambda: [show_window.destroy(), main_window.deiconify()]).place(x=40, y=60)


def show2():
    global city

    cit = city.get()
    che = 0
    saf = 0
    c.execute('SELECT CITY FROM ADDRESS')
    ifin = []
    r = c.fetchall()
    for i in r:
        for j in i:
            ifin.append(j)
    if cit not in ifin:
        che = 1
        messagebox.showerror(title='Geo', message='City not in the table')
        searchcity()
    for i in cit:
        if not i.isalpha():
            saf = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='City cant have special characters or numbers')

        searchcity()
    if saf == 0 and che == 0:
        show2_window = Toplevel(main_window)
        show2_window.geometry('835x200')
        x = 'SELECT D.DNO,NAME,PHONE_NO,JOB,HNO,CITY,PINCODE FROM DIRECTORY D,ADDRESS A WHERE A.CITY=%s AND A.DNO=D.DNO '
        v = (cit,)
        c.execute(x, v)
        tree = ttk.Treeview(show2_window, selectmode='browse')
        tree.pack()
        tree['columns'] = ('DNo', 'Name', 'Phone', 'Job', 'City')
        tree['show'] = 'headings'
        tree.column("DNo", width=200, anchor='c')
        tree.column("Name", width=200, anchor='c')
        tree.column("Phone", width=200, anchor='c')
        tree.column("Job", width=200, anchor='c')
        tree.column("City", width=200, anchor='c')
        tree.heading("DNo", text='DNo')
        tree.heading("Name", text='Name')
        tree.heading("Phone", text='Phone')
        tree.heading("Job", text='Job')
        tree.heading("City", text='City')
        r = c.fetchall()
        for i in r:
            tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3]))
        Button(show2_window, text='CLOSE', bg='white', font=('abel', 12), border=0,
               command=lambda: [show2_window.destroy(), main_window.deiconify()]).place(x=5, y=70)


def show3():
    global name
    nam = name.get()

    che = 0
    saf = 0
    c.execute('SELECT NAME FROM DIRECTORY')
    ifin = []
    r = c.fetchall()
    for i in r:
        for j in i:
            ifin.append(j[0])
    if nam not in ifin:
        che = 1
        messagebox.showerror(title='Geo', message='Name not in table')
        searchname1()
    for i in nam:
        if i.isalpha() == False and i != ' ':
            saf = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Name cant have special characters or numbers')
        searchname1()
    if saf == 0 and che == 0:
        show_window = Toplevel(main_window)
        show_window.geometry('950x200')
        c.execute('SELECT * FROM ADDRESS')
        r = c.fetchall()
        if not r:
            c.execute('SELECT * FROM DIRECTORY WHERE NAME LIKE "{}%"'.format(nam))
            tree = ttk.Treeview(show_window, selectmode='browse')
            tree.pack()
            tree['columns'] = ('DNo', 'Name', 'Phone', 'Job')
            tree['show'] = 'headings'
            tree.column("DNo", width=200, anchor='c')
            tree.column("Name", width=200, anchor='c')
            tree.column("Phone", width=200, anchor='c')
            tree.column("Job", width=200, anchor='c')
            tree.heading("DNo", text='DNo')
            tree.heading("Name", text='Name')
            tree.heading("Phone", text='Phone')
            tree.heading("Job", text='Job')
            r = c.fetchall()
            for i in r:
                tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3]))
        else:
            c.execute(
                'SELECT D.DNO,NAME,PHONE_NO,JOB,HNO,CITY,PINCODE FROM DIRECTORY D,ADDRESS A WHERE NAME LIKE "{}%"'.format(
                    nam))
            tree = ttk.Treeview(show_window, selectmode='browse')
            tree.grid(row=1, column=1, padx=20, pady=20)
            tree['columns'] = ('DNo', 'Name', 'Phone', 'Job', 'HNo', 'City', 'Pincode')
            tree['show'] = 'headings'
            tree.column("DNo", width=200, anchor='c')
            tree.column("Name", width=200, anchor='c')
            tree.column("Phone", width=200, anchor='c')
            tree.column("Job", width=200, anchor='c')
            tree.column("HNo", width=200, anchor='c')
            tree.column("City", width=200, anchor='c')
            tree.column("Pincode", width=200, anchor='c')
            tree.heading("DNo", text='DNo')
            tree.heading("Name", text='Name')
            tree.heading("Phone", text='Phone')
            tree.heading("Job", text='Job')
            tree.heading("HNo", text='HNo')
            tree.heading("City", text='City')
            tree.heading("Pincode", text='Pincode')
            r = c.fetchall()
            for i in r:
                tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
            c.execute('SELECT * FROM DIRECTORY')
            r = c.fetchall()
            try:

                for i in r:
                    tree.insert('', 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3], 'NULL', 'NULL', 'NULL'))
            except:
                dfnaoiwd = 1

        Button(show_window, text='close', font=('abel', 15), border=0,
               command=lambda: [show_window.destroy(), main_window.deiconify()]).place(x=850, y=30)


def update():
    global dno
    update_window = Toplevel(main_window)
    update_window.geometry('400x300')
    update_window.resizable(False, False)
    main_window.withdraw()
    dno = StringVar()
    Label(update_window, bg='#bc8dbb', height=1000, width=1000).pack()
    Label(update_window, text='DNo.:', font=('abel', 15), bg='#e0a8c5').place(x=80, y=100)
    dno_entry = Entry(update_window, text='dno', textvariable=dno, font=('abel', 15), border=1, bg='#e0a8c5')
    dno_entry.place(x=135, y=100)
    Button(update_window, text='ENTER', bg='#e0a8c5', width=20,
           command=lambda: [update_window.destroy(), updating()]).place(x=40, y=170)
    Button(update_window, text='CLOSE', bg='#e0a8c5', width=20,
           command=lambda: [update_window.destroy(), main_window.deiconify()]).place(x=200, y=170)


def updating():
    global dno, name, phone, job, dirno
    updating_window = Toplevel(main_window)
    updating_window.geometry('500x300')
    dirno = dno.get()
    saf = 0
    che = 0
    for i in dirno:
        if not i.isnumeric():
            saf = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Dno can only have numbers')
        che = 1
        update()
        updating_window.destroy()
    if len(dirno) != 5:
        messagebox.showerror(title='Geo', message='invalid dno must be 5 digits')
        che = 1
        update()
        updating_window.destroy()
    c.execute('SELECT DNO FROM DIRECTORY')
    ifin = []
    r = c.fetchall()
    for i in r:
        for j in i:
            ifin.append(j)
    if int(dirno) not in ifin:
        messagebox.showerror(title='Geo', message='Dno not in table')
        updating_window.destroy()
        update()
        che = 1
    if che == 0:
        Label(updating_window, bg='#bc8dbb', height=1000, width=1000).pack()
        c.execute(
            'SELECT NAME,PHONE_NO,JOB,HNO,AREA,CITY,PINCODE FROM DIRECTORY D,ADDRESS A WHERE D.DNO=%s AND D.DNO=A.DNO',
            (dirno,))
        r = c.fetchall()
        n = r[0][0]
        p = r[0][1]
        j = r[0][2]
        h = r[0][3]
        a = r[0][4]
        c = r[0][5]
        pin = r[0][7]
        name = StringVar()
        phone = StringVar()
        job = StringVar()
        hno = StringVar()
        ar = StringVar()
        ci = StringVar()
        pi = StringVar()
        name_entry = Entry(updating_window, textvariable=name, font=('abel', 20), bg='#e0a8c5', border=1)
        name_entry.place(x=150, y=50)
        name_entry.insert(0, n)
        Label(updating_window, text='NAME', font=('abel', 17), bg='#e0a8c5').place(x=75, y=50)
        phone_entry = Entry(updating_window, textvariable=phone, font=('abel', 20), bg='#e0a8c5', border=1)
        phone_entry.place(x=150, y=100)
        phone_entry.insert(0, p)
        Label(updating_window, text='PHONE', font=('abel', 17), bg='#e0a8c5').place(x=75, y=100)
        job_entry = Entry(updating_window, textvariable=job, font=('abel', 20), bg='#e0a8c5', border=1)
        job_entry.place(x=150, y=150)
        job_entry.insert(0, j)
        Label(updating_window, text='JOB', font=('abel', 17), bg='#e0a8c5').place(x=75, y=150)
        hno_entry = Entry(updating_window, textvariable=hno, font=('abel', 20), bg='#e0a8c5', border=1)
        hno_entry.place(x=150, y=200)
        hno_entry.insert(0, h)
        Label(updating_window, text='HNO', font=('abel', 17), bg='#e0a8c5').place(x=75, y=200)
        area_entry = Entry(updating_window, textvariable=ar, font=('abel', 20), bg='#e0a8c5', border=1)
        area_entry.place(x=150, y=250)
        area_entry.insert(0, a)
        Label(updating_window, text='AREA', font=('abel', 17), bg='#e0a8c5').place(x=75, y=250)
        city_entry = Entry(updating_window, textvariable=ci, font=('abel', 20), bg='#e0a8c5', border=1)
        city_entry.place(x=150, y=300)
        city_entry.insert(0, c)
        Label(updating_window, text='CITY', font=('abel', 17), bg='#e0a8c5').place(x=75, y=300)
        pin_entry = Entry(updating_window, textvariable=pi, font=('abel', 20), bg='#e0a8c5', border=1)
        pin_entry.place(x=150, y=150)
        pin_entry.insert(0, pin)
        Label(updating_window, text='PINCODE', font=('abel', 17), bg='#e0a8c5').place(x=75, y=150)
        Button(updating_window, text='UPDATE', width=20, bg='#e0a8c5',
               command=lambda: [updation(), update(), updating_window.destroy()]).place(x=250, y=220)
        Button(updating_window, text='CLOSE', bg='#e0a8c5', width=20,
               command=lambda: [updating_window.destroy(), main_window.deiconify()]).place(x=100, y=220)


def updation():
    global name, phone, job, dirno, hno, ar, pi, ci
    nam = name.get()
    ph = phone.get()
    jb = job.get()
    hn = hno.get()
    are = ar.get()
    pin = pi.get()
    cit = ci.get()
    che = 0
    saf = 0
    for i in nam:
        if i.isalpha() == False and i != ' ':
            saf = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Name cant have special charecters or numbers')
    saf = 0
    for i in jb:
        if not i.isalpha():
            saf = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Job cant have numbers or special charecters')
    saf = 0
    for i in ph:
        if not i.isnumeric():
            saf = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Phone number can only have numbers')

    if len(ph) != 10:
        messagebox.showerror(title='Geo', message='invalid phone no, must be 10 digits')
        che = 1

    if che != 1:
        c.execute('UPDATE DIRECTORY SET NAME=%s,PHONE_NO=%s,JOB=%s WHERE DNO=%s', (nam, ph, jb, dirno))
        c.execute('UPDATE ADDRESS SET HNO=%s,AREA=%s,CITY=%s,PINCODE=%s WHERE DNO=%s', (hn, are, cit, pin, dirno))
        con.commit()
        messagebox.showinfo(title='geo', message='updated')


def deletion():
    global dno
    delete_window = Toplevel(main_window)
    delete_window.geometry('400x300')
    delete_window.resizable(False, False)
    main_window.withdraw()
    dno = StringVar()
    Label(delete_window, bg='#bc8dbb', height=1000, width=1000).pack()
    Label(delete_window, text='DNo.:', font=('abel', 15), bg='#e0a8c5').place(x=80, y=100)
    dno_entry = Entry(delete_window, text='dno', textvariable=dno, font=('abel', 15), border=1, bg='#e0a8c5')
    dno_entry.place(x=135, y=100)
    Button(delete_window, text='ENTER', bg='#e0a8c5', width=20, command=lambda: [delete()]).place(x=40, y=170)
    Button(delete_window, text='CLOSE', bg='#e0a8c5', width=20,
           command=lambda: [delete_window.destroy(), main_window.deiconify()]).place(x=200, y=170)


def delete():
    global dno
    dirno = dno.get()
    che = 0
    saf = 0
    for i in dirno:
        if not i.isnumeric():
            saf = 1
    if saf == 1:
        messagebox.showerror(title='Geo', message='Dno can only have numbers')
        che = 1
    if len(dirno) > 5:
        messagebox.showerror(title='Geo', message='invalid dno must be 5 or less digits')
        che = 1
    c.execute('SELECT DNO FROM DIRECTORY')
    ifin = []
    r = c.fetchall()
    for i in r:
        for j in i:
            ifin.append(j)
    saf = 1
    for i in range(len(ifin)):
        if dirno == str(ifin[i]):
            saf = 0

    if saf == 1:
        messagebox.showerror(title='Geo', message='Dno not in table')
        che = 1

    if che == 0:
        messagebox.showinfo(title='geo', message='deleted')
        c.execute('DELETE FROM DIRECTORY WHERE DNO=%s', (dirno,))
        con.commit()


def bi():
    f = open('text/about.txt', 'w')
    che = 0
    f.write(
        'Geo is a telecommunication service company which provides telecommunication services to its customers.\nIt uses a structured query language to store vast amount of records of its customers.\nIt uses GUI and visually rich application called Geo Enterprises which aids in accessing these tables.\nGeo enterprises connects to 2 tables,\nnamely "Directories" and "Address" which store personal and postal address of the customers respectively.\nUsing this app, an employee can add, delete, update or search using constraints.\nThis app helps in easily manipulating and using data and is efficient in mangement of immense amount of data within seconds.')
    f.close()
    f = open('text/about.txt', 'r')
    s = f.read()
    bi_window = Toplevel(main_window)
    l = Label(bi_window, text=s, font=('Arial', 14), bg='#e0a8c5').pack()
    Button(bi_window, text='CLOSE', bg='#e0a8c5', width=20, command=lambda: [bi_window.destroy()]).pack()
    f.close()


def canvases(images, w, h):
    photo = Image.open(images)
    photo1 = photo.resize((w, h), Image.Resampling.LANCZOS)
    photo2 = ImageTk.PhotoImage(photo1)
    canvas = Canvas(main_window, width='%d' % w, height='%d' % h)
    canvas.grid(row=0, column=0)
    canvas.grid_propagate(False)
    canvas.create_image(0, 0, anchor=NW, image=photo2)
    canvas.image = photo2
    return canvas


# Login page------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pyglet.font.add_file('Fonts/FontsFree-Net-Abel-Regular.ttf')
t, i = 0, 0
login_window = Tk(className=" Geo Enterprises")
login_window.geometry("1079x720")
login_window.resizable(False, False)

#vars
username = StringVar()
password = StringVar()

#labels
loginimage = PhotoImage(file="images/1079x720.png")
Label(login_window, image=loginimage).pack()
Label(login_window, width=50, height=30, bg='white').place(x=350, y=200)
Label(login_window, text='Login', bg='white', font=('abel', 40)).place(x=465, y=220)

#username enrty
username_entry = Entry(login_window, font=('abel', 15), border=0, width=20, bg='white', textvariable=username)
username_entry.place(x=390, y=350)
username_entry.focus()
Frame(login_window, width=290, height=2, bg='black').place(x=380, y=375)

#password entry
password_entry = Entry(login_window, font=('abel', 15), border=0, width=20, bg='white', textvariable=password, show='*')
password_entry.place(x=390, y=450)
Frame(login_window, width=290, height=2, bg='black').place(x=380, y=475)

#button to login
Button(login_window, width=20, text='Login', font='abel', border=0, bg='light grey', command=checking,
       cursor="hand2").place(x=450, y=575)

login_window.mainloop()

if t != 1:
    exit()
#sql-------------------------------------------------------------------------------------------------------
con = ms.connect(host='localhost', user='root', password='mat24RUDR', database='Directory')
if not con.is_connected():
    print('not connected')
    exit()
c = con.cursor()
x = 'CREATE TABLE IF NOT EXISTS DIRECTORY(DNO INT(5) NOT NULL PRIMARY KEY,NAME VARCHAR(30),PHONE_NO CHAR(10),JOB VARCHAR(30))'
c.execute(x)
x = 'CREATE TABLE IF NOT EXISTS ADDRESS(AID INT(5) NOT NULL PRIMARY KEY,HNO VARCHAR(4),AREA VARCHAR(30),CITY VARCHAR(30),PINCODE INT(6),DNO INT(5),CONSTRAINT FK FOREIGN KEY (DNO) REFERENCES DIRECTORY(DNO) ON DELETE CASCADE ON UPDATE CASCADE  )'
c.execute(x)
#creating window----------------------------------------------------------------------------------------------------------------------------
main_window = Tk(className='Geo enterprises')
#width=main_window.winfo_screenwidth()
#height=main_window.winfo_screenheight()
#m=str(width)+'x'+str(height)
#main_window.geometry("1500x940")#
#main_window.resizable(False,False)

IMG1 = "images/geo.png"

w = main_window.winfo_screenwidth()
h = main_window.winfo_screenheight()
canvas = canvases(IMG1, w, h)

#Labels
backimage = PhotoImage(file="images/geo.png")
Label(canvas, image=backimage).pack()

#options
#lbl_title = Label(canvas, text = "GEO ENTERPRISES", font=('Papyrus', 50,'bold', ),bg='PINK2', fg='GREY5')
#lbl_title.place(x=370,y=40)
Button(canvas, width=45, height=3, font=('abel', 15), text='INSERTING RECORDS(Directory)', border=1, cursor='hand2',
       command=insertingdir, bg='#b782f1').place(x=200, y=160)
Button(canvas, width=45, height=3, font=('abel', 15), text='INSERTING RECORDS(Address)', border=1, cursor='hand2',
       bg='#b782f1', command=insertingadd).place(x=200, y=285)
Button(canvas, width=45, height=3, font=('abel', 15), text='DISPLAY', border=1, cursor='hand2', bg='#b782f1',
       command=display).place(x=200, y=405)
Button(canvas, width=45, height=3, font=('abel', 15), text='SEARCH BY NAME', border=1, cursor='hand2', bg='#b782f1',
       command=searchname).place(x=200, y=520)
Button(canvas, width=45, height=3, font=('abel', 15), text='SEARCH BY CITY', border=1, cursor='hand2', bg='#9772b1',
       command=searchcity).place(x=670, y=160)
Button(canvas, width=45, height=3, font=('abel', 15), text='SEARCH BY 1ST LETTER OF NAME', border=1, cursor='hand2',
       bg='#9772b1', command=searchname1).place(x=670, y=285)
Button(canvas, width=45, height=3, font=('abel', 15), text='UPDATE', border=1, cursor='hand2', bg='#9772b1',
       command=update).place(x=670, y=405)
Button(canvas, width=45, height=3, font=('abel', 15), text='DELETE', border=1, cursor='hand2', bg='#9772b1',
       command=deletion).place(x=670, y=520)
Button(canvas, width=45, height=3, font=('abel', 15), text='LOGOUT', border=1, cursor='hand2', bg='#b782f1',
       command=lambda: [main_window.destroy(), call(['python', 'main.py'])]).place(x=200, y=635)
Button(canvas, width=45, height=3, font=('abel', 15), text='ABOUT', border=1, cursor='hand2', bg='#9772b1',
       command=bi).place(x=670, y=635)
main_window.mainloop()
