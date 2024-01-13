
import pymongo # pip install pymongo
import pandas as pd
import json


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Roma01:Roma2501@cluster0.xqlkm3n.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = (r"C:\Users\Alisha\Desktop\ML Projects\Shipment_Price\Data\train.csv")
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

#client = MongoClient(uri)

if __name__=="__main__":
    #Read data from the csv file into Pandas Dataframe
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)
    
    #Convert the DataFrame to a list of dictionaries (JSON records)
    #json_record = list(json.loads(df.T.to_json()).values())
    json_records = json.loads(df.to_json(orient="records"))
    print(json_records[0])

    #Establish a connection to MongoDB
    client = pymongo.MongoClient(uri)

    #Access the desired database and collection
    db = client[DATABASE]
    collection = db[COLLECTION_NAME]

    #Insert the json records into the collection
    collection.insert_many(json_records)

    #Close the MongoDB connection
    client.close()

    #client[DATABASE][COLLECTION_NAME].insert_many(json_record)