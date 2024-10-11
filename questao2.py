valor = int(input("Digite o numero"))
termo1 = 0
termo2 = 1
termo3 = termo1 + termo2
while termo3 <= valor:
    termo1 = termo2
    termo2= termo3
    termo3 = termo1 + termo2

if(valor == 0 ):
    print("pertence a sequencia de fibonacci")
elif (valor == termo3):
    print("pertence a sequencia de fibonacci")
else:
    print("não pertence a sequencia de fibonacci")
    
