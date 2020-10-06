from flask import Flask, request, Response
from utils import config
from utils.logger import Logger
from utils.db_manager import DbManager
from utils.csv_parser import CsvBytesParser
from utils.links_generator import LinksGenerator
from utils.point import Point
import io
import csv
app = Flask(__name__)

class HttpServer:

    def __init__(self):
        self._db_manager = DbManager()
        # self._logger = Logger(self.__class__.__name__)

    def add_data(self, item):
        self._db_manager.insert()

    def get_data(self, uuid):
        return self._db_manager.get(uuid)

    def handle_new_data(self, request):

        csv_parser = CsvBytesParser()
        links_generator = LinksGenerator()

        points = []
        links = []
        for line in self.csv_parser.read_next_line():
            new_point = Point(line)
            links.append(links_generator.get_new_links(new_point, points))
            points.append(new_point)

        item = self.add_data(points, links)

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

    try:
        file = r.data
        file = io.StringIO(file.decode())
        for line in file:
            print(line.strip('\r\n'))
        ans = http_main_server.handle_new_data(r)

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
