from flask import Flask, render_template, request, jsonify, redirect, url_for
import connection  # Importa la función conectar_db desde database.py

app = Flask(__name__)
con = connection.conectar_db()

@app.route('/')
def index():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cine.usuarios")
    data = cursor.fetchall()
    users = []
    for i in range(0, len(data)):
        users.append(data[i][1])
    return render_template('index.html', users=users)

@app.route('/home/<user>')
def principal(user):
    user_title = user.title()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cine.peliculas")
    data = cursor.fetchall()
    peliculas = []
    for i in range(0, len(data)):
        peliculas.append((data[i][1], data[i][5]))
    return render_template('principal.html', usuario = user_title, peliculas = peliculas)

# ========= Peliculas =========
# Abrir pagina web
@app.route('/home/<user>/<pelicula>')
def webPeli(user, pelicula):
    user_title = user.title()
    archivo = pelicula
    palabras = pelicula.split("-")  # Dividir la cadena en palabras usando "-" como separador
    texto_formateado = " ".join(palabra.lower().title() for palabra in palabras)
    return render_template('pelicula.html', contenido = texto_formateado, archivo = archivo, usuario = user_title)

# Pedir pelicula
@app.route('/getPeli', methods = ['POST'])
def getPeli():
    data = request.json
    id = data.get('id')
    resultado = con.getPeli(con, id)
    print(resultado)
    return jsonify(resultado)

""" METODO AÑADIR A LA BASE DE DATOS
@app.route('/insertar', methods=['POST'])
def insertar():
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        nombre = request.form['nombre']
        cursor.execute("INSERT INTO tu_tabla (nombre) VALUES (%s)", (nombre,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        return "Error al conectar a la base de datos"
"""

"""  METODO BORRAR DE LA BASE DE DATOS
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tu_tabla WHERE id = %s", (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        return "Error al conectar a la base de datos"
"""

@app.errorhandler(404)
def page_not_found(error):
    return render_template('pnf.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
