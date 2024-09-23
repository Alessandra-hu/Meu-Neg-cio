# Criar um programa de usuários...
print("Digite sua nota 1:")
NOTA1 = int(input())
print("Digite a nota 2:")
NOTA2 = int(input())
print("Digite a nota 3:")
NOTA3 = int(input())
print("Digite a nota 4:")
NOTA4 = int(input())

#calcular média...
MEDIA = (NOTA1 + NOTA3 + NOTA4)/4

if MEDIA >= 6:
    print("Aluno aprovado!")
elif MEDIA < 6:
    print("Aluno reprovado!")

print ("boa sorte!")

