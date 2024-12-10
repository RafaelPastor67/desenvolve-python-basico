def validador_senha(a):

    especiais = '!@#$%&*'
    p1,p2,p3,p4,p5 = False,False,False,False,False

    if len(a) >= 8:
        p1 = True 
    
    for caracteres in senha:
        if caracteres.isupper()== True:
            p2 = True
        elif caracteres.islower()== True:
            p3 = True
        elif caracteres.isdigit()== True:
            p4 = True
        elif caracteres in especiais:
            p5 = True
    if p1 and p2 and p3 and p4 and p5 == True:
        return True
    else:
        return False
##########################################################

while True:

    senha = input("Insira uma senha: ")

    if senha == '0':
        print("Programa encerrado")
        break

    if validador_senha(senha) == True:
        print("Senha válida!")
    else:
        print("Senha Inválida")

    