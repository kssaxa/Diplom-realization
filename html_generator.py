#!/usr/bin/env python3
"""
Генератор HTML интерфейсов на основе элементов альтернатив
"""

import sqlite3
import os
from datetime import datetime

class HTMLInterfaceGenerator:
    def __init__(self):
        self.ontology_db = "ontology.db"
        self.data_db = "data.db"
    
    def get_screen_form_data(self, screen_form_id):
        """Получает данные экранной формы и связанной альтернативы"""
        # Получаем данные экранной формы из data.db
        conn_data = sqlite3.connect(self.data_db)
        cursor_data = conn_data.cursor()
        
        cursor_data.execute("""
            SELECT sf.id, sf.form_name, sf.ontology_term
            FROM screen_forms sf
            WHERE sf.id = ?
        """, (screen_form_id,))
        
        screen_form = cursor_data.fetchone()
        conn_data.close()
        
        if not screen_form:
            return None
        
        screen_form_id, screen_form_name, ontology_term = screen_form
        
        # Получаем альтернативу для этой экранной формы из ontology.db
        conn_ontology = sqlite3.connect(self.ontology_db)
        cursor_ontology = conn_ontology.cursor()
        
        cursor_ontology.execute("""
            SELECT a.id, a.alternative_name, a.set_name
            FROM alternatives a
            WHERE a.set_name = ?
        """, (screen_form_name,))
        
        alternative = cursor_ontology.fetchone()
        if not alternative:
            conn_ontology.close()
            return None
        
        alt_id, alt_name, set_name = alternative
        
        # Получаем элементы альтернативы с их свойствами из ontology.db
        cursor_ontology.execute("""
            SELECT 
                ie.name as element_name,
                poe.name as property_name,
                epd.property_value,
                epd.id as property_id
            FROM alternative_elements ae
            JOIN element_properties_definition epd ON ae.element_property_id = epd.id
            JOIN interface_elements ie ON epd.element_id = ie.id
            JOIN properties_of_elements poe ON epd.property_id = poe.id
            WHERE ae.alternative_id = ?
            ORDER BY ie.name, poe.name
        """, (alt_id,))
        
        elements = cursor_ontology.fetchall()
        conn_ontology.close()
        
        return {
            'screen_form_id': screen_form_id,
            'screen_form_name': screen_form_name,
            'sort_name': ontology_term,
            'alternative_id': alt_id,
            'alternative_name': alt_name,
            'set_name': set_name,
            'elements': elements
        }
    
    def generate_css_from_elements(self, elements_by_type):
        """Генерирует CSS на основе свойств элементов"""
        css = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        """
        
        # Генерируем стили для контейнера
        if 'Контейнер' in elements_by_type:
            container = elements_by_type['Контейнер']
            css += """
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        """
        
        # Генерируем стили для заголовка
        if 'Заголовок' in elements_by_type:
            header = elements_by_type['Заголовок']
            css += """
        h1 {
            color: #FF007F;
            text-align: center;
            margin-bottom: 30px;
        }
        """
        
        # Генерируем стили для поля ввода
        if 'Поле ввода' in elements_by_type:
            input_elem = elements_by_type['Поле ввода']
            css += """
        .input-section {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            align-items: center;
        }
        
        input[type="text"] {
            flex: 1;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        """
        
        # Генерируем стили для кнопки
        if 'Кнопка' in elements_by_type:
            button = elements_by_type['Кнопка']
            css += """
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        
        .add-btn {
            background-color: #4CAF50;
            color: white;
        }
        
        .add-btn:hover {
            background-color: #45a049;
        }
        
        .delete-btn {
            background-color: #f44336;
            color: white;
        }
        
        .delete-btn:hover {
            background-color: #da190b;
        }
        """
        
        # Генерируем стили для списка
        if 'Список' in elements_by_type:
            list_elem = elements_by_type['Список']
            css += """
        .names-list {
            border: 2px solid #ddd;
            border-radius: 5px;
            min-height: 200px;
            padding: 10px;
            background-color: #fafafa;
        }
        
        .name-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px;
            margin: 5px 0;
            background-color: white;
            border-radius: 5px;
            border: 1px solid #eee;
        }
        
        .name-item:hover {
            background-color: #f0f0f0;
        }
        """
        
        # Генерируем стили для сообщения
        if 'Сообщение' in elements_by_type:
            message = elements_by_type['Сообщение']
            css += """
        .empty-message {
            text-align: center;
            color: #666;
            font-style: italic;
            margin-top: 50px;
        }
        """
        
        return css
    
    def generate_html_element(self, element_name, properties, interface_title=None):
        """Генерирует HTML для конкретного элемента"""
        if element_name == 'Заголовок':
            # Используем название термина онтологии, если оно передано
            if interface_title:
                text = interface_title
            else:
                text = properties.get('текст', 'Управление данными')
            return f'<h1>{text}</h1>'
        
        elif element_name == 'Контейнер':
            return '<div class="container">'
        
        elif element_name == 'Поле ввода':
            placeholder = properties.get('место заполнитель', 'Введите имя...')
            return f'''
                <div class="input-section">
                    <input type="text" id="nameInput" placeholder="{placeholder}">
            '''
        
        elif element_name == 'Кнопка':
            button_type = properties.get('тип кнопки', 'add')
            if button_type == 'add':
                return '<button class="add-btn" onclick="addName()">Добавить</button>'
            else:
                return '<button class="delete-btn" onclick="deleteName()">Удалить</button>'
        
        elif element_name == 'Список':
            return '''
                <div class="names-list" id="namesList">
                    <div class="empty-message">Список пуст. Добавьте имена.</div>
                </div>
            '''
        
        elif element_name == 'Сообщение':
            text = properties.get('текст', 'Список пуст. Добавьте имена.')
            return f'<div class="empty-message">{text}</div>'
        
        elif element_name == 'Форма':
            return '<div class="input-section">'
        
        elif element_name == 'Группа кнопок':
            return '<div class="button-group">'
        
        elif element_name == 'Разделитель':
            return '<hr>'
        
        elif element_name == 'Элемент списка':
            return '''
                <div class="name-item">
                    <span></span>
                    <button class="delete-btn" onclick="deleteName(index)">Удалить</button>
                </div>
            '''
        
        return f'<!-- Неизвестный элемент: {element_name} -->'
    
    def generate_html(self, screen_form_id):
        """Генерирует HTML интерфейс для экранной формы"""
        data = self.get_screen_form_data(screen_form_id)
        if not data:
            return None, "Не удалось получить данные экранной формы"
        
        # Используем название сорта как название интерфейса
        interface_title = data['sort_name']
        
        # Группируем элементы по типам
        elements_by_type = {}
        for element_name, property_name, property_value, property_id in data['elements']:
            if element_name not in elements_by_type:
                elements_by_type[element_name] = {}
            elements_by_type[element_name][property_name] = property_value
        
        # Генерируем CSS
        css = self.generate_css_from_elements(elements_by_type)
        
        # Генерируем HTML
        html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{interface_title}</title>
    <style>
{css}
    </style>
</head>
<body>
"""
        
        # Добавляем элементы в правильном порядке
        html_elements = []
        
        # Начинаем с контейнера
        if 'Контейнер' in elements_by_type:
            html_elements.append(self.generate_html_element('Контейнер', elements_by_type['Контейнер'], interface_title))
        
        # Добавляем заголовок
        if 'Заголовок' in elements_by_type:
            html_elements.append(self.generate_html_element('Заголовок', elements_by_type['Заголовок'], interface_title))
        
        # Добавляем форму с полем ввода и кнопкой
        if 'Форма' in elements_by_type:
            html_elements.append(self.generate_html_element('Форма', elements_by_type['Форма'], interface_title))
        
        if 'Поле ввода' in elements_by_type:
            html_elements.append(self.generate_html_element('Поле ввода', elements_by_type['Поле ввода'], interface_title))
        
        if 'Кнопка' in elements_by_type:
            html_elements.append(self.generate_html_element('Кнопка', elements_by_type['Кнопка'], interface_title))
        
        # Закрываем форму
        if 'Форма' in elements_by_type:
            html_elements.append('</div>')
        
        # Добавляем список
        if 'Список' in elements_by_type:
            html_elements.append(self.generate_html_element('Список', elements_by_type['Список'], interface_title))
        
        # Закрываем контейнер
        if 'Контейнер' in elements_by_type:
            html_elements.append('</div>')
        
        # Добавляем JavaScript
        html += ''.join(html_elements)
        
        html += """
    <script>
        let names = [];
        
        function addName() {
            const input = document.getElementById('nameInput');
            const name = input.value.trim();
            
            if (name && !names.includes(name)) {
                names.push(name);
                input.value = '';
                updateNamesList();
            } else if (names.includes(name)) {
                alert('Такое имя уже существует!');
            }
        }
        
        function deleteName(index) {
            names.splice(index, 1);
            updateNamesList();
        }
        
        function updateNamesList() {
            const list = document.getElementById('namesList');
            
            if (names.length === 0) {
                list.innerHTML = '<div class="empty-message">Список пуст. Добавьте имена.</div>';
                return;
            }
            
            list.innerHTML = names.map((name, index) => `
                <div class="name-item">
                    <span>${name}</span>
                    <button class="delete-btn" onclick="deleteName(${index})">Удалить</button>
                </div>
            `).join('');
        }
        
        // Обработка Enter в поле ввода
        document.getElementById('nameInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                addName();
            }
        });
    </script>
</body>
</html>"""
        
        return html, None
    
    def save_html_file(self, html_content, screen_form_id):
        """Сохраняет HTML в файл"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_interfaces/interface_{screen_form_id}_{timestamp}.html"
        
        # Создаем папку если её нет
        os.makedirs("generated_interfaces", exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filename

def main():
    """Тестовая функция"""
    generator = HTMLInterfaceGenerator()
    
    # Получаем список экранных форм
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, form_name FROM screen_forms")
    screen_forms = cursor.fetchall()
    conn.close()
    
    print("Доступные экранные формы:")
    for form_id, form_name in screen_forms:
        print(f"  {form_id}: {form_name}")
    
    if screen_forms:
        # Генерируем HTML для первой формы
        form_id = screen_forms[0][0]
        html, error = generator.generate_html(form_id)
        
        if html:
            filename = generator.save_html_file(html, form_id)
            print(f"\nHTML интерфейс сохранен в: {filename}")
        else:
            print(f"Ошибка: {error}")

if __name__ == "__main__":
    main() 