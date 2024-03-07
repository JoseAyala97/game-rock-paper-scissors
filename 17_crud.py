'''
metodos de listas
'''
numbers = [1,2,3,4,5]
print(numbers[1])
numbers[-1] = 10
print(numbers)
#Metodo append() agregar un elemento al final de la lista

numbers.append(700)
print(numbers)

#metodo insert() agrega elemento donde se ubique

numbers.insert(0, 'hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1','todo 2','todo 3']
new_list = numbers + tasks
print(new_list)

#Metodo index('') para preguntar dónde esta un elemento y reemplazarlo 

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

#Metodo remove('') elimina un elemento especifico buscandolo por el nombre
new_list.remove('todo 1')
print(new_list)

#metodo pop() elimina el último elemento de la lista // si se envia posición elimina ese elemento

new_list.pop()
print(new_list)

print('+' * 50)

new_list.pop(0)
print(new_list)

#Metodo reverse() transforma todo el array, lo cambia de posición

new_list.reverse()
print(new_list)

#Metodo sort() realiza ordenamiento

numbers_a = [1,4,10,20]
numbers_a.sort()
print(numbers_a)
strings = ['sol','fa','la','si']
strings.sort()
print(strings)