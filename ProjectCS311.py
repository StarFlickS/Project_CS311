'''
Project CS311: Program for reporting COVID-19 cases and more
Made by: Purin Singkaew, Niti
'''

'''
Version des:
Version = Pre Release
v1: Making windows frames and widgets, prepare for more advance features, added login page
v2: Added Login feature, connect to database, registration, forget password
v3: Add ReportCovid19 In Thailand Page
'''

from sys import platform
import random
import smtplib
from email.message import EmailMessage
import webbrowser
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkmacosx import Button

def CreatedConnection():
    global conn, cursor
    conn = sqlite3.connect("projectcs311_database.db")
    cursor = conn.cursor()


def CreateWindows():
    root = Tk()
    root.title("Project CS311: Program for reporting COVID-19 cases and more")
    x = root.winfo_screenwidth() / 2 - w / 2
    y = root.winfo_screenheight() / 2 - h / 2
    root.geometry("%dx%d+%d+%d" %(w,h,x,y))
    root.rowconfigure((0,1), weight=1)
    root.columnconfigure((0), weight=1)

    return root


def LoginPage(root):
    global gmail_ent, password_ent, header
    top = Frame(root, bg="#daeffd")
    top.rowconfigure((0,1), weight=1)
    top.columnconfigure((0,1), weight=1)
    top.grid(row=0, column=0, sticky="news")

    bottom = Frame(root, bg="#808cff")
    bottom.grid(row=1, column=0, sticky="news")

    login_frm = Frame(root, bg="white")
    login_frm.rowconfigure((0,1), weight=1)
    login_frm.columnconfigure(0, weight=1)
    login_frm.grid(row=0, rowspan=2, column=0, sticky="news", padx=50, pady=150)

    ent_frm = Frame(login_frm, bg="white")
    ent_frm.rowconfigure((0,1), weight=1)
    ent_frm.columnconfigure(0, weight=1)
    ent_frm.grid(row=0, column=0, sticky="news")

    bottom_frm = Frame(login_frm, bg="white")
    bottom_frm.rowconfigure((0,1), weight=1)
    bottom_frm.columnconfigure((0,1), weight=1)
    bottom_frm.grid(row=1, column=0, sticky="news")

    # * Header Sign in
    header = Label(top, text="Sign In", bg="#daeffd", fg="#6f6767", font="verdana 20 bold")
    header.grid(row=0, column=0, sticky='w', padx=45, pady=50)

    # * Gmail entry
    Label(ent_frm, text="Gmail:", bg="white", fg="black", font="verdana 20 bold").grid(row=0, column=0, sticky='nw', padx=30)
    gmail_ent = Entry(ent_frm, textvariable=gmail_spy, bg="#e9e4e4", width=20, fg="black", font="verdana 20", justify=LEFT, borderwidth=0, highlightthickness=0)
    gmail_ent.grid(row=0, column=0)

    # * Password entry
    Label(ent_frm, text="Password:", bg="white", fg="black", font="verdana 20 bold").grid(row=1, column=0, sticky='nw', padx=30)
    password_ent = Entry(ent_frm, textvariable=pwd_spy, bg="#e9e4e4", width=20, fg="black", font="verdana 20", justify=LEFT, borderwidth=0, highlightthickness=0, show="●")
    password_ent.grid(row=1, column=0)

    # * Login Button
    Button(bottom_frm, text="Login", fg="black", font="verdana 15 bold",bg="#808cff", borderless=1, command=loginclicked).grid(row=0, column=0, columnspan=2)

    # * Registor Button
    Button(bottom_frm, text="Registor", fg="black", font="verdana 15 bold", bg="white", borderless=1, command=RegistrationPage).grid(row=1, column=0)

    # * Forget password button
    Button(bottom_frm, text="Forget password?", fg="black", font="verdana 15 bold", bg="white", borderless=1, command=ForgetPasswordPage).grid(row=1, column=1)

    gmail_ent.focus_force()


def RegistrationPage():
    global rg_frm, fname_ent, lname_ent, gmail_ent, phone_ent, pwd_ent, cfpwd_ent
    header["text"] = "Register"
    rg_frm = Frame(root, bg="red")
    rg_frm.rowconfigure((0,1), weight=1)
    rg_frm.columnconfigure(0, weight=1)
    rg_frm.grid(row=0, rowspan=2, column=0, sticky="news", padx=50, pady=150)

    ent_frm = Frame(rg_frm, bg="white")
    ent_frm.rowconfigure((0,1,2,3,4,5,6), weight=1)
    ent_frm.columnconfigure((0,1), weight=1)
    ent_frm.grid(row=0, column=0, sticky="news")

    btn_frm = Frame(rg_frm, bg="white")
    btn_frm.rowconfigure(0, weight=1)
    btn_frm.columnconfigure((0,1), weight=1)
    btn_frm.grid(row=1, column=0, sticky="news")

    # * Ent frame widgets
    # ? First Name
    Label(ent_frm, text="First Name:", bg="white", fg="black", font="verdana 15").grid(row=0, column=0, sticky='e')
    fname_ent = Entry(ent_frm, bg="#e9e4e4", fg="black", font="verdana 15", width=20, textvariable=rg_fname_spy)
    fname_ent.grid(row=0, column=1, sticky='w')

    # ? Last Name
    Label(ent_frm, text="Last Name:", bg="white", fg="black", font="verdana 15").grid(row=1, column=0, sticky='e')
    lname_ent = Entry(ent_frm, bg="#e9e4e4", fg="black", font="verdana 15", width=20, textvariable=rg_lname_spy)
    lname_ent.grid(row=1, column=1, sticky='w')

    # ? Gmail
    Label(ent_frm, text="Gmail:", bg="white", fg="black", font="verdana 15").grid(row=2, column=0, sticky='e')
    gmail_ent = Entry(ent_frm, bg="#e9e4e4", fg="black", font="verdana 15", width=20, textvariable=rg_gmail_spy)
    gmail_ent.grid(row=2, column=1, sticky='w')

    # ? Birth day
    Label(ent_frm, text="DD/MM/YYYY:", bg="white", fg="black", font="verdana 15").grid(row=3, column=0, sticky='e')
    
    day_list = [x for x in range(1,32)]
    month_list = [x for x in range(1, 13)]
    year_list = [x for x in range(1980, 2023)]
    rg_bd_d_spy.set(day_list[0])
    rg_bd_m_spy.set(month_list[0])
    rg_bd_y_spy.set(year_list[-1])
    
    OptionMenu(ent_frm, rg_bd_d_spy, *day_list).grid(row=3, column=1, sticky='w')
    Label(ent_frm, text="/", bg="white", fg="black", font="verdana 15").grid(row=3, column=1, sticky='w', padx=54)
    OptionMenu(ent_frm, rg_bd_m_spy, *month_list).grid(row=3, column=1, sticky='w',padx=70)
    Label(ent_frm, text="/", bg="white", fg="black", font="verdana 15").grid(row=3, column=1, sticky='e', padx=90)
    OptionMenu(ent_frm, rg_bd_y_spy, *year_list).grid(row=3, column=1, sticky='e', padx=10)

    # ? Phone number
    Label(ent_frm, text="Phone Number:", bg="white", fg="black", font="verdana 15").grid(row=4, column=0, sticky='e')
    phone_ent = Entry(ent_frm, bg="#e9e4e4", fg="black", font="verdana 15", width=20, textvariable=rg_phone_spy)
    phone_ent.grid(row=4, column=1, sticky='w')

    # ? Password
    Label(ent_frm, text="Password:", bg="white", fg="black", font="verdana 15").grid(row=5, column=0, sticky='e')
    pwd_ent = Entry(ent_frm, bg="#e9e4e4", fg="black", font="verdana 15", width=20, show="●", textvariable=rg_pwd_spy)
    pwd_ent.grid(row=5, column=1, sticky='w')

    Label(ent_frm, text="Confirm Password:", bg="white", fg="black", font="verdana 15").grid(row=6, column=0, sticky='e')
    cfpwd_ent = Entry(ent_frm, bg="#e9e4e4", fg="black", font="verdana 15", width=20, show="●", textvariable=rg_cfpwd_spy)
    cfpwd_ent.grid(row=6, column=1, sticky='w')

    # * Button Frame
    Button(btn_frm, text="Cancel", bg="lightgray", fg="black", font="verdana 22 bold", borderless=1, command=ExitRegistrationPage).grid(row=0, column=0)
    Button(btn_frm, text="Sign Up", bg="lightgreen", fg="black", font="verdana 22 bold", borderless=1, command=SignUp_clicked).grid(row=0, column=1)

    fname_ent.focus_force()


def ForgetPasswordPage():
    global fg_frm, fg_gmail_ent, fg_page1_frm, fg_page2_frm, fg_page3_frm
    header["text"] = "Forget Password"
    fg_frm = Frame(root, bg="red")
    fg_frm.rowconfigure(0, weight=1)
    fg_frm.columnconfigure(0, weight=1)
    fg_frm.grid(row=0, rowspan=2, column=0, sticky="news", padx=50, pady=150)

    fg_page1_frm = Frame(fg_frm, bg="white")
    fg_page1_frm.rowconfigure((0,1), weight=1)
    fg_page1_frm.columnconfigure((0,1), weight=1)
    fg_page1_frm.grid(row=0, column=0, sticky="news")

    fg_page2_frm = Frame(fg_frm, bg="white")
    fg_page2_frm.rowconfigure((0,1), weight=1)
    fg_page2_frm.columnconfigure((0,1), weight=1)

    fg_page3_frm = Frame(fg_frm, bg="white")
    fg_page3_frm.rowconfigure((0,1,2), weight=1)
    fg_page3_frm.columnconfigure((0,1), weight=1)

    # * Ent Frame widgets
    Label(fg_page1_frm, text="Enter your Gmail:", bg="white", fg="black", font="verdana 15").grid(row=0, column=0, sticky='e')
    fg_gmail_ent = Entry(fg_page1_frm, bg="lightgray", fg="black", font="verdana 15", textvariable=fg_gmail_spy)
    fg_gmail_ent.grid(row=0, column=1, sticky='w')
    
    Button(fg_page1_frm, text="Sent Code", bg="lightgreen", fg="black", font="verdana 20 bold", borderless=1, command=SentCode_clicked).grid(row=1, column=1)
    Button(fg_page1_frm, text="Cancel", bg="lightgray", fg="black", font="verdana 20 bold", borderless=1, command=lambda:ExitForgerPasswordPage(1)).grid(row=1, column=0)
    
    fg_gmail_ent.focus_force()


def SentCode_clicked():
    global verif_code, verif_ent
    if fg_gmail_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your gmail.")
        fg_gmail_ent.focus_force()
    else:
        text = fg_gmail_ent.get()
        rest = abs(len(text) - 10)
        if text[rest::] != "@gmail.com":
            messagebox.showwarning("Admin:", "Please end your gmail with @gmail.com")
        else:
            sql = "SELECT * FROM users WHERE user_gmail = ?"
            cursor.execute(sql, [fg_gmail_spy.get()])
            res = cursor.fetchone()
            if res:
                verif_code = ""
                for i in range(6):
                    verif_code += str(random.randint(0,9))
                msg = EmailMessage()
                msg["Subject"] = "Password Recovery"
                msg["From"] = "Project CS311 Team"
                msg["To"] = fg_gmail_spy.get()
                context = "Your verification code for change password is %s" %(verif_code)
                msg.set_content(context)
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("projectcs311@gmail.com", "1.3boxbox")
                server.send_message(msg)
                server.quit()
                messagebox.showinfo("Admin:", "Verification code has been sent to your email.")
                
                fg_page2_frm.grid(row=0, column=0, sticky="news")
                Label(fg_page2_frm, text="Verification code:", bg="white", fg="black", font="verdana 15").grid(row=0, column=0, sticky='e')
                verif_ent = Entry(fg_page2_frm, bg="lightgray", fg="black", font="verdana 15", textvariable=verif_spy)
                verif_ent.grid(row=0, column=1, sticky='w')

                Button(fg_page2_frm, text="Verify code", bg="lightgreen", fg="black", font="verdana 22 bold", borderless=1, command=Verify_clicked).grid(row=1, column=1)
                Button(fg_page2_frm, text="Cancel", bg="lightgray", fg="black", font="verdana 22 bold", borderless=1, command=lambda:ExitForgerPasswordPage(2)).grid(row=1, column=0)

                verif_ent.focus_force()
            else:
                messagebox.showerror("Admin:", "This gmail hasn't sign up yet, please sign up before continue.")
                fg_gmail_spy.set("")
                fg_gmail_ent.focus_force()


def SignUp_clicked():
    if rg_fname_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your First Name.")
        fname_ent.focus_force()
    elif rg_lname_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your Last Name.")
        lname_ent.focus_force()
    elif rg_gmail_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your Gmail.")
        gmail_ent.focus_force()
    elif rg_phone_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your Phone Number.")
        phone_ent.focus_force()
    elif rg_pwd_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your Password.")
        pwd_ent.focus_force()
    elif rg_cfpwd_spy.get() == "":
        messagebox.showwarning("Admin:", "Please Confirm your Password.")
        cfpwd_ent.focus_force()
    elif rg_pwd_spy.get() != rg_cfpwd_spy.get():
        messagebox.showwarning("Admin:", "Password and Confirm Password are incorrect, please try again.")
        cfpwd_ent.delete(0, END)
        cfpwd_ent.focus_force()
    else:
        text = rg_gmail_spy.get()
        rest = abs(len(text) - 10)
        if text[rest::] != "@gmail.com":
            messagebox.showwarning("Admin:", "Please end your gmail with @gmail.com")
            gmail_ent.focus_force()
        else:
            sql = "SELECT * FROM users WHERE user_gmail = ?"
            cursor.execute(sql, [rg_gmail_spy.get()])
            res = cursor.fetchone()
            if res:
                messagebox.showerror("Admin:", "This Gmail already exist, please try again.")
                gmail_ent.focus_force()
                gmail_ent.select_range(0, END)
            else:
                birth_day = ("%s/%s/%s" %(rg_bd_d_spy.get(), rg_bd_m_spy.get(), rg_bd_y_spy.get()))
                age = 2022 - rg_bd_y_spy.get()
                sql = "INSERT INTO users VALUES (?,?,?,?,?,?,?)"
                param = [rg_gmail_spy.get(), rg_pwd_spy.get(), rg_fname_spy.get(), rg_lname_spy.get(), birth_day, age, rg_phone_spy.get()]
                cursor.execute(sql, param)
                conn.commit()
                messagebox.showinfo("Admin:", "Registration Successfully.")
                ExitRegistrationPage()


def Verify_clicked():
    global fg_newpwd_ent, fg_cfnewpwd_ent
    if verif_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter Verification Code.")
        verif_ent.focus_force()
    elif verif_spy.get() != verif_code:
        messagebox.showwarning("Admin:", "This Verification code is incorrect, please try again.")
        verif_ent.focus_force()
        verif_ent.select_range(0, END)
    else:
        messagebox.showinfo("Admin:", "Verification Successfully.")
        fg_page3_frm.grid(row=0, column=0, sticky="news")

        Label(fg_page3_frm, text="New Password:", fg="black", bg="white", font="verdana 15").grid(row=0, column=0, sticky='e')
        fg_newpwd_ent = Entry(fg_page3_frm, bg="lightgray", fg="black", font="verdana 15", show="●", textvariable=fg_newpwd_spy)
        fg_newpwd_ent.grid(row=0, column=1, sticky='w')

        Label(fg_page3_frm, text="Confirm New Password:", fg="black", bg="white", font="verdana 13").grid(row=1, column=0, sticky='e')
        fg_cfnewpwd_ent = Entry(fg_page3_frm, bg="lightgray", fg="black", font="verdana 15", show="●", textvariable=fg_cfnewpwd_spy)
        fg_cfnewpwd_ent.grid(row=1, column=1, sticky='w')

        Button(fg_page3_frm, text="Cancel", bg="lightgray", fg="black", font="verdana 15 bold", command=lambda:ExitForgerPasswordPage(3), borderless=1).grid(row=2, column=0)
        Button(fg_page3_frm, text="Change Password", bg="lightgreen", fg="black", font="verdana 15 bold", command=ChangePassword_clicked, borderless=1).grid(row=2, column=1)

        fg_newpwd_ent.focus_force()


def ChangePassword_clicked():
    if fg_newpwd_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your new password.")
        fg_newpwd_ent.focus_force()
    elif fg_cfnewpwd_spy.get() == "":
        messagebox.showwarning("Admin:", "Please Confirm your new password.")
        fg_cfnewpwd_ent.focus_force()
    elif fg_newpwd_spy.get() != fg_cfnewpwd_spy.get():
        messagebox.showwarning("Admin:", "New password and Confirm new password are incorrect, please try again")
        fg_cfnewpwd_ent.focus_force()
        fg_cfnewpwd_ent.select_range(0, END)
    else:
        sql = "SELECT user_pwd FROM users WHERE user_gmail = ?"
        cursor.execute(sql, [fg_gmail_spy.get()])
        res = cursor.fetchone()
        if res[0] == fg_newpwd_spy.get():
            messagebox.showerror("Admin:", "This password is already used.")
            fg_newpwd_spy.set("")
            fg_cfnewpwd_spy.set("")
            fg_newpwd_ent.focus_force()
        else:
            sql = "UPDATE users SET user_pwd = ? WHERE user_gmail = ?"
            cursor.execute(sql, [fg_newpwd_spy.get(), fg_gmail_spy.get()])
            conn.commit()
            messagebox.showinfo("Admin:", "Password Change Successfully.")
            fg_frm.destroy()
            fg_gmail_spy.set("")
            verif_spy.set("")
            fg_newpwd_spy.set("")
            fg_cfnewpwd_spy.set("")



def ExitRegistrationPage():
    header["text"] = "Sign In"
    rg_frm.destroy()
    rg_fname_spy.set("")
    rg_lname_spy.set("")
    rg_gmail_spy.set("")
    rg_bd_d_spy.set(0)
    rg_bd_m_spy.set(0)
    rg_bd_y_spy.set(0)
    rg_phone_spy.set("")
    rg_pwd_spy.set("")
    rg_cfpwd_spy.set("")


def ExitForgerPasswordPage(page: int):
    if page == 1:
        header["text"] = "Sign In"
        fg_frm.destroy()
        fg_page1_frm.destroy()
    elif page == 2:
        fg_frm.destroy()
        fg_page1_frm.destroy()
        fg_page2_frm.destroy()
    elif page == 3:
        fg_frm.destroy()
        fg_page1_frm.destroy()
        fg_page2_frm.destroy()
        fg_page3_frm.destroy()
    fg_gmail_spy.set("")
    verif_spy.set("")
    fg_newpwd_spy.set("")
    fg_cfnewpwd_spy.set("")


def loginclicked():
    if gmail_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your Gmail.")
        gmail_ent.focus_force()
    else:
        if pwd_spy.get() == "":
            messagebox.showwarning("Admin:", "Please enter your Password.")
            password_ent.focus_force()
        else:
            sql = "SELECT * FROM users WHERE user_gmail = ? AND user_pwd = ?"
            cursor.execute(sql, [gmail_spy.get(), pwd_spy.get()])
            result = cursor.fetchone()
            if result:
                messagebox.showinfo("Admin:", "Login Successfully.")
            else:
                messagebox.showerror("Admin:", "Gmail or Password incorrect, please try again.")
                gmail_spy.set("")
                pwd_spy.set("")
                gmail_ent.focus_force()


def ReportCovid19THPage():
    report_th_page = Frame(root, bg="red")
    report_th_page.grid(row=0, column=0, rowspan=2, sticky="news")


if platform == "darwin":
    w = 500
    h = 650
else:
    w = 600
    h = 700

CreatedConnection()
root = CreateWindows()

# ! login spies
gmail_spy = StringVar()
pwd_spy = StringVar()

# ! regis spies
rg_fname_spy = StringVar()
rg_lname_spy = StringVar()
rg_gmail_spy = StringVar()
rg_bd_d_spy = IntVar()
rg_bd_m_spy = IntVar()
rg_bd_y_spy = IntVar()
rg_phone_spy = StringVar()
rg_pwd_spy = StringVar()
rg_cfpwd_spy = StringVar()

# ! Forget password spies
fg_gmail_spy = StringVar()
verif_spy = StringVar()
fg_newpwd_spy = StringVar()
fg_cfnewpwd_spy = StringVar()

LoginPage(root)
ReportCovid19THPage()
root.mainloop()