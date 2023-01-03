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
        self.TWITTER_BEARER_TOKEN = config.get('twitter_bearer_token')
        self.NICK_TWITTER_URL_BASE = "https://twitter.com/EvryMnRodriguez/status/"
        self.NICK_TWITTER_ID = config.get('nick_twitter_id')
        self.NICK_STACK_OVERFLOW_ID = config.get('nick_stack_overflow_id')
        self.NICK_STACK_OVERFLOW_URL = f"https://api.stackexchange.com/2.2/users/{self.NICK_STACK_OVERFLOW_ID}/questions?site=stackoverflow.com"
        self.NICK_GITHUB_USERNAME = "costa-rica"
        self.NICK_GITHUB_TOKEN = config.get("nick_github_token")
            

class ConfigLocal(ConfigBase):

    def __init__(self):
        super().__init__()
        
    DEBUG = True
    SA_API_URL = "http://localhost:5001"
    
            

class ConfigDev(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = True
    SA_API_URL = "http://198.172.1.6"
            

class ConfigProd(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = False
    SA_API_URL = "https://api.to_something.com"
