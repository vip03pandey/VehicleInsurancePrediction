import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException


class Proj1Data:
    def __init__(self) -> None:
        try:
            self.mongo_client=MongoDBClient(DATABASE_NAME)
        except Exception as e:
            raise MyException(e,sys)
            sys.exit(1)
    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection=self.mongo_client.database[collection_name]
            else:
                collection=self.mongo_client.client[database_name][collection_name]
            print("fetching data from collection")
            data=list(collection.find())
            df=pd.DataFrame(data)
            return df
        except Exception as e:
            raise MyException(e,sys)
            sys.exit(1)

