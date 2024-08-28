# import sqlite3
# # 1
# class DatabaseManager:
#     def __init__(self, db_name):
#         self.db_name = db_name
#         self.connection = None
#         self.cursor = None
    
#     def open_connection(self):
#         """Открыть соединение с базой данных"""
#         self.connection = sqlite3.connect(self.db_name)
#         self.cursor = self.connection.cursor()
    
#     def close_connection(self):
#         """Закрыть соединение с базой данных"""
#         if self.connection:
#             self.connection.close()
#             self.connection = None
#             self.cursor = None
    
#     def execute_query(self, query, params=()):
#         """Выполнить SQL-запрос"""
#         if self.cursor:
#             self.cursor.execute(query, params)
#             self.connection.commit()
    
#     def fetch_query(self, query, params=()):
#         """Выполнить SQL-запрос и вернуть результаты"""
#         if self.cursor:
#             self.cursor.execute(query, params)
#             return self.cursor.fetchall()

#     def find_user_by_name(self, username):
#         """Найти пользователя по имени"""
#         query = "SELECT * FROM users WHERE user = ?"
#         return self.fetch_query(query, (username,))
#     # 2
#     class User(DatabaseManager):
#     def __init__(self, db_name):
#         super().__init__(db_name)
#         self.open_connection()
#         self.create_table()
#         self.close_connection()
    
#     def create_table(self):
#         """Создать таблицу users, если она не существует"""
#         query = """
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user TEXT UNIQUE NOT NULL,
#             age INTEGER,
#             role TEXT
#         )
#         """
#         self.execute_query(query)
    
#     def add_user(self, user, age, role):
#         """Добавить нового пользователя"""
#         query = "INSERT INTO users (user, age, role) VALUES (?, ?, ?)"
#         self.execute_query(query, (user, age, role))
    
#     def get_user_by_id(self, user_id):
#         """Получить пользователя по ID"""
#         query = "SELECT * FROM users WHERE id = ?"
#         return self.fetch_query(query, (user_id,))
    
#     def delete_user(self, user_id):
#         """Удалить пользователя по ID"""
#         query = "DELETE FROM users WHERE id = ?"
#         self.execute_query(query, (user_id,))
# # 3
# class Admin(User):
#     def __init__(self, db_name):
#         super().__init__(db_name)
#         self.create_admin_table()
    
#     def create_admin_table(self):
#         """Создать таблицу admins"""
#         query = """
#         CREATE TABLE IF NOT EXISTS admins (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user TEXT UNIQUE NOT NULL,
#             age INTEGER,
#             permissions TEXT
#         )
#         """
#         self.execute_query(query)
    
#     def add_admin(self, user, age, permissions):
#         """Добавить нового администратора"""
#         query = "INSERT INTO admins (user, age, permissions) VALUES (?, ?, ?)"
#         self.execute_query(query, (user, age, permissions))

# class Customer(User):
#     def __init__(self, db_name):
#         super().__init__(db_name)
#         self.create_customer_table()
    
#     def create_customer_table(self):
#         """Создать таблицу customers"""
#         query = """
#         CREATE TABLE IF NOT EXISTS customers (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user TEXT UNIQUE NOT NULL,
#             age INTEGER,
#             membership_level TEXT
#         )
#         """
#         self.execute_query(query)
    
#     def add_customer(self, user, age, membership_level):
#         """Добавить нового клиента"""
#         query = "INSERT INTO customers (user, age, membership_level) VALUES (?, ?, ?)"
#         self.execute_query(query, (user, age, membership_level))
# 4-5
# db = DatabaseManager('mydatabase.db')

# queries = [
#     ("INSERT INTO users (user, age, role) VALUES (?, ?, ?)", ('JohnDoe', 30, 'admin')),
#     ("INSERT INTO users (user, age, role) VALUES (?, ?, ?)", ('JaneDoe', 25, 'customer'))
# ]

# db.execute_transaction(queries)

