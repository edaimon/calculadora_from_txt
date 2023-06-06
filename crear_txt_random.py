import random
with open ('calculs.txt', 'w') as f:
    n = int(input("Quants càlculs tindrà el fitxer calculs.txt? "))
    for i in range(n):
        n1 = random.randint(0,1000)
        n2 = random.randint(0,1000)
        operadores = ['+', '-', '*', '/']
        operador = random.choice(operadores)
        f.write(f"{n1} {operador} {n2}")
        f.write('\n')    
        print("Línia", i+1 , "-->", n1, operador, n2)

# As seen in https://www.youtube.com/watch?v=qdLb0hpuWcI