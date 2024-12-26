from bson.objectid import ObjectId

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def from_json(data):
        return {
            "_id": str(data["_id"]),
            "name": data["name"],
            "email": data["email"],
            "password": data["password"]
        }
