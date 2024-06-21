import random
numero = random.randint(0,10)
while True:
    guess = int(input("Adivinhe o número: "))
    if guess == numero:
        print(f"Você acertou, era o número {numero}")
        break
    elif guess > numero: 
        print("Muito alto, tente de novo")
    else:
        print("Muito baixo, tente de novo")