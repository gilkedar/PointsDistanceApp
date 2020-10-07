from flask import Flask, request, Response
from utils import config
from utils.logger import Logger
from utils.db_manager import DbManager
from utils.csv_parser import CsvBytesParser
from utils.point import Point
from utils.db_item import DbItem
import json
from bson import json_util


app = Flask(__name__)


class HttpServer:

    def __init__(self):
        self._db_manager = DbManager(DbItem)
        self.logger = Logger(self.__class__.__name__)

    def add_data_to_db(self, item):
        return self._db_manager.insert(item)

    def get_data_from_db(self, uuid):
        return self._db_manager.get(uuid)

    def handle_new_data_request(self, data):

        csv_parser = CsvBytesParser(data)

        points = []
        links = []
        for line in csv_parser.get_next_line():
            try:
                name, lat, lon = line
            except Exception as ex:
                self.logger.warning("invalid item in csv line, skipping...")
                continue
            new_point = Point(name, lat, lon)
            links.extend(new_point.create_links(points))
            points.append(new_point)

        db_item = DbItem(points,links)

        item = self.add_data_to_db(db_item)

        return item

    def handle_get_item_request(self, desired_id):
        return self.get_data_from_db(desired_id)


@app.route(config.URI_POST_ADDRESSES, methods=['POST'])
def get_addresses():
    """
    request containing csv file with points and their lat/lon
    :return: db uuuid for stored json response
    """
    r = request
    data = r.get_data()
    try:
        ans = http_main_server.handle_new_data_request(data)
    except Exception as ex:
        http_main_server.logger.error(ex)

    return Response(response=str(ans),
                    status=200,
                    mimetype="plain/text")


@app.route(config.URI_GET_RESPONSE, methods=['GET'])
def get_response():
    """
    request containing uuid returned by get_addresses uri
    :return: json containing db query results
    """
    r = request
    desired_id = r.data.decode("utf-8")
    item = {}
    try:
        item = http_main_server.handle_get_item_request(desired_id)
    except Exception as ex:
        http_main_server.logger.error(ex)

    return Response(response=json.dumps(item, default=json_util.default),
                    status=200,
                    mimetype="application/json")


if __name__ == '__main__':

    http_main_server = None
    try:
        http_main_server = HttpServer()
        app.run(host=config.HTTP_SERVER_IP, port=config.HTTP_SERVER_PORT)
    except Exception as ex:
        if http_main_server:
            http_main_server.logger.critical(ex)
        else:
            print(ex)