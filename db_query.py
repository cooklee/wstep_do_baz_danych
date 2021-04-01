
def get_users(connection):
    cursor = connection.cursor()
    query = 'SELECT * FROM "user"'
    cursor.execute(query)
    return cursor.fetchall()

def add_user(username, connection):
    cursor = connection.cursor()
    query = f"INSERT INTO \"user\" (username) values ('{username}');"
    cursor.execute(query)