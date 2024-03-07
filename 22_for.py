'''
se usa cuando hay un número de elementos o iteraciones dadas por algún elemento
'''
#for (elemento iterador (i)) "in" (range(rango))
''' 
for element in range(1, 20+1):
  print(element)
'''
my_list = [23,45,67,89,43]
for i in my_list:
  print(i)

my_tuple = ('nico','jose','mari')
for i in my_tuple:
  print(i)

product = {
  'name': 'camisa',
  'price':100,
  'stock': 89
}
for i in product:
  print('-'*10)
  print(i, '=>', product[i])

for i, values in product.items():
  print(i,'=>',values)
#lista diccionarios [{}]
people = [
{
  'name':'jose',
  'age':34
},
{
  'name':'zule',
  'age':45
},
{
  'name':'santi',
  'age':4
}
  ]

for person in people:
  print('name =>',person['name'])
