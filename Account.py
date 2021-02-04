from random import randint
import datetime


class Account():

	# Constructor
	def __init__(self, f_name, l_name, account_num, password, account_type):
		self.f_name = f_name
		self.l_name = l_name
		self.account_num = account_num
		self.password = password
		self.account_type = account_type
		self.balance = 0.00
		self.transactions = ''

	# Destructor
	def __del__(self):
		return
	
	# Deposits money into account from balance
	def deposit(self, amount):
		if amount < 5.00:
			return 0
		else:
			self.balance += round(amount, 2)
			
			#Date of Transaction
			now = datetime.datetime.now()
			rn  = now.strftime("%y-%m-%d, %H:%M")

			#Type of Transaction
			amount = "{:.2f}".format(amount)
			my_trans = 'Deposit'
			my_t = "({time}), {trans}, ${money})".format(time=rn, trans=my_trans, money=amount)

			self.transactions= my_t

	# Withdraws money from account from balance
	def withdraw(self, amount):
		if amount > self.balance:
			return 0
		else:
			self.balance -= round(amount, 2)
			
			#Date of Transaction
			now = datetime.datetime.now()
			rn  = now.strftime("%y-%m-%d, %H:%M")

			#Type of Transaction
			amount = "{:.2f}".format(amount)
			my_trans = 'Withdraw'
			my_t = "({time}), {trans}, ${money})".format(time=rn, trans=my_trans, money=amount)

			self.transactions = my_t

	# Returns account information as a list
	def display(self):
		return [self.f_name, self.l_name, self.account_num, self.password, self.account_type, self.balance, self.transactions]

	# Set all:
	def set_all(self, first, last, num, passw, acc_type, bal, trans):
		self.f_name = first 
		self.l_name = last
		self.account_num = num
		self.password = passw
		self.account_type = acc_type
		self.balance = bal
		self.transactions = trans

	# Update balance 
	def update_balance(self, new_balance):
		self.balance = new_balance