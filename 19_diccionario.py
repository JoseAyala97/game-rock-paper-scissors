'''
Buscar un valor
llave key
valor definition
'''
my_dict = {}
print(type(my_dict))
my_dict = {
  'name': 'Jose', 
  'Last_name': 'ayala',
  'age': '25'
}
print(my_dict)
print(len(my_dict))
print(my_dict['name'])
'''
mejor mostrar con get, debido a que si se ingresa un valor que no existe mostraría none
'''
print(my_dict.get('agi'))
print(my_dict.get('age'))

print('-'*10)