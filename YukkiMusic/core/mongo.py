from mongita import MongitaClientDisk

Создаем локальный клиент Mongita

client = MongitaClientDisk()

Используем базу данных "vevomusic"

db = client.vevomusic

Пример коллекций (можно расширить по необходимости)

chats_col = db.chats users_col = db.users sudos_col = db.sudos

Пример функций (используйте по назначению)

def get_chat(chat_id): return chats_col.find_one({"chat_id": chat_id})

def save_chat(chat_id, data): chats_col.update_one({"chat_id": chat_id}, {"$set": data}, upsert=True)

def get_user(user_id): return users_col.find_one({"user_id": user_id})

def save_user(user_id, data): users_col.update_one({"user_id": user_id}, {"$set": data}, upsert=True)

def get_sudoers(): return [doc["user_id"] for doc in sudos_col.find()]

def add_sudo(user_id): if not sudos_col.find_one({"user_id": user_id}): sudos_col.insert_one({"user_id": user_id})


