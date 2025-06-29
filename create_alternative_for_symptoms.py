#!/usr/bin/env python3
"""
Создание альтернативы для экранной формы "Интерфейс для симптомов"
"""

import sqlite3

def create_alternative_for_symptoms():
    """Создает альтернативу для экранной формы симптомов"""
    print("=== СОЗДАНИЕ АЛЬТЕРНАТИВЫ ДЛЯ СИМПТОМОВ ===")
    
    conn = sqlite3.connect("ontology.db")
    cursor = conn.cursor()
    
    # Добавляем альтернативу для интерфейса симптомов
    print("1. Добавляем альтернативу...")
    cursor.execute("""
        INSERT OR IGNORE INTO alternatives (alternative_name, set_name) 
        VALUES (?, ?)
    """, ("Альтернатива для симптомов", "Интерфейс для симптомов"))
    
    # Получаем ID новой альтернативы
    cursor.execute("SELECT id FROM alternatives WHERE alternative_name = ?", 
                   ("Альтернатива для симптомов",))
    alternative_id = cursor.fetchone()[0]
    
    print(f"   ✓ Альтернатива создана с ID: {alternative_id}")
    
    # Получаем существующие определения свойств для базовых элементов
    cursor.execute("""
        SELECT epd.id, ie.name, poe.name, epd.property_value
        FROM element_properties_definition epd
        JOIN interface_elements ie ON epd.element_id = ie.id
        JOIN properties_of_elements poe ON epd.property_id = poe.id
        WHERE ie.name IN ('Поле ввода', 'Кнопка ввода', 'Список записей')
        ORDER BY ie.name, poe.name
    """)
    
    definitions = cursor.fetchall()
    
    # Добавляем элементы в альтернативу
    print("2. Добавляем элементы в альтернативу...")
    for def_id, elem_name, prop_name, prop_value in definitions:
        cursor.execute("""
            INSERT OR IGNORE INTO alternative_elements 
            (alternative_id, element_property_id) VALUES (?, ?)
        """, (alternative_id, def_id))
        print(f"   ✓ {elem_name}: {prop_name} = {prop_value}")
    
    conn.commit()
    conn.close()
    print("\n✅ Альтернатива для симптомов успешно создана!")

if __name__ == "__main__":
    create_alternative_for_symptoms() 