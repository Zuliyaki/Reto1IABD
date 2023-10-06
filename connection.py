import psycopg2

def conectar_db():
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="192.168.22.35",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    
def getPeliId(con, id):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM peliculas where id = %s", (id,))
    return cursor.fetchall()

def getUsers(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()