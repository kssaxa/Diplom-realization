#!/usr/bin/env python3
"""
Проверка альтернатив в ontology.db
"""

import sqlite3

def check_alternatives():
    """Проверяет альтернативы в ontology.db"""
    print("=== ПРОВЕРКА АЛЬТЕРНАТИВ В ONTOLOGY.DB ===")
    
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, alternative_name, set_name FROM alternatives")
    alternatives = cursor.fetchall()
    
    print(f"\nНайдено альтернатив: {len(alternatives)}")
    for alt_id, alt_name, set_name in alternatives:
        print(f"  ID: {alt_id}, Название: {alt_name}, Множество: {set_name}")
    
    conn.close()

def check_screen_forms():
    """Проверяет экранные формы в data.db"""
    print("\n=== ПРОВЕРКА ЭКРАННЫХ ФОРМ В DATA.DB ===")
    
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, form_name, ontology_term FROM screen_forms")
    forms = cursor.fetchall()
    
    print(f"\nНайдено экранных форм: {len(forms)}")
    for form_id, form_name, ontology_term in forms:
        print(f"  ID: {form_id}, Название: {form_name}, Онтология: {ontology_term}")
    
    conn.close()

if __name__ == "__main__":
    check_alternatives()
    check_screen_forms() 