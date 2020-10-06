
class Link:

    def __init__(self, curr_point, other_point):
        self.name = other_point.name + curr_point.name
        self.distance = curr_point.get_distance(other_point)

    def toJSON(self):
        return self.__dict__
