import mariadb

def get_connection():
    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="localhost",
            port=3306,
            database="db1"
        )
        cursor = conn.cursor()
        return conn, cursor
    except mariadb.Error as e:
        print(f"Erro ao conectar: {e}")
        return None, None