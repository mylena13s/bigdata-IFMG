# QUANTIDADE INDERTEMINADA DE NÚMEROS (BREAK)

soma = 0
while True:
    n = float(input('Informe um número: '))
    if n == 0:
        break
    soma = soma + n
print('Soma dos números:', soma)    

# NÃO SOMAR NÚMERO NEGATIVOS (CONTINUE)

soma = 0
while True:
    n = float(input('Informe um número: '))
    if n < 0:
        continue
    if n == 0:
    soma = soma + n
print('Soma dos números:', soma) 

