from simple_atm_machine import SimpleATMMachine

if __name__ == '__main__':
	atm= SimpleATMMachine()
	db = atm.db

	is_exit = False
	while not is_exit:
		try:
			mode = raw_input("1. db_table, 2. delete_account\n>")

			if mode == '1':
				db.show_table()


		except KeyboardInterrupt:
			is_exit = True
			break
		except Exception, e:
			print("\n[WARN]%s\n"%e)

	atm.save_database()
	print("\n[INFO]Saved the ATM Database")