student = input("Qual o nome do aluno: ")
discipline = input("Qual o nome da disciplina: ")
test = float(input(f"Qual foi na nota do {student} na prova: "))
work = float(input(f"Qual foi na nota do {student} no trabalho: "))
project = float(input(f"Qual foi na nota do {student} no projeto: "))

media = (test + work + project) / 3

print(f"A media do {student} é de {media:.2}")

if media > 6:
    print(f"Parabens, você foi aprovado em {discipline}.")
else:
    print(f"Que pena, foi reprovado em {discipline}.")
