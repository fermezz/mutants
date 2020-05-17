import os


MONGODB_SETTINGS = {
    "db": os.environ["MONGODB_DATABASE"],
    "host": os.environ["MONGODB_HOSTNAME"],
    "password": os.environ["MONGODB_PASSWORD"],
    "username": os.environ["MONGODB_USERNAME"],
}
