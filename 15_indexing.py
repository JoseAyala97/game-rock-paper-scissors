'''
indexing = muestra la posición que se solicite
slicing = de una posición a otra 
'''
text = 'Ella sabe python'
#indexing
print(text[0])
print(text[1])
print(text[6])
size = len(text)
print('size =>',size)
print(text[-1])
print(text[size - 1])
#slicing
print(text[0:7])