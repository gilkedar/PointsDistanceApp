API_VERSION = "1.0"

HTTP_SERVER_IP = "127.0.0.1"
HTTP_SERVER_PORT = 5000

API_NAME = "api"
RESOURCE_GET_RESPONSE = "getResponse"
RESOURCE_POST_ADDRESSES = "postAddresses"

URI_GET_RESPONSE = f"/{API_NAME}/{API_VERSION}/{RESOURCE_GET_RESPONSE}"
URI_POST_ADDRESSES = f"/{API_NAME}/{API_VERSION}/{RESOURCE_POST_ADDRESSES}"

MONGO_DB_ACCESS_USER = "test_user"
MONGO_DB_ACCESS_PASSWORD = "4WoLxYOa00WLOUCM"
MONGO_DB_NAME = "test"
MONGO_COLLECTION_NAME = "points_and_links"
MONGO_URL = f"mongodb+srv://{MONGO_DB_ACCESS_USER}:{MONGO_DB_ACCESS_PASSWORD}@cluster0.h6xhg.mongodb.net/{MONGO_DB_NAME}"