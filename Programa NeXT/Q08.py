# Crie uma lista de locais que você gostaria de conhecer no mundo, na ordem do local que você dá mais prioridade para o local que você dá menos prioridade. Exiba a lista nas seguintes configurações:
#a) ordem original
#b) ordem alfabética
#c) ordem de prioridades inversa
#d) quantidade de itens

locais = ['italia', 'liverpool', 'disney', 'hard rock stadium' ]

print(locais)

locais_alfa = sorted(locais)
print(locais_alfa)

locais.reverse()
print(locais)

print(len(locais))