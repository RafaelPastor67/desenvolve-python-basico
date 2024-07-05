horas_trabalhadas = [40, 37, 45, 40, 40, 48]
lista_pagamento=[20 * min(x, 40) + 25 * max(0, x - 40) for x in horas_trabalhadas]
print(lista_pagamento)
