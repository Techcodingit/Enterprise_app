from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO data (name) VALUES (?)', ('Enterprise Item 1',))
    cursor.execute('INSERT INTO data (name) VALUES (?)', ('Enterprise Item 2',))
    conn.commit()
    conn.close()

@app.route('/api/data')
def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    data = cursor.fetchall()
    conn.close()
    return jsonify([{'id': row[0], 'name': row[1]} for row in data])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

