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
    
    # Listas
    cursorLista = con.cursor()
    cursorLista.execute("SELECT lr.nombre AS nombre_lista, p.titulo AS nombre_pelicula FROM cine.usuarios u INNER JOIN cine.listasreproduccion lr ON u.userid = lr.userid LEFT JOIN cine.peliculasenlistas pl ON lr.playlistid = pl.playlistid LEFT JOIN cine.peliculas p ON pl.movieid = p.movieid WHERE u.nombre like %s", (user_title,))
    listaReproduccion = cursorLista.fetchall()
    dictListas = {}
    for i in range(0, len(listaReproduccion)):
        dictListas[listaReproduccion[i][0]] = []
        if listaReproduccion[i][0] in dictListas:
            dictListas[listaReproduccion[i][0]].append(listaReproduccion[i][1].lower().replace(" ", "-"))
            print(dictListas)
        else:
            dictListas[listaReproduccion[i][0]] = listaReproduccion[i][1].lower().replace(" ", "-")
            print(dictListas)

    print(dictListas)
    
    # Peliculas
    cursorPeli = con.cursor()
    cursorPeli.execute("SELECT * FROM cine.peliculas order by movieid")
    datosPeli = cursorPeli.fetchall()
    peliculas = []
    for i in range(0, len(datosPeli)):
        peliculas.append((datosPeli[i][1], datosPeli[i][5]))
        
    return render_template('principal.html', usuario = user_title, peliculas = peliculas)

# ========= Peliculas =========
# Abrir pagina web
@app.route('/home/<user>/<pelicula>')
def webPeli(user, pelicula):
    user_name = user.title()
    archivo = pelicula
    palabras = pelicula.split("-")  # Dividir la cadena en palabras usando "-" como separador
    texto_formateado = " ".join(palabra.lower().title() for palabra in palabras)
    cursor = con.cursor()
    cursor.execute("SELECT movieid, calificacionpromedio, reproducciones, sinopsis FROM cine.peliculas where titulo = %s", (texto_formateado,))
    data = cursor.fetchall()
    infoPeli = {
        'id': data[0][0],
        'titulo': texto_formateado,
        'valoracion': data[0][1],
        'reproducciones': data[0][2],
        'sinopsis': data[0][3],
        'codaName': archivo
    }
    return render_template('pelicula.html', usuario = user_name, datos = infoPeli)

# Pedir pelicula
@app.route('/getPeliId', methods = ['POST'])
def getPeliId():
    data = request.json
    id = data.get('id')
    resultado = con.getPeliId(con, id)
    print(resultado)
    return jsonify(resultado)

@app.route('/actualizarReproducciones', methods=['POST', 'PUT'])
def actualizar_reproducciones():
    try:
        titulo = request.form['titulo']
        cursor = con.cursor()
        cursor.execute("SELECT reproducciones FROM cine.peliculas where titulo like %s", (titulo,))
        valor_actual = cursor.fetchone()[0]
        nuevo_valor = valor_actual + 1
        cursor.execute("UPDATE cine.peliculas SET reproducciones = %s where titulo like %s", (nuevo_valor, titulo,))
        con.commit()
        cursor.close()
        return str(nuevo_valor)
    except Exception as e:
        # Manejo de errores
        con.rollback()
        return 'Error en la actualización: ' + str(e)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('pnf.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
