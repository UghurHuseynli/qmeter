from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(host='mongodb://localhost:27017'
                # port=int(port),
                # username=username,
                # password=password
                )
    db_handle = client['db_name']
    return db_handle, client