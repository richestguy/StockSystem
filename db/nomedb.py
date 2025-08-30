# nomedb.py
import db 

def get_produtos():
    conn, cursor = db.get_connection()
    if conn is not None and cursor is not None:
        try:
            cursor.execute("SELECT nome FROM produtos")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar produtos: {e}")
            return []
        finally:
            conn.close()
    else:
        return []