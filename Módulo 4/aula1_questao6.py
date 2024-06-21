q_experimentos = int(input("Quantidade de experimentos: "))#pergunta quantos experimetos foram feitos
i = q_experimentos # iguala um iterador a quantidade de vezes
qr, qs,qc = 0,0,0 #definindo variáveis
while i > 0: # Vai repetir esse código até i ser > 0, cada vez que executar o i vai chegar mais perto de 0
    q1=int(input("Qual a quantidade de cobaias? "))
    c=input("Tipo de cobaia('R', 'S' ou 'C')")

    if c == 'R':# se digir R vai adicionar a quantidade de ratos cobaias
        qr += q1
        
    elif c == 'S':# se digir S vai adicionar a quantidade de ratos sapos
        qs += q1
    
    elif c == 'C':# se digir C vai adicionar a quantidade de ratos coelhos
        qc += q1
  
    i-=1 #iterador
total = qr+qs+qc #somatoria
print(f'Total:{total} cobaias')
print(f'Total de coelhos:{qc}')
print(f'Total de ratos:{qr}')
print(f'Total de sapos:{qs}')
print(f'percentual de coelhos:{qc*100/total:.2f}%')#pega a porcentagem de coelhos
print(f'percentual de ratos:{qr*100/total:.2f}%')#pega a porcentagem de ratos
print(f'percentual de sapos:{qs*100/total:.2f}%')#pega a porcentagem de sapos

