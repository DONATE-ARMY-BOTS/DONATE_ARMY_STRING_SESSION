from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

import config


mongo = MongoCli(config.MONGO_DB_URI)
db = mongo.DONATE_ARMY_STRING
