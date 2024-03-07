'''
tuplas = inmutables
se declara con parentesis()
'''
numbers = (1,2,3,5)
sstrings = ('jose','mari','santi','jose')
print(numbers)
print(type(numbers))
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print('*' * 10)
print(sstrings)
print(type(sstrings))
'''
Metodos de la tupla
'''
#index() buscar posición del elemento
print(sstrings)
print(sstrings.index('mari'))
#count() contar cuántas veces hay un elemento en la tupla
print(sstrings)
print(sstrings.count('jose'))
#transformación entre tupla y lista
#metodo list()
my_list = list(sstrings)
print(my_list)
print(type(my_list))
my_list[-1] = 'pedro'
print(my_list)
#transformación entre tupla y lista
#metodo tuple()
my_list = tuple(my_list)
print(my_list)
print(type(my_list))