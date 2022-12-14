import os

secretKey = os.getenv("FLASK_SECRET_KEY")

mongoHost = os.getenv("MONGO_HOST")
mongoPort = int(os.getenv("MONGO_PORT"))
mongoDbManagement = os.getenv("MONGO_DB_MANAGEMENT")
mongoDbTransaction = os.getenv("MONGO_DB_TRANSACTION")
mongoDbMaster = os.getenv("MONGO_DB_MASTER")
mongoDbContent = os.getenv("MONGO_DB_CONTENT")