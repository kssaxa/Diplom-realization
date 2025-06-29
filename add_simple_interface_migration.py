#!/usr/bin/env python3
"""
Миграция: добавление простых элементов и свойств для базового интерфейса
"""

import sqlite3

def add_simple_interface_elements():
    print("=== МИГРАЦИЯ: ДОБАВЛЕНИЕ ПРОСТОГО ИНТЕРФЕЙСА ===")
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()

    # 1. Добавляем недостающие элементы
    elements = [
        ("Заголовок",),
        ("Поле ввода",),
        ("Кнопка",),
        ("Список",),
        ("Подсказка",)
    ]
    for element in elements:
        cursor.execute("INSERT OR IGNORE INTO interface_elements (name) VALUES (?)", element)
        print(f"✓ Элемент: {element[0]}")

    # 2. Добавляем недостающие свойства
    properties = [
        ("Текст",),
        ("Шрифт",),
        ("Цвет",),
        ("Выравнивание",),
        ("Ширина",),
        ("Высота",),
        ("Отступы",),
        ("Тип",),
        ("Плейсхолдер",),
        ("Границы",),
        ("Фон",)
    ]
    for prop in properties:
        cursor.execute("INSERT OR IGNORE INTO properties_of_elements (name) VALUES (?)", prop)
        print(f"✓ Свойство: {prop[0]}")

    # 3. Получаем id элементов и свойств
    cursor.execute("SELECT id, name FROM interface_elements")
    element_ids = {name: eid for eid, name in cursor.fetchall()}
    cursor.execute("SELECT id, name FROM properties_of_elements")
    property_ids = {name: pid for pid, name in cursor.fetchall()}

    # 4. Добавляем определения свойств для простого интерфейса
    # Заголовок
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Заголовок"], property_ids["Текст"], "Заголовок интерфейса"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Заголовок"], property_ids["Шрифт"], "20px bold"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Заголовок"], property_ids["Цвет"], "0,0,0"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Заголовок"], property_ids["Выравнивание"], "center"))

    # Поле ввода
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Поле ввода"], property_ids["Тип"], "text"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Поле ввода"], property_ids["Плейсхолдер"], "Введите значение..."))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Поле ввода"], property_ids["Ширина"], "300px"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Поле ввода"], property_ids["Фон"], "#f5f5f5"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Поле ввода"], property_ids["Границы"], "1px solid #ccc"))

    # Кнопка
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Кнопка"], property_ids["Текст"], "Добавить"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Кнопка"], property_ids["Фон"], "#e0e0e0"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Кнопка"], property_ids["Цвет"], "0,0,0"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Кнопка"], property_ids["Ширина"], "120px"))

    # Список
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Список"], property_ids["Ширина"], "100%"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Список"], property_ids["Высота"], "200px"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Список"], property_ids["Фон"], "#fff"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Список"], property_ids["Границы"], "1px solid #ccc"))

    # Подсказка
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Подсказка"], property_ids["Текст"], "Введите значение и нажмите 'Добавить'"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Подсказка"], property_ids["Шрифт"], "12px italic"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Подсказка"], property_ids["Цвет"], "128,128,128"))
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition (element_id, property_id, property_value)
        VALUES (?, ?, ?)
    """, (element_ids["Подсказка"], property_ids["Выравнивание"], "center"))

    conn.commit()
    conn.close()
    print("\n✅ Миграция завершена! Простой интерфейс готов.")

if __name__ == "__main__":
    add_simple_interface_elements() 