#!/usr/bin/env python3
"""
Проверка данных онтологии и экранных форм
"""

import sqlite3

def check_ontology_data():
    """Проверяет данные онтологии"""
    print("=== ПРОВЕРКА ДАННЫХ ОНТОЛОГИИ ===")
    
    # Проверяем data.db
    print("\n--- DATA.DB ---")
    conn_data = sqlite3.connect("data.db")
    cursor_data = conn_data.cursor()
    
    print("\n1. Онтологии:")
    cursor_data.execute("SELECT * FROM ontologies")
    ontologies = cursor_data.fetchall()
    for row in ontologies:
        print(f"   ID: {row[0]}, Название: {row[1]}")
    
    print("\n2. Термины онтологии:")
    cursor_data.execute("SELECT * FROM ontology_terms")
    terms = cursor_data.fetchall()
    for row in terms:
        print(f"   ID: {row[0]}, Онтология: {row[1]}, Термин: {row[2]}")
    
    print("\n3. Сорта онтологии:")
    cursor_data.execute("SELECT * FROM ontology_sorts")
    sorts = cursor_data.fetchall()
    for row in sorts:
        print(f"   ID: {row[0]}, Онтология: {row[1]}, Термин: {row[2]}, Сорт: {row[3]}")
    
    print("\n4. Экранные формы:")
    cursor_data.execute("SELECT * FROM screen_forms")
    forms = cursor_data.fetchall()
    for row in forms:
        print(f"   ID: {row[0]}, Название: {row[1]}, Онтология: {row[2]}")
    
    conn_data.close()
    
    # Проверяем ontology.db
    print("\n--- ONTOLOGY.DB ---")
    conn_ontology = sqlite3.connect("ontology.db")
    cursor_ontology = conn_ontology.cursor()
    
    print("\n5. Альтернативы:")
    cursor_ontology.execute("SELECT * FROM alternatives")
    alternatives = cursor_ontology.fetchall()
    for row in alternatives:
        print(f"   ID: {row[0]}, Название: {row[1]}, Множество: {row[2]}")
    
    conn_ontology.close()

if __name__ == "__main__":
    check_ontology_data() 