#!/usr/bin/env python3
"""
Тестирование генерации HTML для интерфейса лекарств
"""

from html_generator import HTMLInterfaceGenerator

def test_medicines_interface():
    """Тестирует генерацию HTML для интерфейса лекарств"""
    print("=== ТЕСТИРОВАНИЕ ИНТЕРФЕЙСА ЛЕКАРСТВ ===")
    
    generator = HTMLInterfaceGenerator()
    
    # Генерируем HTML для интерфейса лекарств (ID: 3)
    html, error = generator.generate_html(3)
    
    if error:
        print(f"Ошибка: {error}")
        return
    
    # Сохраняем файл
    filename = generator.save_html_file(html, 3)
    print(f"✅ HTML интерфейс для лекарств сохранен в: {filename}")
    
    # Показываем первые 500 символов HTML для проверки
    print("\n--- ПРЕВЬЮ HTML ---")
    print(html[:500] + "...")

if __name__ == "__main__":
    test_medicines_interface() 