from flask import Flask, render_template, request, redirect, url_for
from connection import conectar_db  # Importa la función conectar_db desde database.py

app = Flask(__name__)

@app.route('/')
def index():
    """
    conn = conectar_db()  # Establece la conexión a la base de datos
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tu_tabla")
        registros = cursor.fetchall()
        conn.close()
        return render_template('index.html', registros=registros)
    else:
        # Manejo de error de conexión
        return "Error al conectar a la base de datos"
    """
    return render_template('index.html')

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

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
if __name__ == '__main__':
    app.run(debug=True)
