#and condiciones usadas deben ser ciertas
print('AND')
print('True and True=>', True and True)
print('True and False=>', True and False)
print('False and True=>', False and False)
print('False and False=>', False and False)
print('*'*11)
print(10>5 and 5<10)

stock = input("Ingrese el número de stock =>")
stock = int(stock)
print(stock >= 100 and stock<=1000)

#or Solo una de las condiciones debe cumplirse
print('OR')
print('True or True=>', True or True)
print('True or False=>', True or False)
print('False or True=>', False or True)
print('False or False=>', False or False)

role =input('Digita el rol => ')
print(role == 'admin' or role == 'seller')