'''
while : mientras que
'''
'''
while  True:
  print('se ejecuto')
'''
'''
counter = 0
while counter < 10:
  counter += 1
  print(counter,'primer while')
'''
'''
counter = 0
while counter <20:
  counter +=1
  if  counter == 15:
    #forma forzada de romper el ciclo while BREAK (dentro de if)
    break
  print(counter)
'''
counter = 0
while counter <20:
  counter +=1
  if  counter <15:
    #continue salta a la siguiente iteración o siguiente ciclo, lo que esta anterior al continue lo ignora
    continue
  print(counter)
  
