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
        """CREATE TABLE IF NOT EXISTS definitions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            set_name TEXT NOT NULL,
            definition TEXT NOT NULL,
            FOREIGN KEY (set_name) REFERENCES sets (name) ON DELETE CASCADE
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
        """CREATE TABLE IF NOT EXISTS defining_element_properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ui_elements TEXT NOT NULL,
            property_element TEXT NOT NULL,
            FOREIGN KEY (ui_elements) REFERENCES intarface_elements (name) ON DELETE CASCADE,
            FOREIGN KEY (property_element) REFERENCES properties_of_elements (name) ON DELETE CASCADE
        )"""
    )
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
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            FOREIGN KEY (name) REFERENCES ontologies (ontology) ON DELETE CASCADE
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
            ontology_name TEXT NOT NULL,
            term TEXT NOT NULL, 
            sort TEXT NOT NULL, 
            FOREIGN KEY (ontology_name, term) REFERENCES ontology_terms (ontology_name, term) ON DELETE CASCADE,
            UNIQUE(ontology_name, term, sort)
        )"""
    )





    conn.commit()
    conn.close()
