'''
Project CS311: Program for reporting COVID-19 cases and more
Made by: Purin Singkaew, Niti Puangsema
'''
'''
Version des:
Version = Release
Github : https://github.com/StarFlickS/Project_CS311
SSH : git@github.com:StarFlickS/Project_CS311.git
v1: Making windows frames and widgets, preparing for more advanced features, added login page
v2: Added Login feature, connect to database, registration, forget password
v3: Add ReportCovid19 In Thailand Page, Add Menu page, Add open map feature
v4: Add ReportCovid19ProvincesPage, Add chatbot
v4.1: Add CorrectRangeOfUnit fucntion
'''

from sys import platform
import random
import smtplib
from email.message import EmailMessage
from tkinter.ttk import Combobox
import requests
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
    root.title("หมอไม่พร้อม")
    x = root.winfo_screenwidth() / 2 - w / 2
    y = root.winfo_screenheight() / 2 - h / 2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.rowconfigure((0, 1), weight=1)
    root.columnconfigure((0), weight=1)

    return root


def LoginPage(root):
    global gmail_ent, password_ent, header
    top = Frame(root, bg="#daeffd")
    top.rowconfigure((0, 1), weight=1)
    top.columnconfigure((0, 1), weight=1)
    top.grid(row=0, column=0, sticky="news")

    bottom = Frame(root, bg="#808cff")
    bottom.grid(row=1, column=0, sticky="news")

    login_frm = Frame(root, bg="white")
    login_frm.rowconfigure((0, 1), weight=1)
    login_frm.columnconfigure(0, weight=1)
    login_frm.grid(row=0,
                   rowspan=2,
                   column=0,
                   sticky="news",
                   padx=50,
                   pady=150)

    ent_frm = Frame(login_frm, bg="white")
    ent_frm.rowconfigure((0, 1), weight=1)
    ent_frm.columnconfigure(0, weight=1)
    ent_frm.grid(row=0, column=0, sticky="news")

    bottom_frm = Frame(login_frm, bg="white")
    bottom_frm.rowconfigure((0, 1), weight=1)
    bottom_frm.columnconfigure((0, 1), weight=1)
    bottom_frm.grid(row=1, column=0, sticky="news")

    # * Header Sign in
    header = Label(top,
                   text="Sign In",
                   bg="#daeffd",
                   fg="#6f6767",
                   font="verdana 20 bold")
    header.grid(row=0, column=0, sticky='w', padx=45, pady=50)

    # * Gmail entry
    Label(ent_frm,
          text="Email:",
          bg="white",
          fg="black",
          font="verdana 20 bold").grid(row=0, column=0, sticky='nw', padx=30)
    gmail_ent = Entry(ent_frm,
                      textvariable=gmail_spy,
                      bg="#e9e4e4",
                      width=20,
                      fg="black",
                      font="verdana 20",
                      justify=LEFT,
                      borderwidth=0,
                      highlightthickness=0,
                      insertbackground="black")
    gmail_ent.grid(row=0, column=0)

    # * Password entry
    Label(ent_frm,
          text="Password:",
          bg="white",
          fg="black",
          font="verdana 20 bold").grid(row=1, column=0, sticky='nw', padx=30)
    password_ent = Entry(ent_frm,
                         textvariable=pwd_spy,
                         bg="#e9e4e4",
                         width=20,
                         fg="black",
                         font="verdana 20",
                         justify=LEFT,
                         borderwidth=0,
                         highlightthickness=0,
                         show="●",
                         insertbackground="black")
    password_ent.grid(row=1, column=0)

    # * Login Button
    Button(bottom_frm,
           text="Login",
           fg="black",
           font="verdana 15 bold",
           bg="#808cff",
           borderless=1,
           command=loginclicked).grid(row=0, column=0, columnspan=2)

    # * Register Button
    Button(bottom_frm,
           text="Register",
           fg="black",
           font="verdana 15 bold",
           bg="white",
           borderless=1,
           command=RegistrationPage).grid(row=1, column=0)

    # * Forget password button
    Button(bottom_frm,
           text="Forget password?",
           fg="black",
           font="verdana 15 bold",
           bg="white",
           borderless=1,
           command=ForgetPasswordPage).grid(row=1, column=1)

    gmail_ent.focus_force()


def RegistrationPage():
    global rg_frm, fname_ent, lname_ent, gmail_ent, phone_ent, pwd_ent, cfpwd_ent
    header["text"] = "Register"
    rg_frm = Frame(root, bg="red")
    rg_frm.rowconfigure((0, 1), weight=1)
    rg_frm.columnconfigure(0, weight=1)
    rg_frm.grid(row=0, rowspan=2, column=0, sticky="news", padx=50, pady=150)

    ent_frm = Frame(rg_frm, bg="white")
    ent_frm.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    ent_frm.columnconfigure((0, 1), weight=1)
    ent_frm.grid(row=0, column=0, sticky="news")

    btn_frm = Frame(rg_frm, bg="white")
    btn_frm.rowconfigure(0, weight=1)
    btn_frm.columnconfigure((0, 1), weight=1)
    btn_frm.grid(row=1, column=0, sticky="news")

    # * Ent frame widgets
    # ? First Name
    Label(ent_frm,
          text="First Name:",
          bg="white",
          fg="black",
          font="verdana 15").grid(row=0, column=0, sticky='e')
    fname_ent = Entry(ent_frm,
                      bg="#e9e4e4",
                      fg="black",
                      font="verdana 15",
                      width=20,
                      textvariable=rg_fname_spy)
    fname_ent.grid(row=0, column=1, sticky='w')

    # ? Last Name
    Label(ent_frm,
          text="Last Name:",
          bg="white",
          fg="black",
          font="verdana 15").grid(row=1, column=0, sticky='e')
    lname_ent = Entry(ent_frm,
                      bg="#e9e4e4",
                      fg="black",
                      font="verdana 15",
                      width=20,
                      textvariable=rg_lname_spy)
    lname_ent.grid(row=1, column=1, sticky='w')

    # ? Gmail
    Label(ent_frm, text="Email:", bg="white", fg="black",
          font="verdana 15").grid(row=2, column=0, sticky='e')
    gmail_ent = Entry(ent_frm,
                      bg="#e9e4e4",
                      fg="black",
                      font="verdana 15",
                      width=20,
                      textvariable=rg_gmail_spy)
    gmail_ent.grid(row=2, column=1, sticky='w')

    # ? Birth day
    Label(ent_frm,
          text="DD/MM/YYYY:",
          bg="white",
          fg="black",
          font="verdana 15").grid(row=3, column=0, sticky='e')

    day_list = [x for x in range(1, 32)]
    month_list = [x for x in range(1, 13)]
    year_list = [x for x in range(1980, 2023)]
    rg_bd_d_spy.set(day_list[0])
    rg_bd_m_spy.set(month_list[0])
    rg_bd_y_spy.set(year_list[-1])

    OptionMenu(ent_frm, rg_bd_d_spy, *day_list).grid(row=3,
                                                     column=1,
                                                     sticky='w')
    Label(ent_frm, text="/", bg="white", fg="black",
          font="verdana 15").grid(row=3, column=1, sticky='w', padx=54)
    OptionMenu(ent_frm, rg_bd_m_spy, *month_list).grid(row=3,
                                                       column=1,
                                                       sticky='w',
                                                       padx=70)
    Label(ent_frm, text="/", bg="white", fg="black",
          font="verdana 15").grid(row=3, column=1, sticky='e', padx=90)
    OptionMenu(ent_frm, rg_bd_y_spy, *year_list).grid(row=3,
                                                      column=1,
                                                      sticky='e',
                                                      padx=10)

    # ? Phone number
    Label(ent_frm,
          text="Phone Number:",
          bg="white",
          fg="black",
          font="verdana 15").grid(row=4, column=0, sticky='e')
    phone_ent = Entry(ent_frm,
                      bg="#e9e4e4",
                      fg="black",
                      font="verdana 15",
                      width=20,
                      textvariable=rg_phone_spy)
    phone_ent.grid(row=4, column=1, sticky='w')

    # ? Password
    Label(ent_frm, text="Password:", bg="white", fg="black",
          font="verdana 15").grid(row=5, column=0, sticky='e')
    pwd_ent = Entry(ent_frm,
                    bg="#e9e4e4",
                    fg="black",
                    font="verdana 15",
                    width=20,
                    show="●",
                    textvariable=rg_pwd_spy)
    pwd_ent.grid(row=5, column=1, sticky='w')

    Label(ent_frm,
          text="Confirm Password:",
          bg="white",
          fg="black",
          font="verdana 15").grid(row=6, column=0, sticky='e')
    cfpwd_ent = Entry(ent_frm,
                      bg="#e9e4e4",
                      fg="black",
                      font="verdana 15",
                      width=20,
                      show="●",
                      textvariable=rg_cfpwd_spy)
    cfpwd_ent.grid(row=6, column=1, sticky='w')

    # * Button Frame
    Button(btn_frm,
           text="Cancel",
           bg="lightgray",
           fg="black",
           font="verdana 22 bold",
           borderless=1,
           command=ExitRegistrationPage).grid(row=0, column=0)
    Button(btn_frm,
           text="Sign Up",
           bg="lightgreen",
           fg="black",
           font="verdana 22 bold",
           borderless=1,
           command=SignUp_clicked).grid(row=0, column=1)

    fname_ent.focus_force()


def ForgetPasswordPage():
    global fg_frm, fg_gmail_ent, fg_page1_frm, fg_page2_frm, fg_page3_frm
    header["text"] = "Forget Password"
    fg_frm = Frame(root, bg="red")
    fg_frm.rowconfigure(0, weight=1)
    fg_frm.columnconfigure(0, weight=1)
    fg_frm.grid(row=0, rowspan=2, column=0, sticky="news", padx=50, pady=150)

    fg_page1_frm = Frame(fg_frm, bg="white")
    fg_page1_frm.rowconfigure((0, 1), weight=1)
    fg_page1_frm.columnconfigure((0, 1), weight=1)
    fg_page1_frm.grid(row=0, column=0, sticky="news")

    fg_page2_frm = Frame(fg_frm, bg="white")
    fg_page2_frm.rowconfigure((0, 1), weight=1)
    fg_page2_frm.columnconfigure((0, 1), weight=1)

    fg_page3_frm = Frame(fg_frm, bg="white")
    fg_page3_frm.rowconfigure((0, 1, 2), weight=1)
    fg_page3_frm.columnconfigure((0, 1), weight=1)

    # * Ent Frame widgets
    Label(fg_page1_frm,
          text="Enter your Email:",
          bg="white",
          fg="black",
          font="verdana 15").grid(row=0, column=0, sticky='e')
    fg_gmail_ent = Entry(fg_page1_frm,
                         bg="lightgray",
                         fg="black",
                         font="verdana 15",
                         textvariable=fg_gmail_spy)
    fg_gmail_ent.grid(row=0, column=1, sticky='w')

    Button(fg_page1_frm,
           text="Sent Code",
           bg="lightgreen",
           fg="black",
           font="verdana 20 bold",
           borderless=1,
           command=SentCode_clicked).grid(row=1, column=1)
    Button(fg_page1_frm,
           text="Cancel",
           bg="lightgray",
           fg="black",
           font="verdana 20 bold",
           borderless=1,
           command=lambda: ExitForgerPasswordPage(1)).grid(row=1, column=0)

    fg_gmail_ent.focus_force()


def SentCode_clicked():
    global verif_code, verif_ent
    if fg_gmail_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your Email.")
        fg_gmail_ent.focus_force()
    else:
        text = fg_gmail_ent.get()
        rest = abs(len(text) - 10)
        if text[rest::] != "@gmail.com" and text[rest - 1::] != "@bumail.net":
            messagebox.showwarning(
                "Admin:",
                "Please end your Email with @gmail.com or @bumail.net")
            fg_gmail_ent.focus()
            fg_gmail_ent.select_range(0, END)
        else:
            sql = "SELECT * FROM users WHERE user_gmail = ?"
            cursor.execute(sql, [fg_gmail_spy.get()])
            res = cursor.fetchone()
            if res:
                verif_code = ""
                for i in range(6):
                    verif_code += str(random.randint(0, 9))
                msg = EmailMessage()
                msg["Subject"] = "Password Recovery"
                msg["From"] = "Project CS311 Team"
                msg["To"] = fg_gmail_spy.get()
                context = "Your verification code for change password is %s" % (
                    verif_code)
                msg.set_content(context)
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("projectcs311@gmail.com", "pedzyf-2vycne-semTam")
                server.send_message(msg)
                server.quit()
                messagebox.showinfo(
                    "Admin:", "Verification code has been sent to your email.")

                fg_page2_frm.grid(row=0, column=0, sticky="news")
                Label(fg_page2_frm,
                      text="Verification code:",
                      bg="white",
                      fg="black",
                      font="verdana 15").grid(row=0, column=0, sticky='e')
                verif_ent = Entry(fg_page2_frm,
                                  bg="lightgray",
                                  fg="black",
                                  font="verdana 15",
                                  textvariable=verif_spy)
                verif_ent.grid(row=0, column=1, sticky='w')

                Button(fg_page2_frm,
                       text="Verify code",
                       bg="lightgreen",
                       fg="black",
                       font="verdana 22 bold",
                       borderless=1,
                       command=Verify_clicked).grid(row=1, column=1)
                Button(fg_page2_frm,
                       text="Cancel",
                       bg="lightgray",
                       fg="black",
                       font="verdana 22 bold",
                       borderless=1,
                       command=lambda: ExitForgerPasswordPage(2)).grid(
                           row=1, column=0)

                verif_ent.focus_force()
            else:
                messagebox.showerror(
                    "Admin:",
                    "This Email hasn't sign up yet, please sign up before continue."
                )
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
        messagebox.showwarning("Admin:", "Please enter your Email.")
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
        messagebox.showwarning(
            "Admin:",
            "Password and Confirm Password are incorrect, please try again.")
        cfpwd_ent.delete(0, END)
        cfpwd_ent.focus_force()
    else:
        text = rg_gmail_spy.get()
        rest = abs(len(text) - 10)
        if text[rest::] != "@gmail.com" and text[rest - 1::] != "@bumail.net":
            messagebox.showwarning(
                "Admin:",
                "Please end your Email with @gmail.com or @bumail.net")
            gmail_ent.focus_force()
        else:
            sql = "SELECT * FROM users WHERE user_gmail = ?"
            cursor.execute(sql, [rg_gmail_spy.get()])
            res = cursor.fetchone()
            if res:
                messagebox.showerror(
                    "Admin:", "This Email already exist, please try again.")
                gmail_ent.focus_force()
                gmail_ent.select_range(0, END)
            else:
                birth_day = (
                    "%s/%s/%s" %
                    (rg_bd_d_spy.get(), rg_bd_m_spy.get(), rg_bd_y_spy.get()))
                age = 2022 - rg_bd_y_spy.get()
                sql = "INSERT INTO users VALUES (?,?,?,?,?,?,?)"
                param = [
                    rg_gmail_spy.get(),
                    rg_pwd_spy.get(),
                    rg_fname_spy.get(),
                    rg_lname_spy.get(), birth_day, age,
                    rg_phone_spy.get()
                ]
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
        messagebox.showwarning(
            "Admin:", "This Verification code is incorrect, please try again.")
        verif_ent.focus_force()
        verif_ent.select_range(0, END)
    else:
        messagebox.showinfo("Admin:", "Verification Successfully.")
        fg_page3_frm.grid(row=0, column=0, sticky="news")

        Label(fg_page3_frm,
              text="New Password:",
              fg="black",
              bg="white",
              font="verdana 15").grid(row=0, column=0, sticky='e')
        fg_newpwd_ent = Entry(fg_page3_frm,
                              bg="lightgray",
                              fg="black",
                              font="verdana 15",
                              show="●",
                              textvariable=fg_newpwd_spy)
        fg_newpwd_ent.grid(row=0, column=1, sticky='w')

        Label(fg_page3_frm,
              text="Confirm New Password:",
              fg="black",
              bg="white",
              font="verdana 13").grid(row=1, column=0, sticky='e')
        fg_cfnewpwd_ent = Entry(fg_page3_frm,
                                bg="lightgray",
                                fg="black",
                                font="verdana 15",
                                show="●",
                                textvariable=fg_cfnewpwd_spy)
        fg_cfnewpwd_ent.grid(row=1, column=1, sticky='w')

        Button(fg_page3_frm,
               text="Cancel",
               bg="lightgray",
               fg="black",
               font="verdana 15 bold",
               command=lambda: ExitForgerPasswordPage(3),
               borderless=1).grid(row=2, column=0)
        Button(fg_page3_frm,
               text="Change Password",
               bg="lightgreen",
               fg="black",
               font="verdana 15 bold",
               command=ChangePassword_clicked,
               borderless=1).grid(row=2, column=1)

        fg_newpwd_ent.focus_force()


def ChangePassword_clicked():
    if fg_newpwd_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your new password.")
        fg_newpwd_ent.focus_force()
    elif fg_cfnewpwd_spy.get() == "":
        messagebox.showwarning("Admin:", "Please Confirm your new password.")
        fg_cfnewpwd_ent.focus_force()
    elif fg_newpwd_spy.get() != fg_cfnewpwd_spy.get():
        messagebox.showwarning(
            "Admin:",
            "New password and Confirm new password are incorrect, please try again"
        )
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
            header["text"] = "Sign In"
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
    header["text"] = "Sign In"
    fg_gmail_spy.set("")
    verif_spy.set("")
    fg_newpwd_spy.set("")
    fg_cfnewpwd_spy.set("")


def loginclicked():
    if gmail_spy.get() == "":
        messagebox.showwarning("Admin:", "Please enter your Email.")
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
                menufame(result)
            else:
                messagebox.showerror(
                    "Admin:", "Email or Password incorrect, please try again.")
                gmail_spy.set("")
                pwd_spy.set("")
                gmail_ent.focus_force()


def menufame(result):
    global mf_frm
    header["text"] = "Username:" + " " + result[2] + " " + result[3]

    mf_frm = Frame(root, bg="white")
    mf_frm.rowconfigure((0, 1), weight=1)
    mf_frm.columnconfigure((0, 1, 2), weight=1)
    mf_frm.grid(row=0, rowspan=2, column=0, sticky="news", padx=10, pady=150)

    Button(mf_frm,
           text="My country",
           fg="#D6E5FA",
           bg="#808cff",
           font="verdana 14",
           image=img_home,
           compound=TOP,
           command=ReportCovid19THPage,
           borderless=1).grid(row=0, column=0, sticky="news", pady=20, padx=20)
    Button(mf_frm,
           text="Province",
           fg="#D6E5FA",
           bg="#808cff",
           font="verdana 15",
           image=img_earth,
           compound=TOP,
           borderless=1,
           command=ReportCovid19ProvincesPage).grid(row=0,
                                                    column=1,
                                                    sticky="news",
                                                    pady=20)
    Button(mf_frm,
           text="Chatbot",
           fg="#D6E5FA",
           bg="#808cff",
           font="verdana 14",
           image=img_bot,
           compound=TOP,
           borderless=1,
           command=chatbot).grid(row=0,
                                 column=2,
                                 sticky="news",
                                 pady=20,
                                 padx=20)
    Button(mf_frm,
           text="Station",
           fg="#D6E5FA",
           bg="#808cff",
           font="verdana 14",
           image=img_map,
           compound=TOP,
           command=OpenMap,
           borderless=1).grid(row=1, column=0, sticky="news", padx=20, pady=10)
    Button(mf_frm,
           text="Log out",
           fg="#D6E5FA",
           bg="#808cff",
           font="verdana 14",
           image=img_out,
           command=logout,
           compound=TOP,
           borderless=1).grid(row=1, column=1, sticky="news", pady=10)
    Button(mf_frm,
           text="Exit",
           fg="#D6E5FA",
           bg="#808cff",
           font="verdana 15",
           image=img_lupa,
           compound=TOP,
           borderless=1,
           command=quit).grid(row=1, column=2, sticky="news", pady=10, padx=20)


def logout():
    gmail_spy.set("")
    pwd_spy.set("")
    LoginPage(root)


def ReportCovid19THPage():
    report_th_page = Frame(root, bg="red")
    report_th_page.rowconfigure(0, weight=1)
    report_th_page.rowconfigure(1, weight=3)
    report_th_page.columnconfigure(0, weight=1)
    report_th_page.grid(row=0, column=0, rowspan=2, sticky="news")

    head = Frame(report_th_page, bg="#daeffd")
    head.rowconfigure(0, weight=1)
    head.rowconfigure(1, weight=5)
    head.columnconfigure((0, 1, 2), weight=1)
    head.grid(row=0, column=0, sticky="news")

    info_frm = Frame(report_th_page, bg="#daeffd")
    info_frm.rowconfigure((0, 1, 2, 3), weight=1)
    info_frm.columnconfigure((0, 1), weight=1)
    info_frm.grid(row=1, column=0, sticky="news")

    # * Header
    Button(head,
           image=go_back_img,
           bg="#dde0fa",
           command=report_th_page.destroy).grid(row=0, column=0, sticky="news")
    Label(head,
          text="My Country",
          fg="black",
          bg="#808cff",
          font="verdana 15 bold").grid(row=0, column=1, sticky="news")
    Label(head,
          text="                ",
          fg="black",
          bg="#dde0fa",
          font="verdana 15 bold").grid(row=0, column=2, sticky="news")
    Label(head,
          text="Thailand",
          fg="lightgray",
          bg="#808cff",
          font="verdana 25",
          width=25).grid(row=1, column=0, columnspan=3)

    # * Info
    # * API {'txn_date': '2022-04-02', 'new_case': 28029, 'total_case': 3684755, 'new_case_excludeabroad': 27993, 'total_case_excludeabroad': 3662238, 'new_death': 96, 'total_death': 25318, 'new_recovered': 23352, 'total_recovered': 3403642, 'update_date': '2022-04-02 07:29:43'}
    response = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
    info = response.json()
    info = info[0]

    # ? Total Cases
    total_frm = Frame(info_frm, bg="#fd8888")
    total_frm.rowconfigure((0, 1), weight=1)
    total_frm.columnconfigure(0, weight=1)
    total = str(info["total_case"])[::-1]
    total_case_str = CorrectRangeOfUnit(total)
    Label(total_frm,
          text="Total Confirmed Cases:",
          fg="white",
          bg="#fd8888",
          font="verdana 19").grid(row=0, column=0, sticky='nw', padx=5, pady=5)
    Label(total_frm,
          text=total_case_str,
          fg="white",
          bg="#fd8888",
          font="verdana 40").grid(row=1, column=0, sticky='e')
    total_frm.grid(row=0, column=0, columnspan=2, sticky="news", padx=20)

    # ? Recovery
    recov_frm = Frame(info_frm, bg="#84e756")
    recov_frm.rowconfigure((0, 1), weight=1)
    recov_frm.columnconfigure(0, weight=1)
    recov = str(info["new_recovered"])[::-1]
    recov_str = CorrectRangeOfUnit(recov)
    Label(recov_frm,
          text="Today Recovery:",
          fg="white",
          bg="#84e756",
          font="verdana 20").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    Label(recov_frm,
          text=recov_str,
          fg="white",
          bg="#84e756",
          font="verdana 25").grid(row=1, column=0, sticky='se')
    recov_frm.grid(row=1, column=0, sticky="news", padx=20, pady=20)

    # ? Today Cases
    td_frm = Frame(info_frm, bg="#808cff")
    td_frm.rowconfigure((0, 1), weight=1)
    td_frm.columnconfigure(0, weight=1)
    td_case = str(info["new_case"])[::-1]
    td_case_str = CorrectRangeOfUnit(td_case)
    Label(td_frm,
          text="Today Case:",
          fg="white",
          bg="#808cff",
          font="verdana 20").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    Label(td_frm,
          text=td_case_str,
          fg="white",
          bg="#808cff",
          font="verdana 25").grid(row=1, column=0, sticky='se')
    td_frm.grid(row=1, column=1, sticky="news", padx=20, pady=20)

    # ? Today death
    today_d_frm = Frame(info_frm, bg="gray")
    today_d_frm.rowconfigure((0, 1), weight=1)
    today_d_frm.columnconfigure(0, weight=1)
    td_d_case = str(info["new_death"])[::-1]
    td_d_case_str = CorrectRangeOfUnit(td_d_case)
    Label(today_d_frm,
          text="Today Death:",
          fg="white",
          bg="gray",
          font="verdana 20").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    Label(today_d_frm,
          text=td_d_case_str,
          fg="white",
          bg="gray",
          font="verdana 25").grid(row=1, column=0, sticky='se')
    today_d_frm.grid(row=2, column=1, sticky="news", padx=20, pady=20)

    # ? Total death
    total_d_frm = Frame(info_frm, bg="#f33534")
    total_d_frm.rowconfigure((0, 1), weight=1)
    total_d_frm.columnconfigure(0, weight=1)
    total_d = str(info["total_death"])[::-1]
    total_d_str = CorrectRangeOfUnit(total_d)
    Label(total_d_frm,
          text="Total Death:",
          fg="white",
          bg="#f33534",
          font="verdana 20").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    Label(total_d_frm,
          text=total_d_str,
          fg="white",
          bg="#f33534",
          font="verdana 25").grid(row=1, column=0, sticky='se')
    total_d_frm.grid(row=2, column=0, sticky="news", padx=20, pady=20)

    Label(info_frm,
          text="Source: Ministry of Public Health",
          bg="#daeffd",
          fg="black",
          font="verdana 10 bold").grid(row=3, column=0, columnspan=2)


def ReportCovid19ProvincesPage():
    global response, info_frm
    report_pv_page = Frame(root, bg="red")
    report_pv_page.rowconfigure(0, weight=1)
    report_pv_page.rowconfigure(1, weight=3)
    report_pv_page.columnconfigure(0, weight=1)
    report_pv_page.grid(row=0, column=0, rowspan=2, sticky="news")

    head = Frame(report_pv_page, bg="#daeffd")
    head.rowconfigure(0, weight=1)
    head.rowconfigure(1, weight=5)
    head.columnconfigure((0, 1, 2), weight=1)
    head.grid(row=0, column=0, sticky="news")

    info_frm = Frame(report_pv_page, bg="#daeffd")
    info_frm.rowconfigure((0, 1, 2, 3), weight=1)
    info_frm.columnconfigure((0, 1), weight=1)
    info_frm.grid(row=1, column=0, sticky="news")

    Button(head,
           image=go_back_img,
           bg="#dde0fa",
           command=report_pv_page.destroy).grid(row=0, column=0, sticky="news")
    Label(head,
          text="Province",
          fg="black",
          bg="#808cff",
          font="verdana 15 bold").grid(row=0, column=1, sticky="news")
    Label(head,
          text="                ",
          fg="black",
          bg="#dde0fa",
          font="verdana 15 bold").grid(row=0, column=2, sticky="news")

    response = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces")
    response = response.json()
    provinces_list = [response[i]["province"] for i in range(len(response))]
    selected_province.set("Please select province")
    combobox = Combobox(head,
                        textvariable=selected_province,
                        values=provinces_list,
                        font="verdana 20",
                        state="readonly")
    combobox.bind("<<ComboboxSelected>>", Province_selected)
    combobox.grid(row=1, column=0, columnspan=3)


def Province_selected(e):
    info = []
    for i in range(len(response)):
        if response[i]["province"] == selected_province.get():
            info.append(response[i])
            break
    info = info[0]

    # ? Total Cases
    total_frm = Frame(info_frm, bg="#fd8888")
    total_frm.rowconfigure((0, 1), weight=1)
    total_frm.columnconfigure(0, weight=1)
    total = str(info["total_case"])[::-1]
    total_case_str = CorrectRangeOfUnit(total)
    Label(total_frm,
          text="Total Confirmed Cases:",
          fg="white",
          bg="#fd8888",
          font="verdana 19").grid(row=0, column=0, sticky='nw', padx=5, pady=5)
    Label(total_frm,
          text=total_case_str,
          fg="white",
          bg="#fd8888",
          font="verdana 40").grid(row=1, column=0, sticky='e')
    total_frm.grid(row=0, column=0, columnspan=2, sticky="news", padx=20)

    # ? New_case (abroad)
    new_ex_frm = Frame(info_frm, bg="#84e756")
    new_ex_frm.rowconfigure((0, 1), weight=1)
    new_ex_frm.columnconfigure(0, weight=1)
    new_ex = str(info["new_case_excludeabroad"])[::-1]
    new_ex_str = CorrectRangeOfUnit(new_ex)
    Label(new_ex_frm,
          text="New Case:\n(not include from other countries)",
          fg="white",
          bg="#84e756",
          font="verdana 15",
          justify=LEFT).grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    Label(new_ex_frm,
          text=new_ex_str,
          fg="white",
          bg="#84e756",
          font="verdana 25").grid(row=1, column=0, sticky='se')
    new_ex_frm.grid(row=1, column=0, sticky="news", padx=20, pady=20)

    # ? Today Cases
    td_frm = Frame(info_frm, bg="#808cff")
    td_frm.rowconfigure((0, 1), weight=1)
    td_frm.columnconfigure(0, weight=1)
    td_case = str(info["new_case"])[::-1]
    td_case_str = CorrectRangeOfUnit(td_case)
    Label(td_frm,
          text="Today Case:",
          fg="white",
          bg="#808cff",
          font="verdana 20").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    Label(td_frm,
          text=td_case_str,
          fg="white",
          bg="#808cff",
          font="verdana 25").grid(row=1, column=0, sticky='se')
    td_frm.grid(row=1, column=1, sticky="news", padx=20, pady=20)

    # ? Today death
    today_d_frm = Frame(info_frm, bg="gray")
    today_d_frm.rowconfigure((0, 1), weight=1)
    today_d_frm.columnconfigure(0, weight=1)
    td_d_case = str(info["new_death"])[::-1]
    td_d_case_str = CorrectRangeOfUnit(td_d_case)
    Label(today_d_frm,
          text="Today Death:",
          fg="white",
          bg="gray",
          font="verdana 20").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    Label(today_d_frm,
          text=td_d_case_str,
          fg="white",
          bg="gray",
          font="verdana 25").grid(row=1, column=0, sticky='se')
    today_d_frm.grid(row=2, column=1, sticky="news", padx=20, pady=20)

    # ? Total death
    total_d_frm = Frame(info_frm, bg="#f33534")
    total_d_frm.rowconfigure((0, 1), weight=1)
    total_d_frm.columnconfigure(0, weight=1)
    total_d = str(info["total_death"])[::-1]
    total_d_str = CorrectRangeOfUnit(total_d)
    Label(total_d_frm,
          text="Total Death:",
          fg="white",
          bg="#f33534",
          font="verdana 20").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
    Label(total_d_frm,
          text=total_d_str,
          fg="white",
          bg="#f33534",
          font="verdana 25").grid(row=1, column=0, sticky='se')
    total_d_frm.grid(row=2, column=0, sticky="news", padx=20, pady=20)

    Label(info_frm,
          text="Source: Ministry of Public Health",
          bg="#daeffd",
          fg="black",
          font="verdana 10 bold").grid(row=3, column=0, columnspan=2)


def OpenMap():
    url = 'https://mohpromtstation.moph.go.th/maps'
    webbrowser.open(url)


def chatbot():
    global chatbotfrm, top, lower, entry_chatbot, Button_send
    chatbotfrm = Frame(root, bg="#daeffd")
    chatbotfrm.rowconfigure(0, weight=1)
    chatbotfrm.rowconfigure(1, weight=4)
    chatbotfrm.rowconfigure(2, weight=2)
    chatbotfrm.columnconfigure((0, 1), weight=2)
    chatbotfrm.place(x=0, y=0, width=w, height=h)
    Label(chatbotfrm,
          text="ChatBot",
          fg="#808cff",
          bg="#daeffd",
          font="verdana 40").grid(row=0, column=0, columnspan=2, sticky="news")

    top = Text(chatbotfrm,
               bg='#daeffd',
               fg="black",
               font="verdana 10",
               width=200,
               height=2)
    top.columnconfigure(0, weight=1)
    top.grid(row=1, column=0, sticky='news')
    scrollbar = Scrollbar(top)
    scrollbar.pack(side=RIGHT, fill="y")

    right = Frame(chatbotfrm, bg="#daeffd")
    right.columnconfigure((0, 1, 2, 3, 4), weight=1)
    right.grid(row=2, column=0, sticky='news', rowspan=7)
    Label(right,
          text="กดเลขหมายด้านล่าง หากมีข้อสงสัยเกี่ยวกับ",
          bg="#daeffd",
          fg="black",
          font="verdana 15").grid(row=0, column=0, sticky="w")
    Label(right,
          text="1. ถ้าติดโควิด19จะทำยังไง",
          bg="#daeffd",
          fg="black",
          font="verdana 15").grid(row=1, column=0, sticky="w")
    Label(right,
          text="2. อาการเบื้องต้นของโควิด",
          bg="#daeffd",
          fg="black",
          font="verdana 15").grid(row=2, column=0, sticky="w")
    Label(
        right,
        text="3. ผู้ที่เคยติดโควิด19มาก่อน ยังจำเป็นต้องได้รับวัคซีนโควิด 19 หรือไม่",
        bg="#daeffd",
        fg="black",
        font="verdana 15").grid(row=3, column=0, sticky="w")
    Label(right,
          text="4. วัคซีนในประเทศไทย",
          bg="#daeffd",
          fg="black",
          font="verdana 15").grid(row=4, column=0, sticky="w")

    lower = Text(chatbotfrm, bg='#daeffd')
    lower.columnconfigure((0, 1), weight=1)
    lower.grid(row=3, column=0, columnspan=1, sticky='news', rowspan=7)
    entry_chatbot = Entry(lower, textvariable=spy_message)
    entry_chatbot.grid(row=1, column=0, ipadx=150)
    Button_send = Button(lower,
                         text="Send",
                         bg="#808cff",
                         fg="white",
                         command=send)
    Button_send.grid(row=1, column=1, columnspan=2, ipadx=30)
    Button(chatbotfrm,
           image=go_back_img,
           bg="#808cff",
           command=chatbotfrm.destroy).grid(row=0,
                                            column=0,
                                            sticky="nw",
                                            ipadx=30)
    entry_chatbot.focus_force()


def send():
    send = "You => " + spy_message.get()
    top.insert(END, "\n" + send)
    if (entry_chatbot.get() == "1"):
        top.insert(
            END, "\n" +
            "Chatbot ==> 1.เตรียมเอกสารต้องใช้ เช่น บัตร ปชช ผลตรวจCOVID19\nและแจ้งหมายเลขโทรศัพท์ของตน ทางหน่วยงาน\n2.งดออกจากที่พักหรือเดินทางข้ามจังหวัด\n3.งดใกล้ชิดคนในครอบครัวและผู้อื่น\n4.สวมแมสก์ตลอดเวลา\n5.หากมีไข้ให้รับประทานยาแล้วเช็ดตัวเพื่อลดไข้\n"
        )
    elif (entry_chatbot.get() == "4"):
        top.insert(
            END, "\n" +
            '''Chatbot ==> วัคซีนโควิด19ที่มีให้บริการในประเทศไทย มี 6 ชนิด คือ
        1.วัคซีนโควิดซิโนแวค (Sinovac) อย.อนุมัติเมื่อ 27 กุมภาพันธ์ 2564
        2.วัคซีนโควิดแอสตราเซเนก้า (AstraZeneca) อย.อนุมัติเมื่อ 20 มกราคม 2564
        3.วัคซีนโควิดจอห์นสัน แอนด์ จอห์นสัน (Johnson & Johnson) อย.อนุมัติเมื่อ 25 มีนาคม 2564
        4.วัคซีนโควิดโมเดอร์นา (Moderna) อย.อนุมัติเมื่อ 13 พฤษภาคม 2564
        5.วัคซีนโควิดซิโนฟาร์ม (Sinopharm) อย.อนุมัติเมื่อ 28 พฤษภาคม 2564
        6.วัคซีนโควิดไฟเซอร์ ไบโอเอ็นเทค (Pfizer/ BioNtech) อย.อนุมัติเมื่อ 24 มิถุนายน 2564
''')
    elif (entry_chatbot.get() == "3"):
        top.insert(
            END, "\n" +
            "Chatbot ==> แม้จะมีภูมิคุ้มกันต่อเชื้อไวรัสโควิด19ในร่างกายแต่ยังมี\nโอกาสติดเชื้อซ้ำได้ ดังนั้นจึงควรได้รับวัคซีน\n"
        )
    elif (entry_chatbot.get() == "2"):
        top.insert(
            END, "\n" +
            "Chatbot ==> -ไม่มีอาการ\n-มีไข้/วัดอุณหภูมิได้ 37.5 C ขึ้นไป\n-ไอ มีน้ำมูก เจ็บคอ\n-ถ่ายเหลว\n-จมูกไม่ได้กลิ่น ลิ้นไม่รับรส-\n-ตาแดง มีผื่น\n-ไม่มีโรคประจำตัวร่วม\n-หายใจปกติ ปอดไม่อักเสบ\n-ไม่มีปัจจัยเสี่ยงต่อการเป็นโรครุนแรง / โรคร่วมสำคัญ\n"
        )
    else:
        top.insert(END, "\nChatbot ==> กรุณาใส่ข้อความใหม่\n")
        entry_chatbot.focus_force()
    entry_chatbot.delete(0, END)
    entry_chatbot.focus_force()


def CorrectRangeOfUnit(number: str):
    return_nums = ""
    counts = 0
    for i in range(len(number)):
        return_nums += number[i]
        counts += 1
        if counts == 3:
            if i + 1 == len(number):
                pass
            else:
                return_nums += ","
                counts = 0
    return return_nums[::-1]


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

# ! Report Global spy
selected_province = StringVar()

go_back_img = PhotoImage(file="images/return.png").subsample(2, 2)
img_bot = PhotoImage(file="images/icon_bot.png").subsample(10, 10)
img_earth = PhotoImage(file="images/icon_earth.png").subsample(20, 20)
img_home = PhotoImage(file="images/icon_home.png").subsample(20, 20)
img_lupa = PhotoImage(file="images/icon_lupa.png").subsample(20, 20)
img_map = PhotoImage(file="images/icon_map.png").subsample(20, 20)
img_out = PhotoImage(file="images/icon_out.png").subsample(20, 20)

#spy chatbot
spy_message = StringVar()
spy_send = StringVar()

LoginPage(root)
root.mainloop()
cursor.close()
conn.close()