# simple-ATM-controller

Implementation of Custom Task for Code Tests.

## Structure

```bash
simple-ATM-controller 
├── ATMAccounts.db 	# user accounts database
├── db_manager.py	# for db-management or monitor
├── main.py			# main routine for this task
├── module			# backend modules
│   ├── backend.py	# simple-atm-controller structure & methods
│   ├── database.py # database structure & methods
│   └── __init__.py
└── README.md
```



## Guide

### main.py

1. **Main Screen**

   ```bash
   ======================================
   	Wellcome to					
   	Simple ATM Controller		
   ======================================
   jointed accounts:3
   
   Access via
   1. Card Number
   
   If you don't have any account,
   2. New Account
   
   3. Exit
   
   >>
   ```

   

2. **Access via Card Number**

   - 2-1. When you enter '1', you can access your account using **card_id & pin_number**

       ```bash
       >>1
       insert card number: 3020
       pin_number: 1111
       ```

   - 2-2. And then, choose which you want to transaction with(enter the **account id**). you can do the three things(See balance, Deposit, Withdraw).

       ```bash
       =======Select_A_Account========
       0. account: cun	id: 420538
       -
       1. account: cun2	id: 405739
       -
       2. account: cun3	id: 487215
       -
       3. account: cun4	id: 419802
       -
       4. account: cun6	id: 802593
       -
       ===============================
       enter account_id
       >>802593
       Choose What you want to
       1. See balance
       2. Deposit
       3. WithDraw
       >>
       ```

       - *See Balance*

           ```bash
           >>1
           balance: $10
           ```
   
       - *Deposit*

           ```bash
           >>2
           balance: $10
           how much do you want to deposit?
           >>10
           $10 deposited. balance: $20
           ```
       
       - *Withdraw*

           ```bash
           >>3
           balance: $20
           how much do you want to withdraw?
           >>10
           $10 withdrawed. balance: $10
           ```

   

3. **Create New Account**

   - When you have a card already, enter **'y'** for your connection w/ your other accounts.

       ```bash
       >>2
       Do you have a card?(y/n)
       >y
       card_id: 3020
       pin_number: 1111
       account_name: cun7
       initial deposit: 10
       -
       name: cun7	accound_id: 164171
       card_id: 3020	balance: 10
       new account created.
        you should keep the card number.
       -
       ```
   
       - please, keep your **card_id** !!! if you couldn't remember, you can see on the db_manager.

   - If you don't have any account, enter **'n'**
   
       ```bash
       >>2
       Do you have a card?(y/n)
       >n
       account_name: cun8
       pin_number: 1111
       pin_number confirm: 1111
       initial deposit: 10
       - 
       name: cun8	accound_id: 241330
       card_id: 2189	balance: 10
       new account created.
        you should keep the card number.
       ```
       
       - please, keep your **card_id** !!!
   
   

### db_manager.py

It is not for normal user. *for maintenance*.

1. **Show DB Table**

   ```bash
   1. db_table, 2. delete_account, 3. exit
   >1
   ======================ACCOUNTS TABLE========================
   0. account: cun	 id: 420538	 card_id: 3020	 balance: $30	
   1. account: cun2	 id: 405739	 card_id: 3020	 balance: $10	
   2. account: cun3	 id: 487215	 card_id: 3020	 balance: $50	
   3. account: cun4	 id: 419802	 card_id: 3020	 balance: $50	
   4. account: cun5	 id: 199195	 card_id: 3020	 balance: $50	
   5. account: cun6	 id: 802593	 card_id: 3020	 balance: $10	
   ============================================================
   ```

   

2. **Delete Account**

   ```bash
   1. db_table, 2. delete_account, 3. exit
   >2
   plz type the account_id what you want to delete
   >199195
   1. db_table, 2. delete_account, 3. exit
   >1
   ======================ACCOUNTS TABLE========================
   0. account: cun	 id: 420538	 card_id: 3020	 balance: $30	
   1. account: cun2	 id: 405739	 card_id: 3020	 balance: $10	
   2. account: cun3	 id: 487215	 card_id: 3020	 balance: $50	
   3. account: cun4	 id: 419802	 card_id: 3020	 balance: $50	
   4. account: cun6	 id: 802593	 card_id: 3020	 balance: $10	
   ============================================================
   ```

   