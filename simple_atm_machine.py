import sys, os, pickle, time
from database import Database

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
		print("2. Account Number")
		print("")
		print("If you don't have any account,")
		print("3. New Account")
		print("")

		return input(">>")

	def to_home(self):
		for i in range(3,-1,-1):
			sys.stderr.write("%d "%i)
			if i == 0: sys.stderr.write("go home!")
			time.sleep(1)

	##############################################
	# Verification
	##############################################
	def pin_verification(self, account_):
		for i in range(1,4):
			pin = raw_input("PIN number > ")
			if self.db.pin_check(account_, pin):
				return True
			else:
				print("PIN number is wrong, retry(%d/3)"%i)

	###############################################
	# Modules
	###############################################
	def access_cardnum(self):
		card_id_ = raw_input("insert card number: ")
		return self.db.search_account(card_id=card_id_)

	def access_accnum(self):
		acc_id_ = raw_input("insert account number: ")
		return self.db.search_account(acc_id=acc_id_)

	def select_account(self, accounts_):
		os.system('clear')
		print("=======Select_A_Account========")
		for i in range(len(accounts_)):
			print("%d. account: %s\t id: %s"%(i,accounts[i].name,accounts[i].id))
			print("-")
		print("===============================")
		return self.db.search_account(acc_id=raw_input(">>"))

	def functions(self, a_account_):
		print("Choose What you want to")
		print("1. See balance")
		print("2. Deposit")
		print("3. WithDraw")
		func = raw_input(">>")

		if func==1: # See balance
			print("balance: $%d"%a_account_.balance)
		elif func==2: # Deposit
			print("balance: $%d"%a_account_.balance)
			deposit = raw_input("how much do you want to deposit?\n>>")
			self.db.deposit(a_account_.id,deposit)
		elif func==3: # WithDraw
			print("balance: $%d"%a_account_.balance)
			withdraw = raw_input("how much do you want to withdraw?\n>>")
			self.db.withdraw(a_account_.id,withdraw)

	def new_account(self):
		name_ = raw_input("name: ")
		card_ = raw_input("card_id: ")
		acc_ = raw_input("account_id: ")
		
		confirmed = False; tries = 0
		while not confirmed:
			pin_ = raw_input("pin_number: ")
			if pin_ == raw_input("pin_number confirm: "):
				confirmed = True
			else:
				print("the pin number is not confirmed...")
				tries = tries + 1
				if tries > 2:
					raise Exception("coundn't confirm the pin number. be over the max tries.")

		deposit_ = raw_input("initial deposit: ")
		self.db.add_account(name_, card_, acc_, pin_, deposit_)

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