#importamos libreria
import getpass
from string import ascii_lowercase as abecedario

#declaramos variables
intentos = 0
todas_encontradas = 1
password = getpass.getpass('Ingresa contraseña: ')

# compara la password con el abecedario y cuenta los intentos
for letra_password in password:
    encontrado = 1
    for letra_abecedario in abecedario:
        intentos += 1
        if letra_password == letra_abecedario:
            encontrado = 1
            break
    if not encontrado:
        todas_encontradas = 0
        break

#output
if todas_encontradas:
    print(f'Se adivinó la palabra en {intentos} intentos.')
    print(f'La contraseña es: {password}')
else:
    print(f'No se pudo adivinar la contraseña.')
