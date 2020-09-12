from simple_atm_machine import SimpleATMMachine
import time

if __name__ == '__main__':
	atm = SimpleATMMachine()
	
	is_exit = False
	while not is_exit:
		try:
			mode = atm.Menual()

			if mode == 1:
				accounts = atm.access_cardnum()
				a_account = atm.select_account(accounts)
				atm.functions(a_account)
			elif mode == 2:
				a_account = atm.access_accnum()
				atm.functions(a_account)
			elif mode == 3:
				atm.new_account()

		except KeyboardInterrupt:
			is_exit = True
			break
		except Exception, e:
			print("[WARN]%s"%e)
		finally:
			if not is_exit: atm.to_home()

	atm.save_database()
	print("\n[INFO]Saved the ATM Database")