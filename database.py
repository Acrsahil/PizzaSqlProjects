from sqlalchemy import create_engine
import pandas as pd
import os

conn_string = "mysql+mysqlconnector://root:dassahil123@localhost:3306/pizzastore"
db = create_engine(
    conn_string, connect_args={"charset": "utf8mb4", "collation": "utf8mb4_general_ci"}
)
conn = db.connect()


path = "/home/window/dataanalyst/sqlprojects/pizzaproject/dataset/"
for file in os.listdir(path):
    df = pd.read_csv(f"{path}{file}", encoding="ISO-8859-1")
    file = file.split(".")[0]
    df.to_sql(file, con=conn, if_exists="replace", index=False)
