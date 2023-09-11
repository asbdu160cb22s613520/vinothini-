class BankAccount:
 def __init__(self,account_number,account_holder_name,initial_balance=0):
   self._account_number=account_number 
   self._account_holder_name=account_holder_name
   self._account_balance=initial_balance
 def deposit(self,amount):
   if amount>0:
     self._account_balance+=amount
     return True
   else:
     return False
 def withdraw(self,amount):
   if 0<amount<=self._account_balance:
     self._account_balance-=amount
     return True
   else:
     return False
 def display_balance(self):
   return
   self._account_balance
 #testing the BankAccount class
  if _name_=="_main_":
    account=BankAccount("123456789","jhon doe",1000)
    print("Initial balance:",account.display_balance())
  if account.deposit(500):
    print("Deposit sucessful.New balance:",account.display_balance())
  else:
    print("Invalid deposit amount.")
  if account.withdraw(200):
    print("withdrawl suceesful.New balance:",account.display_balance())
  else:
    print(Insuffient balance or invalid withdrawl amount.")
    
  
  
  
 
     