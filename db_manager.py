from module.backend import SimpleATMMachine

if __name__ == '__main__':
	atm= SimpleATMMachine()

	is_exit = False
	while not is_exit:
		try:
			mode = raw_input("1. db_table, 2. delete_account, 3. exit\n>")

			if mode == '1':
				atm.db.show_table()
			elif mode == '2':
				acc_to_delete = raw_input("plz type the account_id what you want to delete\n>")
				atm.db.delete_account(acc_to_delete)
			elif mode == '3':
				is_exit = True

		except KeyboardInterrupt:
			is_exit = True
			break
		except Exception, e:
			print("\n[WARN]%s\n"%e)

	atm.save_database()
	print("\n[INFO]Saved the ATM Database")