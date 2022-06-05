class Graph:
    def set_data(self, data):
        self.data = data

    LIMIT_Y = [0, 10]

    def draw(self):
        numbers = []
        for num in self.data:
            if -1 < num < 11:
                numbers.append(num)
        return print(*numbers)


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
