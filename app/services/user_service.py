from app import mongo
from bson.objectid import ObjectId
from app.models.user import User  # Import the User class



class UserService:

    def get_all_users(self):
        users = mongo.db.users.find()
        if not users:
            return ["No User Is Register Yet"]
        return [User.from_json(user) for user in users]

    def get_user_by_id(self, user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return User.from_json(user) if user else "User Not Found"

    def create_user(self, data):
        mongo.db.users.insert_one(data)

    def update_user(self, user_id, data):
        result = mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})
        return result.modified_count > 0

    def delete_user(self, user_id):
        result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
