def notas () -> str:
    ''''''

    m1 = input('Insira sua média 1:')

    m2 = input('Insira sua média 2:')

    m3 = input('Insira sua média 3:')

    m4 = input('Insira sua média 4:')

    nota = float(m1) + float(m2) + float(m3) + float(m4)
    média = nota / 4

    if média >= 70:
        print(f'Você foi aprovada(o)! Sua média é {média}')
    else:
        print(f'Você foi reprovada(o)! Sua média é {média}')

notas()