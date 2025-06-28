import sqlite3


def init_db():

    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )"""
    ) 
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS interface_elements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS properties_of_elements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS property_range (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property TEXT NOT NULL,
            ranges TEXT NOT NULL,
            FOREIGN KEY (property) REFERENCES properties_of_elements (name) ON DELETE CASCADE
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS element_properties_definition (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            element_id INTEGER,
            property_id INTEGER,
            property_value TEXT,
            FOREIGN KEY(element_id) REFERENCES interface_elements(id),
            FOREIGN KEY(property_id) REFERENCES properties_of_elements(id)
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS alternatives (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alternative_name TEXT NOT NULL,
        set_name TEXT NOT NULL, 
        FOREIGN KEY(set_name) REFERENCES definitions(set_name))"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS alternatives (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alternative_name TEXT NOT NULL,
        set_name TEXT NOT NULL, 
        FOREIGN KEY(set_name) REFERENCES definitions(set_name))"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS alternative_elements (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        alternative_id INTEGER, 
        element_property_id INTEGER, 
        FOREIGN KEY(alternative_id) REFERENCES alternatives(id), 
        FOREIGN KEY(element_property_id) REFERENCES defining_element_properties(id))"""
    )

    # Создание таблицы пользователей
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )"""
    )

    # Создание таблицы групп элементов
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS group_elements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alternative_name TEXT NOT NULL,
            element_name TEXT NOT NULL,
            property_name TEXT NOT NULL,
            property_value TEXT NOT NULL,
            FOREIGN KEY (alternative_name) REFERENCES alternatives (alternative_name) ON DELETE CASCADE
        )"""
    )

    # Добавление тестового пользователя (admin/admin)
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", "admin")
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Пользователь уже существует

    conn.commit()
    conn.close()


def init_db_data_editor():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS ontologies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )"""
    )

    
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS sorts (
            CREATE TABLE IF NOT EXISTS ontology_sorts (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            ontology_name TEXT,
            term TEXT, 
            sort TEXT, 
            UNIQUE(ontology_name, term, sort),
            FOREIGN KEY(ontology_name, term) REFERENCES ontology_terms(ontology_name, term));"
        )"""
    )


    cursor.execute(
        """CREATE TABLE IF NOT EXISTS ontology_terms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ontology_name TEXT NOT NULL,
            term TEXT NOT NULL,
            FOREIGN KEY (ontology_name) REFERENCES ontologies (name) ON DELETE CASCADE
        )"""
    )



    conn.commit()
    conn.close()
