#Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo (soma de todos os lados) e apresente a mensagem:

#Perimetro = XX.X

#Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem:

#Area = XX.X

#Fórmula da área de um trapézio: AREA = ((A + B) x C) / 2

#Entrada
#A entrada contém três valores reais.

#Saída
#O resultado deve ser apresentado com uma casa decimal.

#RESOLUÇÃO DIO.ME3
lados = [float(x) for x in input().split()]

a = lados[0];
b = lados[1];
c = lados[2];

if a + b > c and a + c > b and b + c > a:
    #TODO Preencha a formula do perímeto do triangulo (soma de todos os lados).
    perimetro = (a + b + c)
    print(f"perimetro = { perimetro :.1f}")
else:
    #TODO Preencha a formula da área do trapézio: AREA = ((A + B) x C) / 2
    area = ((a + b) * c) /2
    print(f"area = { area :.1f}")