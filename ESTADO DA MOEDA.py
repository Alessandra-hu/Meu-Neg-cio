# Constua um programa de usuário...
print("Digite o Nome de um filme ")
print("A. Qual seria a nota para avaliar ")
print("B. péssima"," Razoável","boa")
print("C. Avaliação dada ao usuário")
print("D. o usuario podera digitar qualquer valor ")
print("E. ")
ESTADO = int(input())

match ESTADO:
    case "A":
        print("Perfeita! Vou pagar R$ 1.000.000.oo!")
    case "B":
        print("Quase Perfeita! Ofereço R$ 250.000.00!")
    case "C":
        print("Que ótimo! posso dar uns R$ 100.000.00!")
    case "D":
        print("Que bom. Aceitaria R$ 30.000.00?")
    case "E":
        print("Desculpe, não aceito nesse estado.")
    case _ :
        print("Opção não reconhecida!")
