class Graph:
    def set_data(self, data):
        self.data = data

    LIMIT_Y = [0, 10]

    def draw(self):
        return print(*self.data)


graph1 = Graph()
graph1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph1.draw()
