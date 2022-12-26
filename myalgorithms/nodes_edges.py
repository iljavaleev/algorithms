import collections
import math
connection = collections.namedtuple('connection', ['destination', 'weight'])


class Vertex:
    names = set()

    def __init__(self, name):
        if name in self.names:
            raise ValueError(f'Vertex with name {name} is already exists')
        else:
            self.names.add(name)
        self.name = name
        self.out_adj_list = list()
        self.in_adj_list = list()
        self.component = None
        self.explored = False
        self.value = math.inf
        self.key = math.inf

    def add_connection(self, destination, weight=None):
        if weight and weight < 0:
            raise ValueError('weight must non negative')
        self.out_adj_list.append(connection(destination, weight))
        destination.in_adj_list.append(connection(self, weight))

    def get_key(self):
        if self.in_adj_list:
            min_connection = min(self.in_adj_list,
                       key=lambda x: x.destination.value + x.weight)
            return min_connection.weight + min_connection.destination.value
        return self.key

    def __str__(self):
        return (f'{self.name}, explored: {self.explored}, value: {self.value}, '
                f'component: {self.component}')

    def __repr__(self):
        return (f'{self.name}, explored: {self.explored}, value: {self.value}, '
                f'component: {self.component}, key: {self.key}')

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        return self.get_key() < other.get_key()

