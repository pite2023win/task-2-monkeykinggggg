# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.


class Client():
    def __init__(self,name,surname,age,money,id):
        self.name=name
        self.surname=surname
        self.age=age
        self.money=money 
        self.id=id 
            

class Bank(Client):
    def __init__(self,badge):
        self.badge=badge
        self.list_of_members=[]

    def add_client(self,name,surname,age,money):
        self.list_of_members.append(Client(name,surname,age,money))    

    def transfer(id1,id2,how_much):
        if how_much<=list_of_members[id1].money:
            list_of_members[id1].money-=how_much
            list_of_members[id2].money+=how_much 
        pass

    def cash_input(self):
        pass

    def withdrawal(self):
        pass

if __name__=='__main__':

    Merlot=Bank()
    client1=Merlot.add_client(self,"Robert","Smith",40,20000,1)
    client2=Merlot.add_client(self,"Anna","Kowalska",35,10000,2)
    client1.transfer(100,client2)
    

