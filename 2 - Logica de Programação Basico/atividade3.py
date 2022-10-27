hora = input('Que horas são? ')

if hora.isdecimal():
    hora = int(hora)
    if hora < 6:
        print(f'São {hora} horas! Está de madrugada')
    elif hora <= 12:
        print(f'São {hora} horas! Bom dia!')
    elif hora < 18:
        print(f'São {hora} horas! Boa tarde!')
    elif hora <= 23:
        print(f'São {hora} horas! Boa noite!')
    else:
        print('Digite um horário válido!')
else:
    print('Digite um horário válido!')

'''
try:
    hora = int(hora)
    if hora < 0 or hora > 23:
        print("Digite uma hora válida!'(00 - 23) horas'")
    elif 6 <= hora <= 12:
        print('Bom dia!')
    elif 12 < hora < 18:
        print('Boa tarde!')
    else:
        print('Boa noite!')

except:
    print('Digite uma hora válida!')
'''
