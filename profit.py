#O obijetivo é calcular o maior lucro possível no passe atual, sabendo o quantidade de cada item e que só temos 40 pontos por passe.
# Qual vou lucrar mais, levando em consideração a taxa da venda da steam.

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

print("")
print(f"Vai custar {pontos} pontos e vai faltar: {estrela-pontos}")
if (d or b or c or s) > 0:
    if d > 0:
        precod = float(input("Digite o valor atual da desert: "))
    if b>0:
        precob = float(input("Digite o valor atual da caixa: "))
    if c>0:
        precoc = float(input("Digite o valor atual do chaveiro: "))
    if s>0:
        precos = float(input("Digite o valor atual do stiker: "))
    
    total = (precod * d) + (precob * b) + (precoc *c) + (precos * s)
    lucro = total-passe

    print("")
    print("Você receberá o total de R$", total)
    print(f"Seu lucro será de R$ {lucro:.2f}")        
else:
    print("Nenhum item selecionado...")