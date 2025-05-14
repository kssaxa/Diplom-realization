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
            FOREIGN KEY(set_name) REFERENCES definitions(set_name)
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS alternative_elements (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            alternative_id INTEGER, 
            element_property_id INTEGER, 
            FOREIGN KEY(alternative_id) REFERENCES alternatives(id), 
            FOREIGN KEY(element_property_id) REFERENCES element_properties_definition(id)
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
        """CREATE TABLE IF NOT EXISTS ontology_terms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ontology_name TEXT NOT NULL,
            term TEXT NOT NULL,
            FOREIGN KEY (ontology_name) REFERENCES ontologies (name) ON DELETE CASCADE,
            UNIQUE(ontology_name, term)
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS ontology_sorts (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            ontology_name TEXT NOT NULL,
            term TEXT NOT NULL, 
            sort TEXT NOT NULL, 
            FOREIGN KEY(ontology_name, term) REFERENCES ontology_terms(ontology_name, term) ON DELETE CASCADE,
            UNIQUE(ontology_name, term, sort)
        )"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS sorts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            FOREIGN KEY (name) REFERENCES ontologies (name) ON DELETE CASCADE
        )"""
    )

    conn.commit()
    conn.close()