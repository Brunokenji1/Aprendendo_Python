notas = input("Digite a nota de todos da turma separado por virgula: ").split(', ')
notas = [float(nota) for nota in notas]

media = sum(notas) / len(notas)

print(f'Media: {media:.2f}')
