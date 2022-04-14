import sqlite3
from datetime import datetime

conn = sqlite3.connect('banco_de_jogos_term.db')
cur = conn.cursor()


#funcoes utilizadas para adicionar informacoes

#funcao auxiliar, nao deve ser utilizada
def atualizaNotaJogo(jogo_id):
    cur.execute("SELECT AVG(nota) FROM comentarios JOIN jogo_comentario ON comentarios.comentario_id = jogo_comentario.comentario_id and jogo_id = ?", (jogo_id, ))
    nota = cur.fetchone()[0]
    print(nota)
    cur.execute("UPDATE jogos SET nota = ? WHERE jogo_id = ?", (nota, jogo_id,))
    conn.commit()

#cria nova desenvolvedora
def adicionaDesenvolvedora(nome_desenvolvedora, site_oficial):
    cur.execute(f"INSERT OR IGNORE INTO desenvolvedora (nome_desenvolvedora, site_oficial) VALUES ( ?, ?)", (nome_desenvolvedora, site_oficial))
    conn.commit()

#adiciona comentario pelo usuario
def adicionaComentario(usuario_id, comentario, nota, jogo_id):
    data = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.today().strftime('%H:%M')
    cur.execute("INSERT OR IGNORE INTO comentarios (usuario_id, comentario, nota, data, hora) VALUES ( ?, ?, ?, ?, ?)", (usuario_id, comentario, nota, data, hora))
    cur.execute("SELECT comentario_id FROM comentarios WHERE usuario_id = ? and data = ? and hora = ? ", (usuario_id, data, hora))
    comentario_id = cur.fetchone()[0]
    cur.execute("INSERT INTO jogo_comentario VALUES (?, ?)", (jogo_id, comentario_id))
    atualizaNotaJogo(jogo_id)
    conn.commit()


def adicionaJogo(nome_jogo, desenvolvedor_id, data_lancamento, genero_id, descricao, link_do_jogo):
    cur.execute("INSERT OR IGNORE INTO jogos (nome_jogo, desenvolvedora_id, data_lancamento, genero_id, descricao, link_do_jogo) VALUES ( ?, ?, ?, ?, ?, ?)", (nome_jogo, desenvolvedor_id, data_lancamento, genero_id, descricao, link_do_jogo))
    conn.commit()

def adicionaUsuario(nome, email, senha):
    cur.execute("INSERT OR IGNORE INTO usuario (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
    conn.commit()

def adicionaGenero(nome): 
    cur.execute("INSERT OR IGNORE INTO genero (nome_genero) VALUES (?)", (nome,))
    conn.commit()

def adicionaJogoFav(usuario_id, jogo_id):
    cur.execute("INSERT INTO usuario_jogoFavorito VALUES (?, ?)", (usuario_id, jogo_id))
    conn.commit()


#consultas

#devolve no formato [(nome_jogo, nome_desenvolvedora, data_lancamento, nome_genero, descricao, nota, link_do_jogo), (...), ...]
def pesquisaJogoNome(nome):
    nome = "'%"+nome+"%'"
    cur.execute(f"""SELECT nome_jogo, nome_desenvolvedora, data_lancamento, nome_genero, descricao, nota, link_do_jogo 
    FROM 
    (SELECT nome_jogo, nome_desenvolvedora, data_lancamento, nome_genero, descricao, nota, link_do_jogo
    FROM jogos 
    JOIN desenvolvedora
    JOIN genero
    ON jogos.desenvolvedora_id = desenvolvedora.desenvolvedora_id and jogos.genero_id = genero.genero_id)
    WHERE nome_jogo LIKE {nome}""")
    conn.commit()
    return cur.fetchall()


#devolve no formato [(nome_jogo, nome_desenvolvedora, data_lancamento, nome_genero, descricao, nota, link_do_jogo), (...), ...]
def filtraPorGenero(genero_id):
    cur.execute(f"""SELECT nome_jogo, nome_desenvolvedora, data_lancamento, nome_genero, descricao, nota, link_do_jogo
    FROM jogos 
    JOIN desenvolvedora
    JOIN genero
    ON jogos.desenvolvedora_id = desenvolvedora.desenvolvedora_id and jogos.genero_id = {genero_id} and genero.genero_id = {genero_id}""")
    conn.commit()
    return cur.fetchall()
    

#retorna lista de tuplas no formato [(nome_jogo, nome_desenvolvedora, data_lancamento, nome_genero, descricao, nota, link_do_jogo), (...), ...]
def devolveTodosJogos():
    cur.execute("""SELECT nome_jogo, nome_desenvolvedora, data_lancamento, nome_genero, descricao, nota, link_do_jogo
    FROM jogos 
    JOIN desenvolvedora
    JOIN genero
    on jogos.desenvolvedora_id = desenvolvedora.desenvolvedora_id and jogos.genero_id = genero.genero_id""")
    conn.commit()
    return cur.fetchall()

#retorna lista de tuplas no formato [(nome_jogo, nome_desenvolvedora, data_lancamento, nome_genero, descricao, nota, link_do_jogo), (...), ...]
def devolveJogosFavoritos(usuario_id):
    cur.execute(f"""
    SELECT nome_jogo, nome_desenvolvedora, data_lancamento, nome_genero, descricao, nota, link_do_jogo
    FROM jogos 
    JOIN usuario_jogoFavorito
    JOIN usuario
    JOIN desenvolvedora
    JOIN genero
    ON jogos.jogo_id = usuario_jogoFavorito.jogo_id and usuario_jogoFavorito.usuario_id = usuario.usuario_id 
    and jogos.desenvolvedora_id = desenvolvedora.desenvolvedora_id and genero.genero_id = jogos.genero_id and usuario.usuario_id = {usuario_id}
    """)
    conn.commit()
    return cur.fetchall()


#retorna lista de tuplas no formato [(nome, comentario, nota, data, hora), (...), ...]
def devolveComentariosJogos(jogo_id):
    cur.execute(f"""SELECT usuario.nome, comentario, nota, data, hora 
    FROM comentarios 
    JOIN jogo_comentario 
    JOIN usuario
    ON comentarios.comentario_id = jogo_comentario.comentario_id and usuario.usuario_id = comentarios.usuario_id and jogo_id = {jogo_id}""")
    conn.commit()
    return cur.fetchall()
    
#retonra no formato [(nome_desenvolvedora, site), (...), ...]
def devolveTodasDesenvolvedoras():
    cur.execute("SELECT nome_desenvolvedora, site_oficial FROM desenvolvedora")
    conn.commit()
    return cur.fetchall()

#retonra no formato [(nome_desenvolvedora, site)]
def devolveDesenvolvedoraDeUmJogo(jogo_id):
    cur.execute(f"""SELECT nome_desenvolvedora, site_oficial 
    FROM jogos
    JOIN desenvolvedora
    ON jogos.desenvolvedora_id = desenvolvedora.desenvolvedora_id and jogos.jogo_id = {jogo_id}""")

    conn.commit()
    return cur.fetchall()

#retorna no formato (nome)
def devolveNomeUsuario(usuario_id):
    cur.execute(f"SELECT nome FROM usuario WHERE usuario_id = {usuario_id}")
    conn.commit()
    return cur.fetchone()[0]

#retorna no formato (jogos_id)
def devolveJogoID (nome_jogo):
    nome_jogo = "'%"+nome_jogo+"%'"
    cur.execute(f"SELECT jogo_id FROM jogos WHERE nome_jogo LIKE {nome_jogo}")
    conn.commit()
    return cur.fetchone()[0]

#retorna no formato (usuario_id)
def devolveUsuarioID (nome):
    nome = "'%"+nome+"%'"
    cur.execute(f"SELECT usuario_id FROM usuario WHERE nome LIKE {nome}")
    conn.commit()
    return cur.fetchone()[0]

#retorna no formato (genero_id)
def devolveGeneroID(nome):
    nome = "'%"+nome+"%'"
    cur.execute(f"SELECT genero_id FROM genero WHERE nome_genero LIKE {nome}")
    conn.commit()
    return cur.fetchone()[0]


#funcao que verifica se os dados (e-mail e senha) estao de acordo com o do banco de dados e devolve o usuario_id
def fazLogin(email, senha):
    cur.execute(f"""SELECT usuario_id, nome 
    FROM usuario 
    WHERE email = '{email}' and senha = '{senha}'""")
    try:
        inter = cur.fetchone()[0]
    except:
        inter = 'E-mail ou senha incorretos!'
    return inter

print("\nDesenvolvedores:\n")
inter = devolveTodasDesenvolvedoras()
for i in inter:
    print(i)

print("\nComentarios de um Jogo: \n")
inter = devolveComentariosJogos(1)
for i in inter:
    print(i)


print("\nMostra meus jogos favoritos:\n")
inter = devolveJogosFavoritos(devolveUsuarioID ('Lucas'))
for i in inter:
    print(i[0])

adicionaJogoFav(devolveUsuarioID ('Lucas'),  devolveJogoID ('Dota 2'))

print("\nMostra meus jogos favoritos:\n")
inter = devolveJogosFavoritos(devolveUsuarioID ('Lucas'))
for i in inter:
    print(i[0])