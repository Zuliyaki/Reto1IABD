import psycopg2

def conectar_db():
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="192.168.20.196",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None