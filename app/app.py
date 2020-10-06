from flask import Flask, request, Response
from utils import config
from utils.logger import Logger
app = Flask(__name__)

class HttpServer:

    def __init__(self):
        self._db_manager = DbManager()
        self.protocol = Protocol()
        self.logger = Logger()
    def add_data(self, item):
        self._db_manager.insert()

    def get_data(self, uuid):
        return self._db_manager.get(uuid)

    def handle_new_data(self, request):

        csv_parser = CsvParser()
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


@app.route(f"/api/{config.API_VERSION}/getAddresses")
def get_addresses():
    """
    request containing csv file with points and their lat/lon
    :return: db uuuid for stored json response
    """

    r = request
    try:
        ans = http_main_server.handle_new_data(r)
    except Exception as ex:
        pass

    return Response(ans)

@app.route(f"/api/{config.API_VERSION}/getResponse")
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
