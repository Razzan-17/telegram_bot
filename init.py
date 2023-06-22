import os

from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

TOKEN = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
name_db = os.getenv('NAME_DB')
host = os.getenv('HOST')


engine = create_engine(f'postgresql+psycopg2://{login}:{password}@{host}/{name_db}',
                       echo=True)
Session = sessionmaker(autoflush=False, bind=engine)
