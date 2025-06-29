#!/usr/bin/env python3
"""
Детальный анализ текущих данных для генерации интерфейса
"""

import sqlite3

def analyze_current_interface_data():
    """Анализирует текущие данные интерфейса"""
    print("=== ДЕТАЛЬНЫЙ АНАЛИЗ ТЕКУЩИХ ДАННЫХ ===")
    
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    
    print("\n1. ТЕКУЩИЕ ИНТЕРФЕЙСНЫЕ ЭЛЕМЕНТЫ:")
    cursor.execute("SELECT id, name FROM interface_elements ORDER BY name")
    elements = cursor.fetchall()
    
    for elem_id, elem_name in elements:
        print(f"   - {elem_name} (ID: {elem_id})")
    
    print("\n2. ТЕКУЩИЕ СВОЙСТВА ЭЛЕМЕНТОВ:")
    cursor.execute("SELECT id, name FROM properties_of_elements ORDER BY name")
    properties = cursor.fetchall()
    
    for prop_id, prop_name in properties:
        print(f"   - {prop_name} (ID: {prop_id})")
    
    print("\n3. ТЕКУЩИЕ ОПРЕДЕЛЕНИЯ СВОЙСТВ:")
    cursor.execute("""
        SELECT epd.id, ie.name, poe.name, epd.property_value
        FROM element_properties_definition epd
        JOIN interface_elements ie ON epd.element_id = ie.id
        JOIN properties_of_elements poe ON epd.property_id = poe.id
        ORDER BY ie.name, poe.name
    """)
    definitions = cursor.fetchall()
    
    for def_id, elem_name, prop_name, prop_value in definitions:
        print(f"   - {elem_name}: {prop_name} = {prop_value}")
    
    print("\n4. АЛЬТЕРНАТИВЫ И ИХ ЭЛЕМЕНТЫ:")
    cursor.execute("SELECT id, alternative_name, set_name FROM alternatives ORDER BY alternative_name")
    alternatives = cursor.fetchall()
    
    for alt_id, alt_name, set_name in alternatives:
        print(f"\n   🔄 {alt_name} (Множество: {set_name})")
        
        cursor.execute("""
            SELECT ae.id, ie.name, poe.name, epd.property_value
            FROM alternative_elements ae
            JOIN alternatives a ON ae.alternative_id = a.id
            JOIN element_properties_definition epd ON ae.element_property_id = epd.id
            JOIN interface_elements ie ON epd.element_id = ie.id
            JOIN properties_of_elements poe ON epd.property_id = poe.id
            WHERE a.alternative_name = ?
            ORDER BY ie.name, poe.name
        """, (alt_name,))
        
        elements = cursor.fetchall()
        for elem_id, elem_name, prop_name, prop_value in elements:
            print(f"     - {elem_name}: {prop_name} = {prop_value}")
    
    conn.close()

def suggest_improved_data():
    """Предлагает улучшенные данные для генерации интерфейса"""
    print("\n=== ПРЕДЛОЖЕНИЯ ПО УЛУЧШЕНИЮ ДАННЫХ ===")
    
    print("\n🎯 ДЛЯ ГЕНЕРАЦИИ КРАСИВОГО ИНТЕРФЕЙСА НУЖНО ДОБАВИТЬ:")
    
    print("\n1. НОВЫЕ ИНТЕРФЕЙСНЫЕ ЭЛЕМЕНТЫ:")
    print("   - Заголовок (Header) - для названия интерфейса")
    print("   - Контейнер (Container) - для группировки элементов")
    print("   - Текст (Text) - для описаний и подписей")
    print("   - Разделитель (Divider) - для визуального разделения")
    print("   - Панель (Panel) - для группировки связанных элементов")
    
    print("\n2. НОВЫЕ СВОЙСТВА ЭЛЕМЕНТОВ:")
    print("   - Ширина (width) - в пикселях или процентах")
    print("   - Высота (height) - в пикселях")
    print("   - Отступы (padding) - внутренние отступы")
    print("   - Границы (border) - стиль границ")
    print("   - Шрифт (font) - размер и стиль шрифта")
    print("   - Выравнивание (align) - left, center, right")
    print("   - Тип (type) - для полей ввода (text, number, etc.)")
    print("   - Плейсхолдер (placeholder) - подсказка в полях")
    print("   - Текст (text) - отображаемый текст")
    print("   - Иконка (icon) - для кнопок")
    
    print("\n3. СПЕЦИАЛЬНЫЕ ЭЛЕМЕНТЫ ДЛЯ МНОЖЕСТВ:")
    print("   - Список элементов (ItemList) - для отображения списков")
    print("   - Кнопка добавления (AddButton) - специальная кнопка")
    print("   - Кнопка удаления (DeleteButton) - специальная кнопка")
    print("   - Поле поиска (SearchInput) - для фильтрации")
    print("   - Панель управления (ControlPanel) - для кнопок управления")
    print("   - Область результатов (ResultArea) - для отображения данных")
    
    print("\n4. ПРИМЕР УЛУЧШЕННОЙ СТРУКТУРЫ ДЛЯ 'МНОЖЕСТВА ИМЕН':")
    print("   Заголовок: 'Управление именами' (text='Управление именами', font='24px bold')")
    print("   Контейнер: 'Основная панель' (width='100%', padding='20px')")
    print("   Поле ввода: 'Поле имени' (type='text', placeholder='Введите имя...', width='300px')")
    print("   Кнопка: 'Добавить' (text='Добавить', type='add', color='green')")
    print("   Список: 'Список имен' (width='100%', height='300px')")
    print("   Текст: 'Подсказка' (text='Нажмите Enter для добавления', align='center')")

def create_sample_data_script():
    """Создает скрипт для добавления улучшенных данных"""
    print("\n=== СКРИПТ ДЛЯ ДОБАВЛЕНИЯ УЛУЧШЕННЫХ ДАННЫХ ===")
    
    script = '''
# Скрипт для добавления улучшенных данных
import sqlite3

def add_improved_data():
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    
    # 1. Добавляем новые интерфейсные элементы
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
        ("Область результатов",)
    ]
    
    for element in new_elements:
        cursor.execute("INSERT OR IGNORE INTO interface_elements (name) VALUES (?)", element)
    
    # 2. Добавляем новые свойства
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
        ("Иконка",)
    ]
    
    for property in new_properties:
        cursor.execute("INSERT OR IGNORE INTO properties_of_elements (name) VALUES (?)", property)
    
    # 3. Добавляем определения свойств для улучшенного интерфейса
    # Получаем ID элементов и свойств
    cursor.execute("SELECT id, name FROM interface_elements")
    elements = {name: id for id, name in cursor.fetchall()}
    
    cursor.execute("SELECT id, name FROM properties_of_elements")
    properties = {name: id for id, name in cursor.fetchall()}
    
    # Определения свойств для заголовка
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
    
    # Определения свойств для поля ввода
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
    
    # Определения свойств для кнопки добавления
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Кнопка добавления"], properties["Текст"], "Добавить"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Кнопка добавления"], properties["Цвет"], "0, 128, 0"))
    
    # Определения свойств для списка
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Список элементов"], properties["Ширина"], "100%"))
    
    cursor.execute("""
        INSERT OR IGNORE INTO element_properties_definition 
        (element_id, property_id, property_value) VALUES (?, ?, ?)
    """, (elements["Список элементов"], properties["Высота"], "300px"))
    
    conn.commit()
    conn.close()
    print("Улучшенные данные добавлены!")

if __name__ == "__main__":
    add_improved_data()
'''
    
    print(script)

if __name__ == "__main__":
    analyze_current_interface_data()
    suggest_improved_data()
    create_sample_data_script()
    print("\nАнализ завершен!") 