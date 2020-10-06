from flask import Flask, request, Response
from utils import config
from utils.logger import Logger
from utils.db_manager import DbManager
from utils.csv_parser import CsvBytesParser
from utils.point import Point
from utils.db_item import DbItem

app = Flask(__name__)

class HttpServer:

    def __init__(self):
        self._db_manager = DbManager()
        self._logger = Logger(self.__class__.__name__)

    def add_data_to_db(self, item):
        return self._db_manager.insert(item)

    def get_data_from_db(self, uuid):
        return self._db_manager.get(uuid)

    def handle_new_data(self, data):

        csv_parser = CsvBytesParser(data)

        points = []
        links = []
        for line in csv_parser.get_next_line():
            try:
                name, lat, lon = line
            except Exception as ex:
                self._logger.warning("invalid item in csv line, skipping...")
                continue
            new_point = Point(name, lat, lon)
            links.extend(new_point.create_links(points))
            points.append(new_point)

        db_item = DbItem(points,links)

        item = self.add_data_to_db(db_item)

        return item

    def get_item(self, request):
        pass

@app.route(config.URI_POST_ADDRESSES, methods=['POST'])
def get_addresses():
    """
    request containing csv file with points and their lat/lon
    :return: db uuuid for stored json response
    """


    r = request
    data = r.get_data()
    try:
        ans = http_main_server.handle_new_data(data)
    except Exception as ex:
        pass

    return Response(ans)

@app.route(config.URI_GET_RESPONSE, methods=['GET'])
def get_response():
    """
    request containing uuid returned by get_addresses uri
    :return: json containing db query results
    """
    r = request
    data = r.get_data_from_db()
    try:
        item = http_main_server.get_item(r)
    except Exception as ex:
        pass

    return Response(item)


if __name__ == '__main__':
        try:
            http_main_server = HttpServer()
            app.run(host=config.HTTP_SERVER_IP, port=config.HTTP_SERVER_PORT)
        except Exception as ex:
            http_main_server.logger.critical(ex)
        finally:
            http_main_server.closeResources()
