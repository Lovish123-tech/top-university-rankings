import sqlite3

def get_db():
    conn = sqlite3.connect('universities.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db()
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT UNIQUE
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS universities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            institution TEXT,
            rank INTEGER,
            score REAL,
            year INTEGER,
            country_id INTEGER,
            FOREIGN KEY (country_id) REFERENCES countries(id)
        )
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
        create_tables()
        print("Tables created!")