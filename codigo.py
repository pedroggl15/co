def cadastro_aluno(nome,turma,cgm):
  print("0 alunos foi cadastrado!")
  opcao = input("deseja ver o cadastro? digitte 's'p/ ver:")
  if opcao == 's' or opcao == 'S':
    print (f"suas informaçãoes são {nome},{turma},{cgm}")
  else:
    print ("volte mais tarde")
 
nome = str (input("nome:"))
turma = str (input("turma:"))
cgm = str ( input("cgm:"))
