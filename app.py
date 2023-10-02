from flask import Flask, render_template, request, redirect, url_for
from connection import conectar_db  # Importa la función conectar_db desde database.py

app = Flask(__name__)

@app.route('/')
def index():
    """
    conn = conectar_db()  # Establece la conexión a la base de datos
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        registros = cursor.fetchall()
        print(reg)
        conn.close()
        return render_template('index.html', registros=registros)
    else:
        # Manejo de error de conexión
        #return "Error al conectar a la base de datos"""
    return render_template('index.html')

@app.route('/home/<user>')
def principal(user):
    user_title = user.title()
    return render_template('principal.html', usuario = user_title)

@app.route('/home/<user>/<pelicula>')
def pelicula(user, pelicula):
    user_title = user.title()
    archivo = pelicula
    palabras = pelicula.split("-")  # Dividir la cadena en palabras usando "-" como separador
    texto_formateado = " ".join(palabra.lower().title() for palabra in palabras)
    return render_template('pelicula.html', contenido = texto_formateado, archivo = archivo, usuario = user_title)


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
