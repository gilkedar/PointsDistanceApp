

class DbItem:

    def __init__(self, points, links):
        self.points = [point.toJSON() for point in points]
        self.links = [link.toJSON() for link in links]

    def toJSON(self):
        return self.__dict__

