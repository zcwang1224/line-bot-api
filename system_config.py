from dotenv import dotenv_values
import os
import sys
class SystemConfig:
    
    def __init__(self, env_file_path: str):
        self.config = dotenv_values(env_file_path)
        self.__app_name = self.config.get("APP_NAME")
        self.__app_port = int(self.config.get("APP_PORT"))
        self.__mongodb_uri = self.config.get("MONGODB_URI")
        self.__db_main_uri = self.config.get("DB_MAIN_URI")
        self.__db_main_name = self.config.get("DB_MAIN_NAME")
        self.__db_main_debug = bool(self.config.get("DB_MAIN_DEBUG"))
        self.__redis_url = self.config.get("REDIS_URL")
        self.__ngrok_auth_token = self.config.get("NGROK_AUTH_TOKEN")
        self.__line_access_token = self.config.get("LINE_ACCESS_TOKEN")
        self.__line_secret = self.config.get("LINE_SECRET")
        
    @property
    def app_name(self):
        return self.__app_name    
    
    @property
    def app_port(self):
        return self.__app_port
    
    @property
    def mongodb_uri(self):
        return self.__mongodb_uri       
    
    @property
    def db_main_uri(self):
        return self.__db_main_uri   
    
    @property
    def db_main_name(self):
        return self.__db_main_name   
    
    @property
    def db_main_debug(self):
        return self.__db_main_debug   
    
    @property
    def redis_url(self):
        return self.__redis_url   
    
    @property
    def ngrok_auth_token(self):
        return self.__ngrok_auth_token  
    
    @property
    def line_access_token(self):
        return self.__line_access_token  
    
    @property
    def line_secret(self):
        return self.__line_secret                            

env_file_path = f"{os.path.dirname(__file__)}/.env"
system_config = SystemConfig(env_file_path)


if __name__ == "__main__":
    config = SystemConfig(env_file_path)
    print(f"App Name: {config.app_name}")
    print(f"App Port: {config.app_port}")
