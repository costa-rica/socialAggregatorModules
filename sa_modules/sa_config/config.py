import os
import json
from dotenv import load_dotenv

load_dotenv()


with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as config_file:
    config = json.load(config_file)

print('- in config.py -')
# print('PROJ_DB_PATH: ', os.environ.get('PROJ_DB_PATH'))

class ConfigBase:

    def __init__(self):
        self.CONFIG_TYPE = os.environ.get('CONFIG_TYPE')
        self.SECRET_KEY = config.get('SECRET_KEY')

        #Email stuff
        self.MAIL_SERVER = config.get('MAIL_SERVER_MSOFFICE')
        self.MAIL_PORT = config.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = config.get('EMAIL')
        self.MAIL_PASSWORD = config.get('EMAIL_PASSWORD')

        self.PROJ_ROOT_PATH = os.environ.get('PROJ_ROOT_PATH')
        self.PROJ_DB_PATH = os.environ.get('PROJ_DB_PATH')
        self.PROJ_LOGS_DIR = os.path.join(self.PROJ_ROOT_PATH, 'logs')
        self.SQL_URI =  f"sqlite:///{self.PROJ_DB_PATH}socialAggregator.db"
        self.TWITTER_BEARER_TOKEN = config.get('TWITTER_BEARER_TOKEN')
        self.TWITTER_URL_BASE = config.get('TWITTER_URL_BASE')
        self.TWITTER_ID = config.get('TWITTER_ID')
        self.STACK_OVERFLOW_ID = config.get('STACK_OVERFLOW_ID')
        self.STACK_OVERFLOW_URL = f"https://api.stackexchange.com/2.2/users/{self.STACK_OVERFLOW_ID}/questions?site=stackoverflow.com"
        self.GITHUB_USERNAME = config.get('GITHUB_USERNAME')
        self.GITHUB_TOKEN = config.get("GITHUB_TOKEN")
        self.GOODREADS_ID = config.get('GOODREADS_ID')
        self.GOODREADS_URL = config.get('GOODREADS_URL')
        self.SEND_DATA = os.environ.get('SEND_DATA')
        self.DESTINATION_PASSWORD = config.get('DESTINATION_PASSWORD')

class ConfigLocal(ConfigBase):

    def __init__(self):
        super().__init__()
        
    DEBUG = True
    API_URL = config.get('UPDATE_DESTINATION_URL_LOCAL')
    
            

class ConfigDev(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = True
    API_URL = config.get('UPDATE_DESTINATION_URL_DEV')
            

class ConfigProd(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = False
    API_URL = config.get('UPDATE_DESTINATION_URL')
    API_ENDPOINT_TESTER = "https://endpointtester.dashanddata.com/posts"
