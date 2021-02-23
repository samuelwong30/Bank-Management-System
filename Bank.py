import sqlite3
from tkinter import *
from Account import *
from Account import *
from tkinter import messagebox
from tkinter import ttk

# Create an account 
def create_account(account):
	my_info = account.display()
	# Insert into table
	c.execute("INSERT INTO account VALUES (:first_name, :last_name, :account_num, :password, :account_type, :balance, :transactions)",{'first_name': my_info[0], 'last_name': my_info[1], 'account_num': my_info[2], 'password': my_info[3], 'account_type': my_info[4], 'balance': my_info[5], 'transactions': "No Transactions"})

# Get account information
def get_account(account_number, my_password):
	c.execute("SELECT * FROM account WHERE account_num = ? AND password = ?", (account_number, my_password))
	my_info = c.fetchone()
	# Case: account number not found
	if type(my_info) == type(None):
		return [0,0]
	else:
		return [my_info, 1]

# Log in by returning account information
def dblog_in(account_num, password):
	status = get_account(account_num, password)

	# If account does not exist, return 0
	if status[1] == 0:
		return [0, 0]
	else:
		return status

# Delete account
def delete_account(account_number, my_password):
	# Check if account exists first 
	c.execute("SELECT * FROM account WHERE account_num = ? AND password = ?", (account_number, my_password))
	my_info = c.fetchone()
	if type(my_info) == type(None):
		return 0
	# Remove from database
	c.execute("DELETE from account WHERE account_num = :account_num", {'account_num': account_number})

# Deposit money into balance add update transactions
def db_deposit(account, amount):
	c.execute("SELECT * FROM account WHERE account_num = ? AND password = ?", (account.account_num, account.password))
	my_info = c.fetchone()
	# Check if account exists
	if type(my_info) == type(None):
		return 0
	temp_account = Account(my_info[0], my_info[1], my_info[2], my_info[3], my_info[4])
	temp_account.update_balance(my_info[5])
	if temp_account.deposit(amount) == 0:
		return 0
	else:
		c.execute("""UPDATE account SET balance = :balance, transactions = :transactions
					WHERE account_num = :account_num AND password = :password""",
					{'balance': temp_account.balance, 'transactions': temp_account.transactions, 'account_num': temp_account.account_num, 'password': temp_account.password})	

# Withdraw money from balance and update transactions
def db_withdraw(account, amount):
	c.execute("SELECT * FROM account WHERE account_num = ? AND password = ?", (account.account_num, account.password))
	my_info = c.fetchone()
	# Check if account exists
	if type(my_info) == type(None):
		return 0
	temp_account = Account(my_info[0], my_info[1], my_info[2], my_info[3], my_info[4])
	temp_account.update_balance(my_info[5])
	if temp_account.withdraw(amount) == 0:
		return 0
	else:
		c.execute("""UPDATE account SET balance = :balance, transactions = :transactions
					WHERE account_num = :account_num AND password = :password""",
					{'balance': temp_account.balance, 'transactions': temp_account.transactions, 'account_num': temp_account.account_num, 'password': temp_account.password})

def create_accountnumber():
	num = ''
	while True:
		for i in range(0,8):
			num += (str(randint(0,9)))
		# Check if account number already exists
		c.execute("SELECT * FROM account WHERE account_num = :account_num", {'account_num': num})
		my_info = c.fetchone()
		if type(my_info) == type(None):
			return num
		num = ''

conn = sqlite3.connect('account.db')

c = conn.cursor()

#c.execute("""CREATE TABLE account (
#			first_name text,
#			last_name text,
#			account_num text,
#			password integer,
#			account_type text,
#			balance real,
#			transactions text
#			)""")

def run_gui():
	root = Tk()
	root.title("Main Menu")
	root.geometry('475x175')

	global account_1

	account_1 = Account("", "", 0, 0, "")

	# THE 3 FRAMES 
	# Frame 1
	# 1 -> 2
	def display_1go2():
		frame1.grid_forget()
		root.title("Log in")
		frame2.grid()
	# 1 -> 3
	def display_1go3():
		frame1.grid_forget()
		root.title("Create Account")
		frame3.grid()
		
	# Frame 2
	# 2 -> 1
	def display_2go1():
		frame2.grid_forget()
		e1_2.delete(0, END)
		e2_2.delete(0, END)
		root.title("Main Menu")
		frame1.grid()
	def display_2go4():
		frame2.grid_forget()
		root.title("Account Menu")
		frame4.grid()

	# Frame 3
	# 3 -> 1
	def display_3go1():
		frame3.grid_forget()
		e1_3.delete(0, END)
		e2_3.delete(0, END)
		e3_3.delete(0, END)
		select.set(options[0])
		root.title("Main Menu")
		frame1.grid()
	def display_3go4():
		frame3.grid_forget()
		root.title("Account Menu")
		frame4.grid()

	# Frame 4
	# 4 -> 1
	def display_4go1():
		response = messagebox.askyesno("Log out", "Are you sure you want to log out?")
		if (response == 1):
			frame4.grid_forget()
			root.title("Main Menu")
			frame1.grid()
	# 4 -> 5
	def display_4go5():
		frame4.grid_forget()
		root.title("Account Information")
		frame5.grid()
		display_info()

	# 4 -> 6	
	def display_4go6():
		frame4.grid_forget()
		root.title("Deposits & Withdraws")
		frame6.grid()

	# 4 -> 7
	def display_4go7():
		frame4.grid_forget()
		root.title("Delete Account")
		frame7.grid()

	# Frame 5
	# 5 -> 4
	def display_5go4():
		l11_5.destroy()
		l22_5.destroy()
		l33_5.destroy()
		l44_5.destroy()
		l55_5.destroy()
		l66_5.destroy()

		frame5.grid_forget()
		root.title("Account Menu")
		frame4.grid()

	# Frame 6
	# 6 -> 4
	def display_6go4():
		frame6.grid_forget()
		root.title("Account Menu")
		frame4.grid()

	# Frame 7
	# 7 -> 4
	def display_7go4():
		frame7.grid_forget()
		root.title("Account Menu")
		frame4.grid()

	# 7 -> 1
	def display_7go1():
		frame7.grid_forget()
		root.title("Main Menu")
		frame1.grid()

	# Get input from entry in frame 1
	def create():
		if (e1_3.get() == "" or e2_3.get() == "" or e3_3.get() == ""):
			messagebox.showerror("Error", "One or more fields left empty")
			return
		if len(e3_3.get()) != 4 or e3_3.get().isdecimal() != True:
			messagebox.showerror("Error", "Password must be be of length 4 consisting of digits 0-9")
			return

		temp_fname = e1_3.get().capitalize()
		temp_lname = e2_3.get().capitalize()

		account_1.f_name = temp_fname
		account_1.l_name = temp_lname
		account_1.account_num = create_accountnumber()
		account_1.password = e3_3.get()
		account_1.account_type = select.get()
		account_1.set_all(temp_fname, temp_lname, create_accountnumber(), e3_3.get(), select.get(), 0.00, "No Transactions")

		# Set information in database
		create_account(account_1)
		messagebox.showinfo("Success!", "Account succesfully created\nAccount number: " + account_1.account_num + "\nPassword: " + e3_3.get())

		global curr_accountnum
		global curr_password

		curr_accountnum = account_1.account_num
		curr_password = e3_3.get()

		e1_3.delete(0, END)
		e2_3.delete(0, END)
		e3_3.delete(0, END)
		select.set(options[0])
		display_3go4()

	# Log in to account
	def log_in():
		status = dblog_in(e1_2.get(), e2_2.get())
		if status[1] != 0:
			global curr_accountnum
			global curr_password
			curr_accountnum = e1_2.get()
			curr_password = e2_2.get()
			status = status[0]
			account_1.set_all(status[0], status[1], status[2], status[3], status[4], status[5], status[6])
			e1_2.delete(0, END)
			e2_2.delete(0, END)
			display_2go4()
		elif (e1_2.get() == "" or e2_2.get() == ""):
			messagebox.showerror("Error", "One or more field left empty")
		else:
			messagebox.showerror("Error", "Incorrect account number or password")

	# Delete account
	def del_account():
		if (e1_7.get() == "" or e2_7.get() == ""):
			messagebox.showerror("Error", "One or more field left empty")
			return
		status = dblog_in(e1_7.get(), e2_7.get())
		if status[1] != 0:
			response = messagebox.askyesno("Delete Account", "Are you sure you want to delete your account?")
			if (response == 1):
				delete_account(e1_7.get(), e2_7.get())
				e1_7.delete(0, END)
				e2_7.delete(0, END)
				my_msg = messagebox.showinfo("Confirmation", "Your account has been deleted")
				display_7go1()
		else:
			messagebox.showerror("Error", "Incorect account number or password")
	
	# Display account information
	def display_info():
		status = dblog_in(account_1.account_num, account_1.password)
		status = status[0]

		global l11_5
		global l22_5
		global l33_5
		global l44_5
		global l55_5
		global l66_5

		l1_5 = Label(frame5, text = "Name:" ).grid(row=1, column=2)
		l11_5 = Label(frame5, text = status[0] + " " + status[1])
		l11_5.grid(row=1, column=3)
		l2_5 = Label(frame5, text = "Account Number:").grid(row=2, column=2)
		l22_5 = Label(frame5, text = status[2])
		l22_5.grid(row=2, column=3)
		l3_5 = Label(frame5, text = "Account Password:").grid(row=3, column=2)
		l33_5 = Label(frame5, text = str(status[3]))
		l33_5.grid(row=3, column=3)
		l4_5 = Label(frame5, text = "Account Type:").grid(row=4, column=2)
		l44_5 = Label(frame5, text = status[4])
		l44_5.grid(row=4, column=3)
		l5_5 = Label(frame5, text = "Balance:").grid(row=5, column=2)
		l55_5 = Label(frame5, text = "$" + str(status[5]))
		l55_5.grid(row=5, column=3)
		l6_5 = Label(frame5, text = "Latest Transaction:").grid(row=6, column=2)
		l66_5 = Label(frame5, text = status[6])
		l66_5.grid(row=6, column=3)

		b2_5 = Button(frame5, text = "Back to Account Menu", command=display_5go4).grid(row=7, column=2)

	# Deposit or withdraw amount into db	
	def depo_withdraw():
		status = dblog_in(curr_accountnum, int(curr_password))
		status = status[0]
		account_1.set_all(status[0], status[1], status[2], status[3], status[4], status[5], status[6])

		# Check parameters
		if e1_6.get() == "":
			response = messagebox.showerror("Error", "Please enter an amount")
			return
		answ = str(e1_6.get())
		if "." not in answ:
			answ += ".00"
		answ = answ.split(".")
		answ = answ[1]
		if len(answ) != 2:
			response = messagebox.showerror("Error", "Please enter an actual amount")
			return
		try:
			float(e1_6.get())
		except ValueError:
			response = messagebox.showerror("Error", "Please enter a decimal")
			return

		# Check whether to deposit or not
		dep_with = pick.get()
		if dep_with == "Deposit":
			if db_deposit(account_1, float(e1_6.get())) == 0:
				response = messagebox.showerror("Error", "Sorry, you need to deposit over $5.00")
				return
			msg = messagebox.showinfo("Success", "You have deposited $" + e1_6.get())
			e1_6.delete(0,END)
			pick.set(bank_actions[0])
			display_6go4()
		else:
			if db_withdraw(account_1, float(e1_6.get())) == 0:
				response = messagebox.showerror("Error", "Sorry, you don't have the funds for that")
				return
			msg = messagebox.showinfo("Success", "You have wtihdrawn $" + e1_6.get())
			e1_6.delete(0,END)
			pick.set(bank_actions[0])
			display_6go4()
	
	# Frame 1: Main Menu
	frame1 = Frame(root)

	l1_1 = Label(frame1, text = "Welcome to the Bank of Sam")
	l1_1.config(font=("Courier", 15))
	l1_1.grid(row=1, column=2)
	l2_2 = Label(frame1, text = "                        ").grid(row=1, column=1)

	b1_go_2 = Button(frame1, text = "Log-in", command = display_1go2).grid(row=2, column=2)
	b1_go_3 = Button(frame1, text = "Create Account", command = display_1go3).grid(row=3, column=2)

	# Frame 2: Log- in
	frame2 = Frame(root)
	Label(frame2, text = 'Account number').grid(row=1, column=2)
	Label(frame2, text = 'Password').grid(row=2,column=2)

	e1_2 = Entry(frame2)
	e1_2.grid(row=1, column = 3)

	e2_2 =  Entry(frame2)
	e2_2.grid(row=2, column = 3)
	
	b2_2 = Button(frame2, text = 'Log-in', command = log_in).grid(row=4, column = 4)
	b2_go_1 = Button(frame2, text = 'Main Menu', command=display_2go1).grid(row=4, column=2)
	
	# Frame 3: Create Account
	frame3 = Frame(root)

	Label(frame3, text = 'First Name').grid(row=1, column=2)
	Label(frame3, text = "Last Name").grid(row=2, column=2)
	Label(frame3, text = 'Password').grid(row=3, column =2)
	Label(frame3, text = 'Account Type').grid(row=4, column=2)
	Label(frame3, text = "Enter 4 digit password", fg = "light gray").grid(row=3, column =4)
	
	# Get entry info to create account
	e1_3 = Entry(frame3)
	e1_3.grid(row=1, column = 3)

	e2_3 = Entry(frame3)
	e2_3.grid(row=2, column = 3)

	e3_3 = Entry(frame3)
	e3_3.grid(row=3, column = 3)

	options = ['Chequing', 'Savings']
	select = StringVar()
	select.set(options[0])

	my_ops = OptionMenu(frame3, select, *options)
	my_ops.grid(row=4, column = 3)

	b1_1 = Button(frame3, text ='Submit', command=create).grid(row=7, column=4)	
	b3_go_1 = Button(frame3, text = 'Back to Main Menu', command=display_3go1).grid(row=7, column=2)

	# Frame 4: Account Menu
	frame4 = Frame(root)

	l1_4 = Label(frame4, text = "Select an option")
	l1_4.config(font = ("Courier", 15))
	l1_4.grid(row=1, column=2)

	l2_4 = Label(frame4, text = "                                     ").grid(row=1, column=1)

	b1_4 = Button(frame4, text = "Account Information", command=display_4go5).grid(row=2,column=2)
	b24 = Button(frame4, text = "Deposit/Withdraw", command=display_4go6).grid(row=3, column=2)
	b3_4 = Button(frame4, text = "Delete Account", command=display_4go7).grid(row=4, column=2)
	b4_4 = Button(frame4, text = "Log-out", command=display_4go1).grid(row=5,column=1)

	# Frame 5: Account Information
	frame5 = Frame(root)

	# Frame 6: Deposit/Withdraw
	frame6 = Frame(root)

	bank_actions = ["Deposit", "Withdraw"]
	pick = StringVar()
	pick.set(bank_actions[0])

	l1_6 = Label(frame6, text = "Select to deposit or withdraw").grid(row=1, column=1)
	pick_action = OptionMenu(frame6, pick, *bank_actions)
	pick_action.grid(row=1, column=2) 

	l2_6 = Label(frame6, text = "Enter Amount: $").grid(row=2, column=1)
	e1_6 = Entry(frame6, text = "Enter monies")
	e1_6.grid(row=2, column=2)

	b1_6 = Button(frame6, text="Back to Account Menu", command=display_6go4).grid(row=3, column=1)
	b2_6 = Button(frame6, text = "Submit", command = depo_withdraw).grid(row=3, column=2)

	# Frame 7: Delete account
	frame7 = Frame(root)

	l1_7 = Label(frame7, text="Enter Account Number").grid(row=1, column=1)
	l1_7 = Label(frame7, text="Enter Password").grid(row=2, column=1)

	e1_7 = Entry(frame7)
	e1_7.grid(row=1, column=2)
	e2_7 = Entry(frame7)
	e2_7.grid(row=2, column=2)

	b1_7 = Button(frame7, text="Delete Account", command=del_account).grid(row=3, column=2)
	b2_7 = Button(frame7, text="Back to Account Menu", command=display_7go4).grid(row=3, column=1)

	frame1.grid()
	root.mainloop()

run_gui()

conn.commit()
conn.close()