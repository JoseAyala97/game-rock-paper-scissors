'''

'''
person = {
  'name':'jose',
  'last_name':'ayala',
  'langs':['python','javascript'],
  'age':99
}
print(person)
person['name'] = 'santi'
print(person)
person['age'] -= 50
print(person)
person['langs'].append('rust')
print(person)
#del para eliminar
del person['last_name']
print(person)
#pop para eliminar 
person.pop('age')
print(person)
print('-'*10)
#item mostrará entidad y lo que llevan
print('item')
print(person.items())
#key mostrará solo entidades
print('key')
print(person.keys())
#values mostrará solo valores
print('values')
print(person.values())