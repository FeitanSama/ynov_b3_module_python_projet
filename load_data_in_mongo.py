from pymongo import MongoClient
import pandas as pd
import os

client = MongoClient('localhost',27017)
db = client.crunchyroll

df = pd.read_csv(os.getcwd()+'/export_list.csv')

db.anime.drop()

db.anime.insert_many(df.to_dict('records'))