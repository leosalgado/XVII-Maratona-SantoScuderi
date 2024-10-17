quant_casas, quant_encomendas = map(int, input().split())

map_casas = {}

num_casas = list(map(int, input().split()))

for i in range(quant_casas):
  map_casas[num_casas[i]] = i
  if i == 0:
    selected = map_casas[num_casas[i]]

list_encomendas = list(map(int, input().split()))

acum = 0
for encomenda in list_encomendas:
  if encomenda in map_casas:
    acum += abs(selected - map_casas[encomenda])
    selected = map_casas[encomenda]

print(acum)