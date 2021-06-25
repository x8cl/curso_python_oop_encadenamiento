class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount     
        return self

    def transfer_money(self, other_user, amount):
    	#self.account_balance -= amount
        #other_user.account_balance += amount
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

    def display_user_balance(self):
        reporte = ("-")*30 + "\n"
        reporte += "Nombre\t:" + self.name + "\n"
        reporte += "Saldo\t: $" + str(self.account_balance)
        return reporte


usuario1 = User("Juan Perez","jperez@gmail.com")
usuario2 = User("Marcelo Soto","msoto@gmail.com")
usuario3 = User("Mauricio Abarca","mauricio@sektorweb.cl")


#Depositos usuario1
usuario1.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(300)
#Saldo usuario1
print(usuario1.display_user_balance())

#Depositos usuario2
usuario2.make_deposit(100).make_deposit(200).make_withdrawal(100).make_withdrawal(100)
#Saldo usuario2
print(usuario2.display_user_balance())

#Depositos usuario3
usuario3.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).make_withdrawal(150)
usuario3.make_withdrawal(100)
#Saldo usuario3
print(usuario3.display_user_balance())

#Transferencia usuario1 a usuario3
usuario1.transfer_money(usuario3, 50)
print("\n" + ("*")*30 + "\n" + "Despues de Transferencia")
print(usuario1.display_user_balance())
print(usuario3.display_user_balance())
