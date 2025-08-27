import db

def check_login(username, password):
    conn, cursor = db.get_connection()
    if conn is not None and cursor is not None:
        try:
            cursor.execute("SELECT * FROM users WHERE usuario = ? AND senha = ?", (username, password))
            user = cursor.fetchone()
            if user:
                return 200
            else:
                return 401
        except Exception as e:
            print(f"Erro ao verificar login: {e}")
            return 500
        finally:
            conn.close()
    else:
        return 500