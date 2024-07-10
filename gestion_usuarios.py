import hashlib
import sqlite3
from flask import Flask, request
app = Flask(__name__)
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (nombre TEXT, password_hash TEXT)''')
usuarios = [("Martin Cuadros", "cisco123"), ("Jose Padilla", "cisco123"), ("Matias Alfaro", "cisco123")]
for usuario in usuarios:
    nombre, password = usuario
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?,?)", (nombre, password_hash))
conn.commit()
conn.close()
@app.route('/login', methods=['POST'])
def login():
    nombre = request.form['nombre']
    password = request.form['password']
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE nombre=? AND password_hash=?", (nombre, password_hash))
    if c.fetchone():
        return "Login exitoso"
    else:
        return "Login fallido"
if __name__ == '__main__':
        app.run(port=5800)

