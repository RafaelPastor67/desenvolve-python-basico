#transformando em código o fluxograma
#Este código o usúario digita quantos números serão analisados e então ele insere essa quantidade de valores e o programa dirá qual o maior
n = int(input("Digite um valor: "))
maior = 0
while n>0:
    x=int(input('Digite um valor para X: '))
    if x>maior:
        maior = x
    n=n-1
print(maior)