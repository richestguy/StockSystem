import db

def get_users():
    conn, cursor = db.get_connection()
    if conn is not None and cursor is not None:
        try:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []
        finally:
            conn.close()