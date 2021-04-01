from flask import Flask, request
from poloczenie import connection
from db_query import add_user, get_users

app = Flask(__name__)

html = """
    <ul>
        <li><a href="/">Uzytkownicy</a></li>
    </ul>
    <br>
    """


@app.route('/')
def uzytkownicy():
    conn = connection()
    uzytkownicy = get_users(conn)
    u = "<ul>"
    for user in uzytkownicy:
        u += f"<li>{user[0]} {user[1]}</li>"
    u += "</ul>"
    conn.close()
    return html + u


if __name__ == '__main__':
    app.run()
