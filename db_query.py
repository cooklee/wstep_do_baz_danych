
def get_users(connection):
    cursor = connection.cursor()
    query = 'SELECT * FROM "user"'
    cursor.execute(query)
    return cursor.fetchall()

