import db, get_user

def remove_user(usuario):
    conn, cursor = db.get_connection()
    if conn is not None and cursor is not None:
        try:
            if usuario in [user[0] for user in get_user.get_users()]:
                cursor.execute("DELETE FROM users WHERE usuario = (?)", (usuario,))
                conn.commit()
                return 200
            else:
                return 409
        except Exception as e:
            print(e)
            return 500
        finally:
            conn.close()
