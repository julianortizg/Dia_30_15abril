import re
# revisar si un patrón aparece al inicio de un texto
a = re.match(r'Prog', 'Programar es fácil y divertido')
print(f"Esto es a: {a}")

# los objetos de las expresiones regulares son "truthy"
if a:
  print("Texto encontrado \n")
else:
  print("Texto no encontrado \n")

b = re.match(r'diver', 'Programar es fácil y divertido')
print(f"Esto es b: {b}")

# los objetos de las expresiones regulares son "truthy"
if b:
  print("Texto encontrado \n")
else:
  print("Texto no encontrado \n")

# mostrar el texto encontrado
print ('El texto encontrado es:', a.group(0), '\n')

# indicar dónde inicia el texto encontrado
print('El texto encontrado inicia en la posición:', a.start(),'\n' )

# indicar dónde termina el texto encontrado
print('El texto encontrado termina en la posición:', a.end(),'\n' )