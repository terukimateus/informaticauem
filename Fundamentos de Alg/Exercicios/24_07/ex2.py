def impostos():
    ''''''

    renda = float(input('Digite sua renda:'))

    if renda <= 1000:
        impostos = renda * 0.05
        renda = renda - impostos
        print(renda)
    elif renda < 4999:
        impostos = ((renda - 1000) * 0.1) + 50
        renda = renda - impostos
        print(renda)
    else:
        impostos = ((renda - 5000) * 0.2) + 450
        renda = renda - impostos
        print(renda)

impostos()