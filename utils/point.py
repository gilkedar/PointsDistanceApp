from utils.link import Link
from geopy import distance


class Point:

    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def get_coords(self):
        return self.lat, self.lon

    def get_distance(self, other):
        return distance.distance(self.get_coords(), other.get_coords()).meters

    def create_link(self, other):
        return Link(self, other)

    def create_links(self, others):
        links = []
        for other in others:
            links.append(self.create_link(other))
        return links

    def toJSON(self):
        return self.__dict__

    def __str__(self):
        return f"{self.name} - {self.lat} / {self.lon}"
