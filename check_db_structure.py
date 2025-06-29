#!/usr/bin/env python3
"""
Проверка структуры базы данных ontology.db
"""

import sqlite3

def check_ontology_db():
    """Проверяет структуру ontology.db"""
    print("=== ПРОВЕРКА СТРУКТУРЫ ONTOLOGY.DB ===")
    
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    
    # Получаем список всех таблиц
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    print(f"\nНайдено таблиц: {len(tables)}")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Проверяем каждую таблицу
    for table in tables:
        table_name = table[0]
        print(f"\n--- ТАБЛИЦА: {table_name} ---")
        
        # Получаем структуру таблицы
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        
        print("Структура:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        
        # Получаем количество записей
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"Записей: {count}")
        
        # Показываем несколько примеров записей
        if count > 0:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
            rows = cursor.fetchall()
            print("Примеры записей:")
            for row in rows:
                print(f"  {row}")
    
    conn.close()

def check_data_db():
    """Проверяет структуру data.db"""
    print("\n=== ПРОВЕРКА СТРУКТУРЫ DATA.DB ===")
    
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    
    # Получаем список всех таблиц
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    print(f"\nНайдено таблиц: {len(tables)}")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Проверяем каждую таблицу
    for table in tables:
        table_name = table[0]
        print(f"\n--- ТАБЛИЦА: {table_name} ---")
        
        # Получаем структуру таблицы
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        
        print("Структура:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        
        # Получаем количество записей
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"Записей: {count}")
        
        # Показываем несколько примеров записей
        if count > 0:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
            rows = cursor.fetchall()
            print("Примеры записей:")
            for row in rows:
                print(f"  {row}")
    
    conn.close()

if __name__ == "__main__":
    check_ontology_db()
    check_data_db() 