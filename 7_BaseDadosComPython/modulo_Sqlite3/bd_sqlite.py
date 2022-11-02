import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

"""Criando a tabela."""
# conexao.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                 'nome TEXT,'
#                 'peso REAL'
#                 ')')

"""Formas de Inserir dados na tabela."""
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Italo", 83.5)')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)',
#                ("Lidiane", 64))
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'Sophia', 'peso': 33})
#
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Yuri', 'peso': 70.8})
#
# conexao.commit()

"""Atualizando dados na tabela."""
# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
#                {'nome': 'Lidia', 'id': 2})
# conexao.commit()

# """Deletar um dado na tebela."""
# cursor.execute('DELETE FROM clientes WHERE id=:id',
#                {'id': 2})
# conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    indentificador, nome, peso = linha

    print(f'id: {indentificador}, nome: {nome}, peso: {peso}')

cursor.close()
conexao.close()
