"""
High-level modules should not depend on low-level modules. Both should depend on abstractions.
"""


from abc import ABC, abstractmethod

# Low-level module
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class MongoDBDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MongoDB database")

# High-level module depends on abstraction (Database) not implementation
class DataManager:
    def __init__(self, database: Database):
        self.database = database

    def store(self, data):
        self.database.save(data)

mysql_db = MySQLDatabase()
mongo_db = MongoDBDatabase()

data_manager = DataManager(mysql_db)
data_manager.store("User data")  # Outputs: Saving User data to MySQL database

data_manager = DataManager(mongo_db)
data_manager.store("User data")  # Outputs: Saving User data to MongoDB database
