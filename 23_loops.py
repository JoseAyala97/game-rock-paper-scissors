'''

'''
#creación de matriz [[datos][datos],[datos],[datos]]
matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matriz[0][1])
#Ciclos anidados
for i in matriz:
  print('row',i)
  for j in i:
    print('column',j)