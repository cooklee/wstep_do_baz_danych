from poloczenie import connection

c = connection()
cursor = c.cursor()
query = """SELECT * FROM "user";"""
cursor.execute(query)
result = cursor.fetchall()
print(result)
for item in cursor:
    print(item)
c.close()