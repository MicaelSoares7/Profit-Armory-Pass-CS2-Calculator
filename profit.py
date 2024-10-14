# O obijetivo é calcular o maior lucro possível no passe atual, sabendo a quantidade de cada item e que só temos 40 pontos por passe.
# Qual vou lucrar mais, digite os valores levando em consideração a taxa da venda da steam!.

passe = 88.99
estrela = 40


desert = 25
box = 2
chaveiros = 3
stiker = 1


precod = (desert/estrela)*passe
precob = (box/estrela)*passe
precoc = (chaveiros/estrela)*passe
precos = (stiker/estrela)*passe

print("Preço calculado em cima do valor do passe!")
print("+------------------+>")
print(f"|Desert: R$ {precod:.2f}")
print(f"|Caixa: R$ {precob:.2f}")
print(f"|Chaveiro: R$ {precoc:.2f}")
print(f"|Stiker: R$ {precos:.2f}")
print("+------------------+>")

d = int(input("Digite o quantidade de desert: "))
b = int(input("Digite o quantidade de caixa: "))
c = int(input("Digite o quantidade de chaveiro: "))
s = int(input("Digite o quantidade de stiker: "))


pontos = (d*desert) + (c*chaveiros) + (b*box) + (s*stiker)
falta = pontos-estrela
sobra = estrela-pontos

print("")
if estrela-pontos <= 0:
    print(f"Vai custar: {pontos} pontos e você precisará de mais: {falta} pontos")
else:
    print(f"Vai custar: {pontos} pontos e vai sobrar: {sobra} pontos")
print("")

if (d or b or c or s) > 0:
    if d > 0:
        for i in range(d):
            precod = float(input("Digite o valor atual da desert: "))

    if b > 0:
        precob = float(input("Digite o valor atual da caixa: "))

    if c > 0:
        for i in range(c):
            precoc = float(input("Digite o valor atual do chaveiro: "))

    if s > 0:
        for i in range(s):
            precos = float(input("Digite o valor atual do stiker: "))
    
    total = (precod * d) + (precob * b) + (precoc *c) + (precos * s)
    lucro = total-passe
    perda = passe-total

    print("")
    print(f"Você receberá o total de R$ {total:.2f}")
    if lucro > 0:
        print(f"Seu lucro será de R$ {lucro:.2f}")      
    else:
        print(f"Você não terá lucro! Você perdeu R$ {perda:.2f}")  
else:
    print("Nenhum item selecionado...")