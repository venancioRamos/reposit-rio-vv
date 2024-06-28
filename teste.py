print('MENU')
print('1 - para vou seguir em frente')
print('2 - vou me deter ')
resp = str(input('digite sua resposta'))
while resp not in '12' or len(resp) == 0:
    resp = str(input('digite sua resposta novamente'))
if resp == '1':
    print('você conseguirá , você tem a formula na cabeça')
elif resp == '2':
    print('você irá afundar')
