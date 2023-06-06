
print("="*50)
print(" " * 20, "RESULTATS", " " * 20)
print("="*50)

# Funció de la calculadora
def funcio_calculadora(n1, n2, operador):

    if n2 == 0 and operador == '/':
        raise ZeroDivisionError("Error: Un número no es pot dividir entre 0")
    elif operador == '+':
        resultat = n1 + n2
        print(n1, operador, n2, "=", resultat)
        return resultat
    elif operador == '-':
        resultat = n1 - n2
        print(n1, operador, n2, "=", resultat)
        return resultat
    elif operador == '*':
        resultat = n1 * n2
        print(n1, operador, n2, "=", resultat)
        return resultat
    elif operador == '/':
        resultat = n1 / n2
        print(n1, operador, n2, "=", resultat)
        return resultat
    
# Obrir el fitxer en mode lectura
txt = open('calculs.txt', 'r') 
linias = txt.readlines()

# Separar els números i operadors del txt en cada línia
for linia in linias:
    elements = linia.split()
    n1 = int(elements[0])
    operador = elements[1]
    n2 = int(elements[2])

    # Passar cada línia per la funció i guardar els resultats en la llista creada
    resultat = funcio_calculadora(n1, n2, operador)

# Tancar el fitxer
txt.close()

print("="*50)
print("\n")


