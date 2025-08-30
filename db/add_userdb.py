import db,get_user

def add_user(username, senha):
    conn, cursor = db.get_connection()
    if conn is not None and cursor is not None:
        try:
            if username in [user[0] for user in get_user.get_users() ]:
                return 409
            else:
                cursor.execute("INSERT INTO users (usuario, senha) VALUES (?,?)", (username,senha,))
                conn.commit()
                return 200
        except Exception as e:
            return 500
        finally:
            conn.close()