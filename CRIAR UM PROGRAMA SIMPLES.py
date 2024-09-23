# Demostração do uso if/elif/else...
print("Digite a sua idade:")
IDADE = int(input())


if IDADE < 18: 
   print("Você não é maior de idade!")
   print("Não podria realizar a opração")
elif IDADE >= 65:
    print("Você já está pronto para se aposentar?")
    print("podemos oferecer suporte técnico...")
else:
    print("Você é maior de idade.")
    print("portanto, poderá realizar a operação.")

print("Obrigado po optar pelos nossoa serviços!")
