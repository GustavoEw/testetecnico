palavra= input("digite uma palavra: ")
palavra_vetor = []
for a in palavra:
    palavra_vetor.append(a)

quantidade = len(palavra_vetor)-1
palavra_invertida = []
while quantidade >=0:
    palavra_invertida.append(palavra_vetor[quantidade])

    quantidade = quantidade - 1

print(palavra_invertida)
