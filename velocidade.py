v = float(input('a que velocidade foi o veiculo?: '))
if v <= 80:
    print('estas na velocidade limite')
else:
    print('estas a exeder a velocidade limite por {} km e estas a dever {} euros'.format(v - 80, (v -80) * 2))