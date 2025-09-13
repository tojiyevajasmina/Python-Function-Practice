
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def bank_menu(console):

     console.print("____... MENU ...___",style ="bold red")
     console.print("1.Yangi bank hisob raqamini ochish",style = "italic black")
     console.print("2.Pul qo'yish (deposit)",style = "italic yellow")
     console.print("3.Pul yechib olish (withdraw)",style = "italic black")
     console.print("4.Hisobdagi balansni ko'rish",style = "italic yellow")
     console.print("5.Dasturdan chiqish",style = "italic black")
     
def print_newline():
   print()

def create_account(console):
   console.print("Account yarating", style ="yellow")
   name = input("ismingizni kiriting:")
     
   return name 


def diposit(balance):
    amount = float (input("Amount:"))
    if amount >0:
      balance += amount

      return balance 
    

def withdraw (balance):
   amount = float(input("amount"))
   if amount > 0 and amount <= balance:
      balance -= amount

      return balance
   
def chesk_balance(console ,balance):
   console.print(f"sizning balansingiz: {balance}",style = "magenta")

def check_user(user):
   return user is not None


   
def main():
   user = None
   balance = 0

   while True:
      bank_menu(console)

      choice = Prompt.ask("Menyuni tanlang:", choices = "1", "2", "3", "4", "5") 
      
      print_newline()


      if choice == "1":
         user = create_account(console)
         balance = 0
         console.print("account yaratilgan",style = "green")
         print_newline()


      elif choice == "2":
         if check_user(user):
            balance = diposit(balance)
      else:
         console.print("accountingiz yuq", style = "red")
     
           
  
main()