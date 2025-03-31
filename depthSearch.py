##opens the Maze text file and reads the file
maze_file = open(r"c:\Users\pnama\Downloads\maze.txt", "r")
maze = maze_file.read()
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

    #funtion that checks wheather the Maze is solve or not
    def result(self):
        if "E" in self.state:
            return False
        else:
            return True
    
    #The funtion returns list to possible actions that can be used on maze
    def actions(self):
        possible_actions = []
        maze = self.state

        #the loop figires out current x,y coordiante in the maze and updates them in x_y
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if "S" == maze[i][j]:
                    x = j
                    y = i
                    break

        length_of_maze = len(maze[y])
        depth_of_maze = len(maze[y])
        #checks if We can move right
        if (x+1 < length_of_maze) and (maze[y][x+1] != "1"):
            possible_actions.append("right")
        #checks if can go left
        if(x+1 != 1) and maze[y][x-1] != "1":
            possible_actions.append("left")
        #checks if can go up
        if(y+1 != 1) and maze[y-1][x] != "1":
            possible_actions.append("up")
        #check if can go down
        if(y+1 < depth_of_maze) and maze[y+1][x] != "1":
            possible_actions.append("down")

        printmaze()
        return possible_actions
    
    def transition(self, action):
        possible_actions = ["right", "left", "up", "down"]
        maze_local = maze
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if "S" == maze[i][j]:
                    x = j
                    y = i
                    break
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

frontier = [initial_node]

