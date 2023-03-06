import os

APP_NAME = os.getenv('APP_NAME', 'hr-prediction')

APP_WORKERS = int(os.getenv('APP_WORKER',1))

SWAGGER_ENDPOINT = os.getenv('SWAGGER_ENDPOINT', '/models')
