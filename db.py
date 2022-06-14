import pymongo
import config

# mongodb link: mongodb+srv://gg:wp@cluster0.2qhvm.mongodb.net/?retryWrites=true&w=majority
db_client = pymongo.MongoClient(config.MONGODB_LINK, serverSelectionTimeoutMS=5000)

current_db = db_client["DenSaulyq"]

places_collection = current_db["places"]
appointments_collection = current_db["appointments"]

