import os
from dotenv import load_dotenv
from utils.BaseExecutor import BaseExecutor

class Config:
    def __init__(self, env_path: str = None):
        
        env_path = env_path or f"{os.getcwd()}\\envs\\.env"
        load_dotenv(dotenv_path=env_path)
        
        self.db_config = {
            "host": os.getenv("DB_HOST"),
            "database": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
        }
        self.base_executor = BaseExecutor(db_config=self.db_config)

    def get_base_executor(self):
        return self.base_executor

config = Config()
base_executor = config.get_base_executor()  