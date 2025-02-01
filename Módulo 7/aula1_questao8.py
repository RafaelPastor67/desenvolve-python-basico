cpf = input("Digite um CPF, na forma(XXX.XXX.XXX-XX): ")
cpf = cpf.replace(".", "").replace("-", "")

if cpf.isdigit() and len(cpf) == 11:
    verificando_cpf = cpf[:-2]
    
    somatorio=0
    verificador = 2
    for digito in verificando_cpf[::-1]:
        multiplicado = int(digito) * verificador
        verificador += 1
        somatorio += multiplicado
    resto = somatorio % 11
    if resto < 2:
        prox = '0'
    else:
        prox = 11 - resto
        prox = str(prox)
        verificando_cpf += prox
        

    somatorio=0
    verificador = 2
    for digito in verificando_cpf[::-1]:
        multiplicado = int(digito) * verificador
        verificador += 1
        somatorio += multiplicado
    resto = somatorio % 11
    if resto < 2:
        prox = '0'
    else:
        prox = 11 - resto
        prox = str(prox)
        verificando_cpf += prox
    if verificando_cpf == cpf:
        print("CPF válido")
    else:    
        print("CPF inválido")
else:
    print("CPF inválido")