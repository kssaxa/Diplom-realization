#!/usr/bin/env python3
"""
Скрипт для добавления улучшенных данных интерфейса
"""

import sqlite3

def add_improved_interface_data():
    """Добавляет улучшенные данные для генерации интерфейса"""
    print("=== ДОБАВЛЕНИЕ УЛУЧШЕННЫХ ДАННЫХ ИНТЕРФЕЙСА ===")
    
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    
    # 1. Добавляем новые интерфейсные элементы
    print("\n1. Добавляем новые интерфейсные элементы...")
    new_elements = [
        ("Заголовок",),
        ("Контейнер",),
        ("Текст",),
        ("Разделитель",),
        ("Панель",),
        ("Список элементов",),
        ("Кнопка добавления",),
        ("Кнопка удаления",),
        ("Поле поиска",),
        ("Панель управления",),
        ("Область результатов",),
        ("Подсказка",)
    ]
    
    for element in new_elements:
        cursor.execute("INSERT OR IGNORE INTO interface_elements (name) VALUES (?)", element)
        print(f"   ✓ Добавлен элемент: {element[0]}")
    
    # 2. Добавляем новые свойства элементов
    print("\n2. Добавляем новые свойства элементов...")
    new_properties = [
        ("Ширина",),
        ("Высота",),
        ("Отступы",),
        ("Границы",),
        ("Шрифт",),
        ("Выравнивание",),
        ("Тип",),
        ("Плейсхолдер",),
        ("Текст",),
        ("Иконка",),
        ("Фон",),
        ("Стиль",)
    ]
    
    for property in new_properties:
        cursor.execute("INSERT OR IGNORE INTO properties_of_elements (name) VALUES (?)", property)
        print(f"   ✓ Добавлено свойство: {property[0]}")
    
    # 3. Получаем ID элементов и свойств
    cursor.execute("SELECT id, name FROM interface_elements")
    elements = {name: id for id, name in cursor.fetchall()}
    
    cursor.execute("SELECT id, name FROM properties_of_elements")
    properties = {name: id for id, name in cursor.fetchall()}
    
    print("\n3. Добавляем определения свойств...")
    
    # Определения свойств для заголовка
    print("   ✓ Настраиваем заголовок...")
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Заголовок"], properties["Текст"], "Управление именами"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Заголовок"], properties["Шрифт"], "24px bold"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Заголовок"], properties["Выравнивание"], "center"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Заголовок"], properties["Цвет"], "0, 0, 139"))
    
    # Определения свойств для контейнера
    print("   ✓ Настраиваем контейнер...")
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Контейнер"], properties["Ширина"], "100%"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Контейнер"], properties["Отступы"], "20px"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Контейнер"], properties["Границы"], "1px solid #ccc"))
    
    # Определения свойств для поля ввода
    print("   ✓ Настраиваем поле ввода...")
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Поле ввода"], properties["Тип"], "text"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Поле ввода"], properties["Плейсхолдер"], "Введите имя..."))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Поле ввода"], properties["Ширина"], "300px"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Поле ввода"], properties["Отступы"], "10px"))
    
    # Определения свойств для кнопки добавления
    print("   ✓ Настраиваем кнопку добавления...")
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Кнопка добавления"], properties["Текст"], "Добавить"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Кнопка добавления"], properties["Цвет"], "0, 128, 0"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Кнопка добавления"], properties["Отступы"], "10px"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Кнопка добавления"], properties["Шрифт"], "14px bold"))
    
    # Определения свойств для списка элементов
    print("   ✓ Настраиваем список элементов...")
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Список элементов"], properties["Ширина"], "100%"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Список элементов"], properties["Высота"], "300px"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Список элементов"], properties["Границы"], "1px solid #ddd"))
    
    # Определения свойств для подсказки
    print("   ✓ Настраиваем подсказку...")
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Подсказка"], properties["Текст"], "Нажмите Enter для добавления имени"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Подсказка"], properties["Выравнивание"], "center"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Подсказка"], properties["Цвет"], "128, 128, 128"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Подсказка"], properties["Шрифт"], "12px italic"))
    
    # 4. Создаем новую альтернативу с улучшенными элементами
    print("\n4. Создаем улучшенную альтернативу...")
    
    # Добавляем альтернативу для множества имен
    cursor.execute("""
        INSERT OR IGNORE INTO alternatives (alternative_name, set_name) 
        VALUES (?, ?)
    """, ("Улучшенное множество имен", "Множество имен"))
    
    # Получаем ID новой альтернативы
    cursor.execute("SELECT id FROM alternatives WHERE alternative_name = ?", 
                   ("Улучшенное множество имен",))
    alternative_id = cursor.fetchone()[0]
    
    # Получаем все определения свойств для новых элементов
    cursor.execute("""
        SELECT epd.id, ie.name, poe.name, epd.property_value
        FROM element_properties_definition epd
        JOIN interface_elements ie ON epd.element_id = ie.id
        JOIN properties_of_elements poe ON epd.property_id = poe.id
        WHERE ie.name IN ('Заголовок', 'Контейнер', 'Поле ввода', 'Кнопка добавления', 'Список элементов', 'Подсказка')
        ORDER BY ie.name, poe.name
    """)
    
    definitions = cursor.fetchall()
    
    # Добавляем элементы в альтернативу
    print("   ✓ Добавляем элементы в альтернативу...")
    for def_id, elem_name, prop_name, prop_value in definitions:
        cursor.execute("""
            INSERT OR IGNORE INTO alternative_elements 
            (alternative_id, element_property_id) VALUES (?, ?)
        """, (alternative_id, def_id))
        print(f"     - {elem_name}: {prop_name} = {prop_value}")
    
    # 5. Создаем альтернативу для множества отображений
    print("\n5. Создаем альтернативу для множества отображений...")
    
    cursor.execute("""
        INSERT OR IGNORE INTO alternatives (alternative_name, set_name) 
        VALUES (?, ?)
    """, ("Улучшенное множество отображений", "Множество отображений"))
    
    cursor.execute("SELECT id FROM alternatives WHERE alternative_name = ?", 
                   ("Улучшенное множество отображений",))
    alternative_id_2 = cursor.fetchone()[0]
    
    # Добавляем элементы для множества отображений
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Заголовок"], properties["Текст"], "Управление отображениями"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Поле ввода"], properties["Плейсхолдер"], "Введите отображение..."))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Подсказка"], properties["Текст"], "Нажмите Enter для добавления отображения"))
    
    # Получаем новые определения свойств
    cursor.execute("""
        SELECT epd.id, ie.name, poe.name, epd.property_value
        FROM element_properties_definition epd
        JOIN interface_elements ie ON epd.element_id = ie.id
        JOIN properties_of_elements poe ON epd.property_id = poe.id
        WHERE epd.property_value IN ('Управление отображениями', 'Введите отображение...', 'Нажмите Enter для добавления отображения')
        ORDER BY ie.name, poe.name
    """)
    
    new_definitions = cursor.fetchall()
    
    for def_id, elem_name, prop_name, prop_value in new_definitions:
        cursor.execute("""
            INSERT OR IGNORE INTO alternative_elements 
            (alternative_id, element_property_id) VALUES (?, ?)
        """, (alternative_id_2, def_id))
        print(f"     - {elem_name}: {prop_name} = {prop_value}")
    
    conn.commit()
    conn.close()
    print("\n✅ Улучшенные данные успешно добавлены!")
    print("\nТеперь у вас есть:")
    print("   - Новые интерфейсные элементы (Заголовок, Контейнер, Текст, etc.)")
    print("   - Новые свойства (Ширина, Высота, Отступы, Шрифт, etc.)")
    print("   - Улучшенные альтернативы для множеств имен и отображений")
    print("   - Готовые определения свойств для красивого интерфейса")

if __name__ == "__main__":
    add_improved_interface_data() 