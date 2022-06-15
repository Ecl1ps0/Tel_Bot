import pymongo
import config

# mongodb link: mongodb+srv://gg:wp@cluster0.2qhvm.mongodb.net/?retryWrites=true&w=majority
db_client = pymongo.MongoClient(config.MONGODB_LINK, serverSelectionTimeoutMS=5000)

current_db = db_client["DenSaulyq"]

places_collection = current_db["places"]
appointments_collection = current_db["appointments"]


def get_all_hospitals():
    return places_collection.find()


def get_user_by_name(name):
    if (appointments_collection.find({"name": name}) != ""):
        return True
    else:
        return False


def get_all_appointments_of_user(name):
    return appointments_collection.find({"name": name})
