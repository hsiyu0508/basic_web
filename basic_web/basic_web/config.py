import os
from dotenv import load_dotenv


class Config:
    load_dotenv()
    shop_db_user = os.getenv('SHOP_DB_USER')
    shop_db_pwd = os.getenv('SHOP_DB_PWD')
    shop_db_host = os.getenv('SHOP_DB_HOST')
    shop_db_port = os.getenv('SHOP_DB_PORT')
    shop_db_db = os.getenv('SHOP_DB_DB')