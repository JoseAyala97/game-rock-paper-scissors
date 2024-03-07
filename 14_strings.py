"""
in = verifica que un subtexto o caracter este dentro de una cadena de texto
len = verifica el largo de una palabra
"""
text = 'Ella sabe programar en Python'
'''
print('JavaScript' in text)
print('Python' in text)
if 'Python' in text:
  print('Elegiste bien!!')
else:
  print('también elegiste bien')
''' 
"""
Metodos:
.upper() mayusculas
.lowe() minuscula
.count(' ') Contará el caracter que se pida
.swapcase() las mayusculas a minusculas y las minusculas a mayusculas
startswith('') palabara con la que inicia
endswith('') palabra con la que finalice
replace('','') remplaza palabara
.capitalize() primer caracter en mayuscula
.title() primer letra de cada palabra en mayuscula
.isdigit() evalua si es un digito
"""
size = len('amor')
print(text.upper())
print(text.lower())
print(text.swapcase())
print(text.startswith('python'))
print(text.endswith('arbol'))
print(text.replace('Python','java'))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print('398'.isdigit())