import datetime,time

class Account():
	def __init__(self, name_, id_, card_, PIN_, balance_=0):
		self.name = name_
		self.id = id_
		self.card = card_
		self.balance = balance_
		self.PIN = PIN_
		self.created_date = datetime.datetime.today()
		self.updated_date = datetime.datetime.today()

class Database():
	def __init__(self):
		self.__accounts = []

	##############################################
	# System Functions
	##############################################
	def add_account(self, name_, id_, card_, PIN_, balance_=0):
		self.__accounts.append(Account(name_, id_, card_, PIN_, balance_))
		print("-")
		print("name: %s\taccound_id: %s\ncard_id: %s\tbalance: %s"%(name_,id_,card_,balance_))
		print("new account created.")
		print("-")

	def search_account(self, acc_id=-1, card_id=-1):
		if not acc_id == -1:
			for acc in self.__accounts:
				if acc.id == acc_id:
					return acc
			raise Exception("Invalid Account Number!")
		elif not card_id == -1:
			accs = []
			for acc in self.__accounts:
				if acc.card == card_id:
					accs.append(acc)
			if len(accs) > 0: return accs
			else:
				raise Exception("Invalid Card Number!")
		else:
			raise Exception("(search_account)something wrong!")

	def pin_check(self, acc_id, pin_num):
		for acc in self.__accounts:
			if acc.id == acc_id:
				if acc.PIN == pin_num: return True
				else: return False
		raise Exception("(pin_check)something worng!")

	def elapsed_clear(self):
		temp_accounts = list(self.__accounts)
		for i in range(len(self.__accounts)):
			if (self.__accounts[i].updated_date.year - datetime.datetime.today().year) > 5: # if it's not updated during 5 years more, clear.
				del temp_accounts[i]
		self.__accounts = list(temp_accounts)

	###################################################
	# Applications
	###################################################
	def get_accounts_number(self):
		return len(self.__accounts)

	def show_table(self):
		print("======================ACCOUNTS TABLE========================")
		for i in range(len(self.__accounts)):
			print("%d. account: %s\t id: %s\t card_id: %s\t balance: $%s\t"
				%(i, self.__accounts[i].name,self.__accounts[i].id,self.__accounts[i].card,self.__accounts[i].balance))
		print("============================================================")
		time.sleep(1)

	def deposit(self, acc_id, deposit):
		for i in range(len(self.__accounts)):
			if self.__accounts[i].id == acc_id:
				self.__accounts[i].balance += deposit
				break
		print("$%d deposited. balance: $%d"%(deposit,self.__accounts[i].balance))

	def withdraw(self, acc_id, withdraw):
		for i in range(len(self.__accounts)):
			if self.__accounts[i].id == acc_id:
				if self.__accounts[i].balance - withdraw < 0:
					raise Exception("balance is not enough")
				self.__accounts[i].balance -= withdraw
				break
		print("$%d withdrawed. balance: $%d"%(withdraw,self.__accounts[i].balance))
