from poloczenie import connection
from db_query import get_users, add_user
INTERFACE = """
1 - wypisz uzytkowników
2 - dodaj użytkownika
3 - wyjdz z programu

"""
conn = connection()
while True:
    opcja = input(INTERFACE)
    if opcja == "1":
        result = get_users(conn)
        for item in result:
            print(item)
    elif opcja == '2':
        username = input("podaj nazwe użytkownika\n")
        add_user(username, conn)
    elif opcja == '3':
        print("do widzenia")
        break
    else:
        print("nie znam tej komendy")
conn.close()