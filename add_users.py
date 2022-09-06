from data_manager import DataManager

data_manager = DataManager()
user = data_manager.create_user()
while not user:
    data_manager.create_user()
data_manager.add_user_to_database()
