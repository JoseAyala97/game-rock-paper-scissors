'''
listas
'''
numbers = [1,2,3,4]
print(type(numbers))
print(numbers)

tasks = ['lavar los platos','jugar videogames']
print(type(tasks))
print(tasks)

types = [1, True,'hola']
print(types)

print(numbers[0])
print(tasks[1])
#Los strings son inmutables
tasks[0]= 'ver platzi'
print(tasks)

print('*' * 50)
print(numbers[0:3])
print(True in types)
print('Hola' in types)