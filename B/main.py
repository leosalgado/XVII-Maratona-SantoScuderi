instancias = int(input())
lista = [] * instancias

while(instancias > 0):

  num_palavras, num_linhas = map(int, input().split())

  my_map = {}

  for i in range(num_palavras):
    palavra = input()
    my_map[palavra] = input()

  traducao = [0] * num_linhas

  for i in range(num_linhas):
    traducao[i] = input().split()
    for j in range(len(traducao[i])):
      if traducao[i][j] in my_map:
        traducao[i][j] = my_map[traducao[i][j]]
      
  lista.append(traducao)

  instancias -= 1

for sublista in lista:
  for item in sublista:
    print(' '.join(item))
  print()