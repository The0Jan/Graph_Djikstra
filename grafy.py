class Graph:
    def __init__(self, field = []):

        self. field = field
        self.route = [[-1, -1, -1, -1, -1, -1], 
                    [-1, -1, -1, -1, -1, -1], 
                    [-1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1], 
                    [-1, -1, -1, -1, -1, -1], 
                    [-1, -1, -1, -1, -1, -1]]

        self.shortest_track =  [[360, 360, 360, 360, 360, 360], 
                                [360, 360, 360, 360, 360, 360], 
                                [360, 360, 360, 360, 360, 360], 
                                [360, 360, 360, 360, 360, 360], 
                                [360, 360, 360, 360, 360, 360], 
                                [360, 360, 360, 360, 360, 360]]
        self.beginning = 0
        self.end = 0

    # function used for finding the end and beginning , so both 0's
    def find_end_begin(self):
        current = 0
        for column in self.field:
            for word in column:
                if word == 0:
                    if self.beginning != 0:
                        self.end  = current
                    else:
                        self.beginning = current
                        self.shortest_track[current//6][current%6] = 0

                current = current + 1
        
    # function used for testing the correctness of the algoritm
    def show(self):
        for column in self.field:
            print(column)
        print("field")
        
        for column in self.shortest_track:
            print(column)  
        print("shortesst_track")

        for column in self.route:
            print(column) 
        print("route")


    # function for going into every direction
    def start(self):
        self.dijkstra( self.beginning % 6, self.beginning // 6+1, self.beginning )
        self.dijkstra( self.beginning % 6, self.beginning // 6-1, self.beginning )
        self.dijkstra( self.beginning % 6+1, self.beginning // 6, self.beginning )
        self.dijkstra( self.beginning % 6-1, self.beginning // 6, self.beginning )


    # djikstra algorithm
    def dijkstra(self, x, y, previous_field):
        if x<6 and x >= 0 and y >= 0 and y < 6:
            value_now = self.shortest_track[previous_field // 6][ previous_field % 6 ] + self.field[y][x]
            if self.shortest_track[y][x] > value_now:
                self.shortest_track[y][x] = value_now
                self.route[y][x] = previous_field
                current_field = x + y*6
                self.dijkstra( x, y+1, current_field )
                self.dijkstra( x, y-1, current_field )
                self.dijkstra( x+1, y, current_field )
                self.dijkstra( x-1, y, current_field )

    # function to get graph from file
    def get_graph(self, name = ""):
        with open(name, "r") as file:
            lines = file.read().split("\n")
            test = []
            for line in lines:
                if line != '':
                    row = []
                    for char in line:
                        if char == ' ':
                            row.append(None)
                        else:
                            row.append(int(char))
                    test.append(row)
        self.field =  test
 
    # backtrack function, to go the shortest way from end to beginning
    def get_path(self):
        path = [[None for x in range(6)] for y in range(6)]
        current = self.end

        while True:
            current_x = current % 6
            current_y = current // 6
            path[current_y][current_x] = self.field[current_y][current_x]
            if self.route[current_y][current_x] == -1:
                return path
            current = self.route[current_y][current_x]

    # function for drawing the test 6x6 
    def draw_test(self):
        path = self.field
        for row in path:
            line = ""
            for price in row:
                line = line + str(price)
            print(line)

    # function for drawing the end results
    def draw_dijks(self):
        path = self.get_path()
        for row in path:
            line = ""
            for price in row:
                if price is not None:
                    line = line + str(price)
                else:
                    line = line + " "
            print(line)

    # function for showing the cordinates of the begin and end in the 6x6
    def show_end_begin(self):
        print(self.beginning %6, self.beginning//6)
        print(self.end %6, self.end //6)


#set of functions for taking the right graph, showing it and finding the shortest path
print("============")

graphy = Graph()
print("test1.txt")
graphy.get_graph("test1.txt")
graphy.draw_test()
graphy.find_end_begin()
graphy.start()
print("------------")
print("result_1")
graphy.draw_dijks()

print("============")

graphy = Graph()
print("test2.txt")
graphy.get_graph("test2.txt")
graphy.draw_test()
graphy.find_end_begin()
graphy.start()
print("------------")
print("result_2")
graphy.draw_dijks()

print("============")

graphy = Graph()
print("test3.txt")
graphy.get_graph("test3.txt")
graphy.draw_test()
graphy.find_end_begin()
graphy.start()
print("------------")
print("result_3")
graphy.draw_dijks()