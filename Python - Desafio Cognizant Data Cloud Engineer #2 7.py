#Desafio
#Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Para cada X e Y, escreva uma mensagem para indicar se tais valores foram digitados em ordem crescente ou decrescente.

#Entrada
#A entrada é composta por vários casos de teste. Cada caso contém dois valores inteiros: X e Y. A leitura deve ser encerrada caso sejam fornecidos os mesmos valores para X e Y.

#Saída
#Caso os valores tenham sido digitados na ordem crescente, imprima “Crescente”. No contrário, “Decrescente”.


while True:
  valores = [int(i) for i in input().split()]
  X, Y = valores
  if X==Y:
    break
  elif X>Y:
    print('Decrescente')
  else:
    print('Crescente')