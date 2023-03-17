#Sistema que lê a nota de 2 provas, calcula a média aritmética e imprime uma mensagem informando a situação do aluno
#aprovado, reprovado ou em recuperação

print("Sistema Acadêmico")
#Entrada de Dados

prova1 = float(input("Digite a nota da prova 1: "))
prova2 = float(input("Digite a nota da prova 2: "))

#Processamento
media = (prova1 + prova2)/2
print("Media: ", media)
if(media>=7):
    print("Aluno(a) aprovado(a)")
elif(media<7 and media >=5):
    print("Aluno(a) em recuperação")
else:
    print("Aluno(a) reprovado(a)")