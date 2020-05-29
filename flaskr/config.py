import os

CELERY_BROKER_URL = f"redis://{os.environ['REDIS_URL']}:6379"
CELERY_RESULT_BACKEND = f"redis://{os.environ['REDIS_URL']}:6379"

MONGODB_SETTINGS = {
    "db": os.environ["MONGODB_DATABASE"],
    "host": os.environ["MONGODB_HOSTNAME"],
    "password": os.environ["MONGODB_PASSWORD"],
    "username": os.environ["MONGODB_USERNAME"],
    "connect": False,
}
