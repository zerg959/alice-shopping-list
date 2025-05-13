import sqlite3
import os

DB_PATH = os.path.join("instance", "shopping.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS lists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

def save_list(user, content):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO lists (user, content) VALUES (?, ?)', (user, content))
        return cur.lastrowid

def get_all_lists(user=None):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        if user:
            cur.execute('SELECT id, content FROM lists WHERE user=? ORDER BY id DESC', (user,))
        else:
            cur.execute('SELECT id, user, content FROM lists ORDER BY id DESC')
        return cur.fetchall()

def update_list(list_id, new_content):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute('UPDATE lists SET content=? WHERE id=?', (new_content, list_id))
        return cur.rowcount > 0