class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj_list = list()
        self.component = None
        self.explored = False
        self.value = None

    def add_connection(self, destination):
        self.adj_list.append(destination)

    def __str__(self):
        return (f'{self.name}, explored: {self.explored}, value: {self.value}, '
                f'component: {self.component}')

    def __repr__(self):
        return (f'{self.name}, explored: {self.explored}, value: {self.value}, '
                f'component: {self.component}')

