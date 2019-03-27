class Node():
    def __init__(self,value,point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0

    def move_cost(self,other):
        return 0 if self.value == '.' else 1

        
def children(point,grid):
    x,y = point.point
    print(len(grid))
    print(len(grid[0]))
    print ([(0 if (x-1) < 0 else x-1, y),(x,0 if (y - 1)< 0 else y-1),(x,y + 1),(x+1,y)])
    links = [grid[d[0]][d[1]] for d in [(0 if (x-1) < 0 else x-1, y),(x,0 if (y - 1)< 0 else y-1),(x,y + 1),(x+1,y)]]
    return [link for link in links if link.value != '%']

def manhattan(point,point2):
    return abs(point.point[0] - point2.point[0]) + abs(point.point[1]-point2.point[0])

def aStar(start, goal, grid):
    openset = []
    closedset = []

    #Ponto de partida   é o ponto inicial
    current = start

    #Adicionando o ponto inicial a lista aberta
    openset.append(current)

    #Enquanto houver elementos na lista aberta
    while openset:
        #Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o:o.G + o.H)
        #If it is the item we want, retrace the path and return it
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        #Remove the item from the open set
        openset.remove(current)
        #Add it to the closed set
        closedset.append(current)
        #Loop through the node's children/siblings
        for node in children(current,grid):
            #If it is already in the closed set, skip it
            if node in closedset:
                continue
            #Otherwise if it is already in the open set
            if node in openset:
                #Check if we beat the G score 
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                #Set the parent to our current item
                node.parent = current
                #Add it to the set
                openset.append(node)
    #Throw an exception if there is no path
    raise ValueError('No Path Found')
def next_move(pacman,food,grid):
    #Convert all the points to instances of Node
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] = Node(grid[x][y],(x,y))
    #Get the path
    print(len(grid))
    print(len(grid[0]))
    print(pacman)
    print(food)
    path = aStar(grid[pacman[0]][pacman[1]],grid[food[0]][food[1]],grid)
    #Output the path
    print (len(path) - 1)
    for node in path:
        x, y = node.point
        print (x, y)
pacman_x = int(input())
pacman_y = int(input())
food_x = int(input())
food_y = int(input())
x = int(input())
y = int(input())

 
grid = []
for i in range(0, x):
    grid.append(input().split())
 
next_move((pacman_x, pacman_y),(food_x, food_y), grid)
