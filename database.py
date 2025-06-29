import sqlite3


def migrate_database():
    """Миграция базы данных для исправления структуры таблицы alternative_elements"""
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    
    try:
        # Удаляем старую таблицу alternative_elements если она существует
        cursor.execute("DROP TABLE IF EXISTS alternative_elements")
        
        # Создаем новую таблицу alternative_elements с правильной структурой
        cursor.execute(
            """CREATE TABLE alternative_elements (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            alternative_id INTEGER, 
            element_property_id INTEGER, 
            FOREIGN KEY(alternative_id) REFERENCES alternatives(id), 
            FOREIGN KEY(element_property_id) REFERENCES element_properties_definition(id))"""
        )
        
        # Удаляем старую таблицу group_elements если она существует
        cursor.execute("DROP TABLE IF EXISTS group_elements")
        
        conn.commit()
        print("Миграция базы данных завершена успешно")
    except Exception as e:
        print(f"Ошибка при миграции: {e}")
        conn.rollback()
    finally:
        conn.close()


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

    # Исправленная таблица alternative_elements - теперь ссылается на element_properties_definition
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS alternative_elements (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        alternative_id INTEGER, 
        element_property_id INTEGER, 
        FOREIGN KEY(alternative_id) REFERENCES alternatives(id), 
        FOREIGN KEY(element_property_id) REFERENCES element_properties_definition(id))"""
    )

    # Создание таблицы пользователей
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
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
        """CREATE TABLE IF NOT EXISTS ontology_terms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ontology_name TEXT NOT NULL,
            term TEXT NOT NULL,
            FOREIGN KEY (ontology_name) REFERENCES ontologies (name) ON DELETE CASCADE
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS ontology_sorts (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            ontology_name TEXT,
            term TEXT, 
            sort TEXT, 
            UNIQUE(ontology_name, term, sort),
            FOREIGN KEY (ontology_name, term) REFERENCES ontology_terms(ontology_name, term)
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS screen_forms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            form_name TEXT NOT NULL,
            ontology_term TEXT NOT NULL,
            UNIQUE(form_name)
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS screen_form_definitions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            screen_form_name TEXT NOT NULL,
            alternative_name TEXT NOT NULL,
            FOREIGN KEY (screen_form_name) REFERENCES screen_forms (form_name) ON DELETE CASCADE
        )"""
    )

    conn.commit()
    conn.close()