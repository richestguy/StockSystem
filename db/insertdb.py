import db
import nomedb

def add_item(item):
    conn, cursor = db.get_connection()
    if conn is not None and cursor is not None:
        try:
            if item in [item[0] for item in nomedb.get_produtos()]:
                return 409
            else:
                cursor.execute("INSERT INTO produtos (nome) VALUES (?)", (item,))
                conn.commit()
                return 200
        except Exception as e:
            print(f"Erro ao adicionar item: {e}")
            return 500
        finally:
            conn.close()
    else:
        return 500