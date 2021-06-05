import database # This attempts to import database.py and not a library (unless database.py cannot be found)
import string  # Importing string (pretty sure its a class). https://docs.python.org/3/library/string.html
import random # Import random which is a library that generates a random 'choice' (random is a class, choice is a method)
from flask import jsonify # Not used here so should have been deleted. 


client = database.connect() # Call the function 'connect' in database.py which returns 
crypto_wallets = client["bank"]["crypto_wallets"] # Define a new variable (crypto_wallets), which using the connect function, finds the database "bank" and the collection crypto_wallets  within bank

class CryptoWallet: #Define a new class called CryptoWallet
    """ A class used to represent a cryptocurrency wallet. 
    
    Args:
        coin: type of the cryptocurrency - Bitcoin, Ethereum.
        balance: initial balance that the user will be provided with (in case of promotions)
        transactions: list of transactions that the wallet has (not implemented). 
    """ #Docstring

    def __init__(self, coin, balance): # When we define a new instance and the function will run only once.
        self.coin = coin  #Define variable coin and others
        self.address = self.generate_address()
        self.balance = balance
        self.transactions = [] #Define an empty list (transactions)

    def store_account(self): #Defines the store_account method
        """ Inserts the newly created crypto wallet into the crypto_wallets collection.  """
        return crypto_wallets.insert_one(self.create_account_object()) #Only called once, we get the collection and call the function insert_one to which we provide what create_account_object returns which returns a dictionary see line 29, which is then used to insert a wallet. It's stored in the database so it's saved properly in case of the instance being closed

    def create_account_object(self): #Define the create_account_object method which uses the values provided in like 40 (in practice this happens in another file)
        """ Creates a new account object, will be user to store this into the crypto_wallets collection.  """
        return {"coin_id": self.coin, "address": self.address, "balance": self.balance, "transactions": self.transactions} # Return a dictionary with the coin a random address, the balance and the transactions list ()nonfunctional, we nonly have BTC but this isn't hardcoded to futureproof code. 


    @staticmethod # We dont need to create a new instance to run this, so we do not need to create a new wallet to generate an address. 
    def generate_address(): #Define the generate_address method
        """ Proof of concept function, in reality an actual wallet will be created for the user. """ # Docstring
        return "".join((random.choice(string.ascii_lowercase) for _ in range(34))) # This is another way to merge text, see line 39 and down, we could have done this in a for loop, it passes a 34length string of lowercase letter , there's no check to see if it exists. 
        
def alternative_generate_address(): # exact same thing but easier to understand
    output = ""
    for _ in range(34):
        output += random.choice(string.ascii_lowercase)
            
##wallet = CryptoWallet("BTC", 200.00) # This will create a new instance, AND run __init__ method.
#CryptoWallet.generate_address()

fruits = ["apple", "banana", "pear"]

print("---".join(fruits))
#output is apple---banana---pear