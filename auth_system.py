#!/usr/bin/env python3
"""
Система аутентификации и авторизации
"""

import sqlite3
import hashlib
import os
from datetime import datetime

class AuthSystem:
    def __init__(self):
        self.auth_db = "auth.db"
        self.current_user = None
        self.current_role = None
        self.init_auth_database()
    
    def init_auth_database(self):
        """Инициализирует базу данных аутентификации"""
        conn = sqlite3.connect(self.auth_db)
        cursor = conn.cursor()
        
        # Создаем таблицу пользователей
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Создаем таблицу сессий
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                session_token TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                expires_at TIMESTAMP NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        # Проверяем, есть ли уже пользователи
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        
        if user_count == 0:
            # Создаем администратора
            admin_password_hash = self.hash_password("admn")
            cursor.execute("""
                INSERT INTO users (username, password_hash, role)
                VALUES (?, ?, ?)
            """, ("admin", admin_password_hash, "admin"))
            
            # Создаем обычного пользователя
            user_password_hash = self.hash_password("user")
            cursor.execute("""
                INSERT INTO users (username, password_hash, role)
                VALUES (?, ?, ?)
            """, ("user", user_password_hash, "user"))
            
            print("✅ Созданы пользователи по умолчанию:")
            print("   👤 Администратор: admin / admn")
            print("   👤 Пользователь: user / user")
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password):
        """Хеширует пароль"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password, password_hash):
        """Проверяет пароль"""
        return self.hash_password(password) == password_hash
    
    def login(self, username, password):
        """Выполняет вход пользователя"""
        conn = sqlite3.connect(self.auth_db)
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT id, username, password_hash, role
                FROM users
                WHERE username = ?
            """, (username,))
            
            user = cursor.fetchone()
            
            if user and self.verify_password(password, user[2]):
                self.current_user = {
                    'id': user[0],
                    'username': user[1],
                    'role': user[3]
                }
                self.current_role = user[3]
                
                print(f"✅ Вход выполнен успешно!")
                print(f"   👤 Пользователь: {username}")
                print(f"   🔑 Роль: {user[3]}")
                
                return True
            else:
                print("❌ Неверное имя пользователя или пароль")
                return False
                
        except Exception as e:
            print(f"❌ Ошибка при входе: {e}")
            return False
        finally:
            conn.close()
    
    def logout(self):
        """Выполняет выход пользователя"""
        if self.current_user:
            print(f"👋 Выход выполнен для пользователя: {self.current_user['username']}")
        
        self.current_user = None
        self.current_role = None
    
    def is_authenticated(self):
        """Проверяет, аутентифицирован ли пользователь"""
        return self.current_user is not None
    
    def is_admin(self):
        """Проверяет, является ли пользователь администратором"""
        return self.current_role == "admin"
    
    def is_user(self):
        """Проверяет, является ли пользователь обычным пользователем"""
        return self.current_role == "user"
    
    def get_current_user(self):
        """Возвращает информацию о текущем пользователе"""
        return self.current_user
    
    def get_current_role(self):
        """Возвращает роль текущего пользователя"""
        return self.current_role
    
    def can_access_knowledge_editor(self):
        """Проверяет доступ к редактору знаний"""
        return self.is_admin()
    
    def can_edit_data(self):
        """Проверяет возможность редактирования данных"""
        return self.is_authenticated()  # И админ, и пользователь могут редактировать данные
    
    def can_view_data(self):
        """Проверяет возможность просмотра данных"""
        return self.is_authenticated()  # И админ, и пользователь могут просматривать данные
    
    def can_generate_interfaces(self):
        """Проверяет возможность генерации интерфейсов"""
        return self.is_authenticated()  # И админ, и пользователь могут генерировать интерфейсы

def main():
    """Тестовая функция"""
    auth = AuthSystem()
    
    print("🔐 Тестирование системы аутентификации")
    print("=" * 40)
    
    # Тест входа администратора
    print("\n1. Тест входа администратора:")
    success = auth.login("admin", "admn")
    if success:
        print(f"   Роль: {auth.get_current_role()}")
        print(f"   Может редактировать знания: {auth.can_access_knowledge_editor()}")
        print(f"   Может редактировать данные: {auth.can_edit_data()}")
    
    auth.logout()
    
    # Тест входа пользователя
    print("\n2. Тест входа пользователя:")
    success = auth.login("user", "user")
    if success:
        print(f"   Роль: {auth.get_current_role()}")
        print(f"   Может редактировать знания: {auth.can_access_knowledge_editor()}")
        print(f"   Может редактировать данные: {auth.can_edit_data()}")
    
    auth.logout()
    
    # Тест неверного пароля
    print("\n3. Тест неверного пароля:")
    auth.login("admin", "wrong_password")

if __name__ == "__main__":
    main() 