def nota():
	n1= float(input('Digite a nota bimestre 1: '))
	n2 = float(input('Digite a nota bimestre 2: '))
	n3 = float(input('Digite a nota bimestre 3: '))
	n4 = float(input('Digite a nota bimestre 4: '))
	calculo=(n1+n2+n3+n4)/4
	if calculo >=7:
	  print(calculo,'Aluno Aprovado')
	else:
		(calculo,'Aluno Reprovado')



def aluno():
	nome=input('Digite o nome do aluno: ')
	nome=nome.upper()
	turma=input('Digite a turma: ')
	periodo=input('Digite o período: ')
	periodo=periodo.upper()
	print('')
	print(f'Nome: {nome}')
	print(f'Turma: {turma}')
	print(f'Periodo: {periodo}')
	
def recuper():
	rec= input('O aluno fez a prova de recuperação? S/N ')
	rec=rec.upper()
	if rec =='S':
		prova = float(input('Digite o valor da prova de recuperação: '))
		if prova <=5:
			print('Aluno Reprovado.')
		else:
			print('Aluno Aprovado')
	elif rec !='S' and rec !='N':
		print('Invalid')
		
	

print('Escola Aprender')
print('Fechamento de notas')
print('-'*20)
aluno()
nota()
recuper()
new= input('Deseja incluir um novo dado?')
new=new.upper()
while new=='S':
	aluno()
	nota()
	recuper()
	new = input('Deseja incluir um novo dado? S/N')

