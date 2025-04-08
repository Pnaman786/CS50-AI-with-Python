from copy import deepcopy
##opens the Maze text file and reads the file
##prompts user for maze location on harddrive
file_location =  input(r"Enter the file location: ")
try:
    with open(file_location, "r") as maze_file:
        maze = maze_file.read()
except Exception as e:
    print(e)
maze = maze.replace(" ", "").split("\n")
for i in range(len(maze)):
    maze[i] = list(maze[i])
def printmaze():
    for i in range(len(maze)):
        print(maze[i])


## A Custom class that would store state of the maze and how it reached that place and possible actions that can be taken
class node:
    ##intilizing function
    def __init__(self,state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        def __lt__(self, other):
            return self.path_cost < other.path_cost

        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if "S" == self.state[i][j]:
                    self.x = j
                    self.y = i
                    break


    def printmaze(self):
        for i in range(len(self.state)):
            print(self.state[i])

    #funtion that checks wheather the Maze is solve or not
    def result(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == "E":
                    return False
        else:
            return True
    
    #The funtion returns list to possible actions that can be used on maze
    def actions(self):
        possible_actions = []
        maze = self.state

        x = self.x
        y = self.y

        length_of_maze = len(maze[y])
        depth_of_maze = len(maze)
        #checks if We can move right
        if (x+1 < length_of_maze) and (maze[y][x+1] not in ("1", "X")):
            possible_actions.append("right")
        #checks if can go left
        if(x > 0) and maze[y][x-1] not in ("1", "X"):
            possible_actions.append("left")
        #checks if can go up
        if(y > 0) and maze[y-1][x] not in ("1", "X"):
            possible_actions.append("up")
        #check if can go down
        if(y+1 < depth_of_maze) and maze[y+1][x] not in ("1", "X"):
            possible_actions.append("down")

        return possible_actions
    
    def transition(self, action):
        possible_actions = ["right", "left", "up", "down"]
        maze_local = deepcopy(self.state)
        
        x = self.x
        y = self.y
        
        if action not in possible_actions:
            print("invalid input")
        else:
            if action == "right":
                maze_local[y][x+1] = "S"

                maze_local[y][x] = "X"
            elif action == "left":
                maze_local[y][x-1] = "S"
                maze_local[y][x] = "X"
            elif action == "up":
                maze_local[y-1][x] = "S"
                maze_local[y][x] = "X"
            elif action == "down":
                maze_local[y+1][x] = "S"
                maze_local[y][x] = "X"
            return node(maze_local,self,action,self.path_cost+1)
            
        


        
        
#initilizing the maze by coverting starting point into a mzae
initial_node = node(maze,None,None,0)

def depth_search(initial_node):
    frontier = [initial_node]
    solutions = []
    while frontier:
        p_node = frontier.pop()
        if p_node.result() == True:
            solutions.append(p_node)
        else:
            p_actions = p_node.actions()
            for action in p_actions:
                frontier.append(p_node.transition(action))
    if len(frontier) == 0:
        return solutions
    
def least_path_cost(solutins):
    l_sol = len(solutins)
    for i in range(l_sol):
        if l_sol > 1:
            if solutins[i].path_cost < solutins[i+1].path_cost:
                solutins.pop(i+1)
                l_sol = l_sol-1
            else:
                solutins.pop(i)
                l_sol = l_sol-1
        else:
            return solutins.pop()

def breadth_first_search(initial_node):
    frontier = [initial_node]
    solutions = []
    while frontier:
        poped_node = frontier.pop(0)
        if poped_node.result() == True:
            solutions.append(poped_node)
        else:
            possible_actions = poped_node.actions()
            for action in possible_actions:
                frontier.append(poped_node.transition(action))
    if len(frontier) == 0:
        return solutions

def main():
    while True:
        choice = input("Enter \"0\" for Depth first Search And \"1\" For Breadth First Search: ")
        if choice.isdigit() == True:
            choice = int(choice)
            if choice != 0 and choice != 1 and choice != 2:
                continue
            else:
                break
        else:
            continue
    
    if choice == 0:
        depth_search(initial_node)[0].printmaze()
    if choice == 1:
        breadth_first_search(initial_node)[0].printmaze()
    if choice == 2:
        least_path_cost(breadth_first_search(initial_node)).printmaze()

main()