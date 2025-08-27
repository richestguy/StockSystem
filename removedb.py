import db
import nomedb

def remove_item(item):
    conn, cursor = db.get_connection()
    if conn is not None and cursor is not None:
        try:
            if item not in [item[0] for item in nomedb.get_produtos()]:
                return 404
            else:
                cursor.execute("DELETE FROM produtos WHERE nome = ?", (item,))
                conn.commit()
                return 200
        except Exception as e:
            print(f"Erro ao remover item: {e}")
            return 500
        finally:
            conn.close()
    else:
        return 500