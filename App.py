from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
from flask import g

DATABASE = 'database.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route('/<int:id>')
def post_view(id):
    post = get_post(id);
    return render_template('post.html', jogos=post)


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM jogos WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


def create_db():
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO jogos (title, content) VALUES (?, ?)",
                ('Ola mundo!', 'Content for the first post')
                )

    cur.execute("INSERT INTO jogos (title, content) VALUES (?, ?)",
                ('Second Post', 'Content for the second post'))

    connection.commit()
    connection.close()


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    jogos = conn.execute('SELECT * FROM jogos').fetchall()
    conn.close()
    return render_template('index.html', jogos=jogos)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=('GET', 'POST'))
def create():
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            link = request.form['link']
            nota = request.form['nota']
            data = request.form['data']

            if not title:
                flash('Title is required!')
            else:
                conn = get_db_connection()

                conn.execute('INSERT INTO jogos (title, content, data, nota, link) VALUES (?, ?, ?, ?, ?)',
                            (title, content, data, nota, link))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
        return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    jogos = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE jogos SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', jogos=jogos)


if __name__ == '__main__':
    app.run()


@app.route('/pesquisa', methods=["POST","GET"])
def pesquisa():
    if request.method == "POST":
        user = request.form["nm"]
        return  redirect (url_for("pesquisa_resultado",resultado=user))
    else:
        return render_template('form-pesquisa.html')

@app.route('/resultado/<resultado>', methods=["POST","GET"])
def pesquisa_resultado(resultado):
    conn = get_db_connection()

    saida = conn.execute("SELECT * FROM jogos WHERE title LIKE :search",
    {"search": '%' + resultado + '%'}).fetchall()
    
    conn.commit()
    conn.close()
    return render_template('resultado_pesquisa.html', resultado = saida)




