import sqlite3

def init_db():
    import sqlite3
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS definitions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            set_name TEXT NOT NULL,
            definition TEXT NOT NULL,
            FOREIGN KEY (set_name) REFERENCES sets (name) ON DELETE CASCADE
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS properties_of_elements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )"""
    )
    conn.commit()
    conn.close()


def add_set(name):
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sets (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_sets():
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sets")
    sets = [row[0] for row in cursor.fetchall()]
    conn.close()
    return sets

def add_definition(set_name, definition):
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO definitions (set_name, definition) VALUES (?, ?)", (set_name, definition))
    conn.commit()
    conn.close()

def get_definitions():
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM definitions")
    rows = cursor.fetchall()
    conn.close()
    return rows