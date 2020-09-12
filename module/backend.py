import sys, os, pickle, time
from module.database import Database

class SimpleATMMachine():
	def __init__(self, db_path="ATMAccounts.db"):
		# Load database & clear long elapsed_data
		self.db = self.load_database(db_path)
		self.db.elapsed_clear()

	####################################################
	# Display-related
	####################################################
	def Menual(self):
		os.system('clear')
		print("======================================")
		print("\tWellcome to					")
		print("\tSimple ATM Controller		")
		print("======================================")

		print('jointed accounts:%d\n'%self.db.get_accounts_number())

		print("Access via")
		print("1. Card Number")
		print("")
		print("If you don't have any account,")
		print("2. New Account")
		print("")
		print("3. Exit")
		print("")

		return input(">>")

	def to_home(self):
		for i in range(3,-1,-1):
			sys.stderr.write("%d "%i)
			if i == 0: sys.stderr.write("go home!")
			time.sleep(1)
		self.save_database() # auto-save

	##############################################
	# Verification
	##############################################
	def pin_verification(self, account_):
		passed = False; tries=0
		while not passed:
			pin_ = int(raw_input("pin_number: "))
			if pin_ == account_.user.PIN:
				passed = True
			else:
				print("wrong PIN number, try again.")
				treis = tries + 1
				if tries > 2:
					raise Exception("wrong PIN number, exceeded the max tries.")
		return pin_

	def pin_number_set(self):
		confirmed = False; tries = 0
		while not confirmed:
			pin_ = raw_input("pin_number: ")
			if pin_ == raw_input("pin_number confirm: "):
				confirmed = True
			else:
				print("the pin number is not confirmed...")
				tries = tries + 1
				if tries > 2:
					raise Exception("coundn't confirm the pin number. exceeded the max tries.")
		return pin_

	###############################################
	# Modules
	###############################################
	def access_cardnum(self):
		card_id_ = raw_input("insert card number: ")
		accounts = self.db.search_account(card_id=card_id_)
		self.pin_verification(accounts[0])
		return accounts

	def select_account(self, accounts_):
		os.system('clear')
		print("=======Select_A_Account========")
		for i in range(len(accounts_)):
			print("%d. account: %s\tid: %s"%(i,accounts_[i].user.name,accounts_[i].id))
			print("-")
		print("===============================")
		return self.db.search_account(acc_id=raw_input("enter account_id\n>>"))

	def functions(self, a_account_):
		print("Choose What you want to")
		print("1. See balance")
		print("2. Deposit")
		print("3. WithDraw")
		func = raw_input(">>")

		if func=='1': # See balance
			print("balance: $%d"%a_account_.balance)
		elif func=='2': # Deposit
			print("balance: $%d"%a_account_.balance)
			deposit = raw_input("how much do you want to deposit?\n>>")
			self.db.deposit(a_account_.id,deposit)
		elif func=='3': # WithDraw
			print("balance: $%d"%a_account_.balance)
			withdraw = raw_input("how much do you want to withdraw?\n>>")
			self.db.withdraw(a_account_.id,withdraw)
		else:
			raise Exception("wrong function mode reqeuested")

	def new_account(self):
		def random_with_N_digits(n):
			from random import randint

			range_start = 10**(n-1)
			range_end = (10**n)-1
			return randint(range_start, range_end)

		has_card = raw_input("Do you have a card?(y/n)\n>")
		if has_card == 'y':
			card_ = raw_input("card_id: ")
			accounts = self.db.search_account(card_id = card_)

			pin_ = self.pin_verification(accounts[0])
			name_ = raw_input("account_name: ")
			card_ = accounts[0].user.card
			acc_ = random_with_N_digits(6)
			deposit_ = raw_input("initial deposit: ")
			self.db.add_account(name_, acc_, card_, pin_, deposit_)

		elif has_card == 'n':
			name_ = raw_input("account_name: ")
			card_ = random_with_N_digits(4)
			acc_ = random_with_N_digits(6)
			pin_ = self.pin_number_set()
			deposit_ = raw_input("initial deposit: ")
			self.db.add_account(name_,  acc_, card_, pin_, deposit_)
		else:
			raise Exception("wrong answer, plz answer y or n")

	###############################################
	# LOAD & SAVE Database of Accounts
	###############################################
	def load_database(self, db_path):
		if not os.path.isfile(db_path):
			return Database()
		else:
			with open(db_path, 'rb') as f:
				db = pickle.load(f)
			return db

	def save_database(self,db_path="ATMAccounts.db"):
		with open(db_path, 'wb') as f:
			pickle.dump(self.db, f)