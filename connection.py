import psycopg2

def conectar_db():
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="192.168.22.101",  # O la dirección IP del servidor PostgreSQL
            port="5432"  # Puerto por defecto de PostgreSQL
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    
def getPeli(con, nombre):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM %s", ("peliculas",))
    return cursor.fetchall()