import logging
logging.basicConfig(level=logging.INFO)

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.clients = {}
        self.logger = logging.getLogger(name)

    def add_client(self, client):
        self.clients[client.id] = client
        self.logger.info(f"Added client: {client.id}: {client.name} {client.surname}")
      
    def print_client(self, id):
        client = self.clients.get(id,None)
        if client:
            self.logger.info(f"Client information: Bank={self.name}, ID={client.id}, Name={client.name}, Surname={client.surname}")
        else:
            self.logger.warning(f"Id {id} not found in {self.name}")
                

    def create_account(self, account_number, money):
        if account_number not in self.accounts:
            self.accounts[account_number] = money
            self.logger.info(f"Account {account_number} created with an initial balance of ${money} at {self.name}")
        else:
            self.logger.warning(f"Account {account_number} already exists at {self.name}")

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            self.logger.warning(f"Account {account_number} does not exist at {self.name}")
            return None
        
    def add_money(self,account_number,amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            self.logger.info(f"Deposited ${amount} into account {account_number} at {self.name}")
        else:
            self.logger.warning(f"Account {account_number} does not exist at {self.name}")

    def get_money(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                self.logger.info(f"Withdrew ${amount} from account {account_number} at {self.name}")
            else:
                self.logger.warning(f"Insufficient funds in account {account_number} at {self.name}")
        else:
            self.logger.info(f"Account {account_number} does not exist at {self.name}")

    def transfer_within_bank(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account] >= amount:
                self.accounts[from_account] -= amount
                self.accounts[to_account] += amount
                self.logger.info(f"Transferred ${amount} from account {from_account} to account {to_account}")
            else:
                self.logger.warning("The amount is unreachable")
        else:
            self.logger.warning("Could not resolve an operation: clients do not exist in database")        

    def transfer_to_external_bank(self, from_account,to_bank,to_account, amount):
        if not from_account in self.accounts:
            self.logger.info(f"Account does not exist")
        else:
            if self.accounts[from_account]>=amount:
                self.accounts[from_account] -= amount
                to_bank.receive_external_transfer(to_account, amount, self)
            else:
                self.logger.info("Not enought money")

    def receive_external_transfer(self, receiving_account, amount, sending_bank):
        self.accounts[receiving_account]+=amount
        self.logger.info(f"Received ${amount} from {sending_bank.name} ")


class Client():
    def __init__(self,name,surname,id,bank):
        self.name=name
        self.surname=surname
        self.id=id 
        self.bank =bank
        self.bank.add_client(self)
        self.logger = logging.getLogger(f"{__name__}.{name}") 
     
    def create_account(self, account_number, money):
        self.bank.create_account(account_number, money)  

    def get_balance(self, account_number):
        return self.bank.get_balance(account_number)

    def add_money(self, account_number, amount):
        self.bank.add_money(account_number, amount)

    def get_money(self, account_number, amount):
        self.bank.get_money(account_number, amount)   

    def transfer(self, from_account,to_bank, to_account, amount):
        if self.bank == to_bank:
            self.bank.transfer_within_bank(from_account, to_account, amount)
        else:
            self.bank.transfer_to_external_bank(from_account,to_bank, to_account, amount)
        

logger = logging.getLogger(__name__)  
if __name__=='__main__':
    Merlot=Bank("Merlot")
    Superbank=Bank("Superbank")

    client1=Client("Sam","Smith","1111",Merlot)
    client2=Client("Alice","Cocosmith","1231",Merlot)
    client3=Client("Anthony","Hopkins","1333",Superbank)
    client1.create_account("1111", 10000)
    client2.create_account("1231", 5000)
    client3.create_account("1333", 2000)

    client1.transfer("1111",Superbank, "1333", 200)
    logger.info(client1.get_balance("1111"))
    logger.info(client3.get_balance("1333"))

    Merlot.print_client("1111")
    

