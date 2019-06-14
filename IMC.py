peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

resultado = float(peso / altura ** 2)

if resultado > 40.0:
    print(f'Obesidade grave, {resultado}')

if resultado >= 30.0 and resultado <= 39.9:
    print(f'Obesidade, {resultado}')

if resultado >= 25.0 and resultado <= 29.9:
    print(f'Sobrepeso, {resultado}')

if resultado >= 18.5 and resultado <= 24.9:
    print(f'Normal, {resultado}')

if resultado < 18.5:
    print(f'Magreza, {resultado}')















