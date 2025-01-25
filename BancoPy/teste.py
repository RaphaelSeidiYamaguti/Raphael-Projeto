from models.cliente import Cliente
from models.conta import Conta


felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '123.456.789-01', '02/09/1987')
angelina: Cliente = Cliente('Angelina Jolie', 'angelinaa.jolie@gmail.com', '123.456.789-01', '02/09/1975')

print(felicity)
print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

print(contaf)
print(contaa)