name = "Nicolas"
last_name= "Ayala"
my_age = 25
print(name)
print(last_name)
full_name = name + " " + last_name
print(full_name)
quote = "I'm Nicolas"
quote2= "She said 'hello' "
print(quote)
print(quote2)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("v2", template)
#f al inicio
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3", template)
template = f"Hola, mi nombre es {name+' '+last_name} y mi edad es {my_age}"
print("Reto ", template)