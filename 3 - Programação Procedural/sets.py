#Criando um set em python, (set) significa conjunto.
set1 = {1, 2, 3, 4, 5,}
set2 = set()

#Adicionando um valor ao set.
set2.add(10)
set2.add(20)
set2.add(30)
set2.add(40)
set2.add(2)
set2.add(5)

#Removendo um valor do set.
set2.discard(20)

#Unindo dois sets
set3 = set1 | set2
print(set3)

#Pegando a interseção dos sets
set4 = set1 & set2
print(set4)

#Pegando o valor que existe apenas no primeiro set.
set5 = set1 - set2
print(set5)

#Pegando o valores que não são iguais nos dois sets.
set6 = set1 ^ set2
print(set6)

#Passando um valor iterável para set usando o updat
set7 = set()
texto = 'python'
set7.update(texto)
print(set7)

lista = ['italo', 'yuri', 'sophia', 'lidiane']
set8 = set(lista)
print(set8)
