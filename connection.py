import psycopg2

def conectar_db():
    try:
        conn = psycopg2.connect(
            database="Netflix",
            user="Zuli",
            password="abcd*1234",
            host="192.168.136.133",  # O la dirección IP del servidor PostgreSQL
            port="5432"  # Puerto por defecto de PostgreSQL
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None