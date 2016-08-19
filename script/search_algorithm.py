import sys

def get_current_robot_position(world):
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == "+":
                return j,i

def get_exit_position(world):
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == "E":
                return j,i                

def get_next_step_to_take(world, available_directions, places_already_visited):
    # direction to be taken after analisys
    direction_to_be_taken = None

    # get current robot position
    x, y = get_current_robot_position(world)

    # from the current position, check what directions can be taken   
    lowest_heuristic_value = sys.maxint 
    for possible_direction in available_directions:
        # store the next robot position in order to verify if it's feasible or not
        next_x_position = x
        next_y_position = y

        # verify to where the robot can be send after going to a given direction
        if   possible_direction == "R": next_x_position = next_x_position + 1
        elif possible_direction == "L": next_x_position = next_x_position - 1
        elif possible_direction == "U": next_y_position = next_y_position - 1
        elif possible_direction == "D": next_y_position = next_y_position + 1

        # verify if the position is feasible (not out of the bounds of the world, it is not a wall neither already visited)
        if (next_y_position < len(world) and next_y_position >= 0) and (next_x_position < len(world[next_y_position]) and next_x_position >= 0): 
            if (world[next_y_position][next_x_position] != "#"): 
                # verify if the next place was already visited
                is_place_already_visited = False
                for place_already_visited in places_already_visited:
                    if (place_already_visited[0] == next_x_position and place_already_visited[0] == next_x_position): is_place_already_visited = True 
                
                if is_place_already_visited == False:
                    # first step is to determine where is the exit
                    exit_x_position, exit_y_position = get_exit_position(world)

                    # calculate heuristic
                    heuristic_value = abs( next_x_position - exit_x_position ) + abs(next_y_position - exit_y_position)

                    # add it as a possible_direction if this is the lowest heuristic value available
                    if ( heuristic_value < lowest_heuristic_value ):
                        lowest_heuristic_value = heuristic_value
                        direction_to_be_taken = possible_direction                    
        
    return direction_to_be_taken

def move_robot(world, direction_to_take, places_already_visited):
    # get current robot position
    x, y = get_current_robot_position(world)

    # store current position in the list of places already visited
    places_already_visited.append((x,y))

    # substitute place where the robot was by the direction taken in the world representation
    world[y][x] = direction_to_take   

    # get the next position by applying the direction to take
    if   direction_to_take == "R": x = x + 1
    elif direction_to_take == "L": x = x - 1
    elif direction_to_take == "U": y = y - 1
    elif direction_to_take == "D": y = y + 1
 
    # update world with the new robot position
    world[y][x] = "+"

def print_world(world):
    for i in range(len(world)):
        print
        for j in range(len(world[i])):
            print world[i][j], 

def create_world():
    # define the world where robo is placed
    world = [["." for x in range(7)] for y in range(3)]

    # defining where are the walls in the world
    world[0][0] = "#"
    world[1][2] = "#"
    world[1][3] = "#"
    world[1][4] = "#"
    world[2][4] = "#"
    world[2][5] = "#"
    world[2][6] = "#"

    # place exit in the world
    world[0][6] = "E"

    return world

def initialize_robot(world, start_position):
    # place robot in the world
    x = start_position[0]
    y = start_position[1]
    world[x][y] = "+"

    # initialize robot 
    robot = None

    return robot

def go_out_of_the_world(world):
    # list of directions taken, in each position,  to go out of the world
    step_list_taken = []

    # list of directions to be taken, ordered by priority
    available_directions_to_take = ["U", "R", "L", "D"]
    
    # list of places already visited by robot 
    places_already_visited = []

    # get exit position
    exit_x_position, exit_y_position = get_exit_position(world)

    # get current robot position
    current_robot_x_position, current_robot_y_position = get_current_robot_position(world)

    # while robot didn't exit the world, try it
    while (current_robot_x_position != exit_x_position or current_robot_y_position != exit_y_position):
        # from the current place, check what direction should be taken
        next_direction_to_take = get_next_step_to_take(world, available_directions_to_take, places_already_visited)

        # move robot in the world
        move_robot(world, next_direction_to_take, places_already_visited)

        # add direction to the list of steps taken
        step_list_taken.append(next_direction_to_take)

        # get current robot position
        current_robot_x_position, current_robot_y_position = get_current_robot_position(world)

    return step_list_taken

def retrieve_path(startPosition):
    # create world where robo will be placed
    world = create_world()
    
    # initialize robot in the world
    robot = initialize_robot(world, startPosition)
       
    # find a way out of the world
    step_list_taken = go_out_of_the_world(world)
    
    print_world(world)
    print
    print step_list_taken
    return step_list_taken

