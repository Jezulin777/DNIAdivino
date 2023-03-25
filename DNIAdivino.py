
import re

while True:
    dni = input("Introduce tu DNI (con letra): ")
    
    # Comprobamos que el DNI tenga 9 caracteres
    if len(dni) != 9:
        print("El DNI debe tener 9 caracteres. Inténtalo de nuevo.")
        continue
    
    # Comprobamos que los 8 primeros caracteres sean números
    if not dni[:8].isdigit():
        print("Los primeros 8 caracteres del DNI deben ser números. Inténtalo de nuevo.")
        continue
    
    # Comprobamos que la letra sea válida
    letra = dni[-1].upper()
    letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
    if letra not in letras_validas:
        print("La letra del DNI es inválida. Inténtalo de nuevo.")
        continue
    
    # Comprobamos que la letra sea la correcta
    if letras_validas[int(dni[:8])%23] != letra:
        print("El DNI es inválido. Inténtalo de nuevo.")
        continue
    
    # Si llegamos aquí, el DNI es válido
    print("El DNI es válido.")
    
    # Preguntamos si se quiere reiniciar el script
    respuesta = input("¿Quieres comprobar otro DNI? (s/n) ")
    if respuesta.lower() != "s":
        break
