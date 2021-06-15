# Aqui está la sintaxis para crear una clase a la que queremos llamar Usuario:

# class User:
    # pass    # La completaremos en breve

# Y así es como creamos una nueva instancia de nuestra clase:

# michael = User()
# anna = User()

# "método mágico" llamado __init__, método que se llama cuando se instancia un nuevo objeto.

class User:		# declara una clase y dale el nombre User
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

# patrón: self.<<attribute_name_of_your_choosing>>

# Luego, para instanciar un par de nuevos usuarios:

guido = User()
monty = User()

print(guido.name)	# salida: Michael
print(monty.name)	# salida: Michael

guido.name = "Guido"
monty.name = "Monty"

class User:
    def __init__(self, username, email_address):# ahora nuestro método tiene 2 parametros!copy
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		# y el atributo email
        self.account_balance = 0		# el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer paráme

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python

class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # agrega el método deposit 
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# salida: 300
print(monty.account_balance)	# salida: 50

