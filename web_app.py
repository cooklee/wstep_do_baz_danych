from flask import Flask, request
from poloczenie import connection
from db_query import get_users, add_user as add_user_to_db, del_user

app = Flask(__name__)

html = """
    <ul>
        <li><a href="/">Uzytkownicy</a></li>
        <li><a href="/add_user">dodaj użytkownika</a></li>
        <li></li>
    </ul>
    <br>
    """


@app.route('/')
def uzytkownicy():
    conn = connection()
    uzytkownicy = get_users(conn)
    u = "<ul>"
    for user in uzytkownicy:
        u += f"""<li>{user[0]} {user[1]} <a href="/delete_user/{user[0]}">usun</a></li>"""
    u += "</ul>"
    conn.close()
    return html + u


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        FORM = """
        <form method='POST'>
            <p> username: <input type='text' name='username'></p>
            <p> <input type='submit'></p>
        </form>
        """
        return html + FORM
    elif request.method == 'POST':
        username = request.form.get('username')
        if username == '':
            return html + "ej no kaman napisz cos"
        conn = connection()
        add_user_to_db(username, conn)
        conn.close()
        return html + "udało sie dodać nowego użytkownika"


@app.route("/delete_user/<int:id>", methods=['POST', 'GET'])
def delete_user(id):
    if request.method == "GET":
        form = """<form method='POST'>
            <input type='submit' name='answer' value='tak'>
            <input type='submit' name='answer' value='nie'> 
            </form>
        """

        return f"Czy jeste pewien, że chcesz usunąć użytkownika od id={id}" + form
    elif request.method == 'POST':
        answer = request.form.get('answer', 'nie')
        if answer == 'tak':
            conn = connection()
            del_user(id, conn)
            conn.close()
            return html + "użytkownik usunięty"
        return html + "rezygnacja z usunięcia"


if __name__ == '__main__':
    app.run()
