from pymongo import MongoClient

def get_database(): 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
 
   # Create a connection using MongoClient.
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database
   return client['db']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   db = get_database()
   users = db['users']