import random

class Snake:

    # SNAKE DIRECTIONS 
    UP = (-1,0)
    DOWN = (1,0)
    RIGHT = (0,1)
    LEFT = (0,-1)

    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
        self.life = 1
    

    def take_step(self, height, width):
        
        # Calc next position
        next_position = (
            self.body[0][0] + self.direction[0],
            self.body[0][1] + self.direction[1])

        # Check body collision
        if next_position in self.body[:-1]:  # Ignore tail
            self.life = 0

        # Check boarder collision
        elif next_position[1] == 0:
            self.life = 0 
        elif next_position[1] == width - 1:
            self.life = 0
        elif next_position[0] == 0:
            self.life = 0 
        elif next_position[0] == height - 1:
            self.life = 0

        # If no collision pop last body element & insert next position
        else:  
            self.body.pop()
            self.body.insert(0, next_position)


    def set_direction(self, direction):

        # Check new direction isn't 180 reverse
        if self.direction[0] + direction[0] == 0:
            pass

        elif self.direction[1] + direction[1] == 0:
            pass
        
        # Update direction
        else:
            self.direction = direction 

class Food:

    def __init__(self, position):
        self.position = position


    def get_position(self, game_height, game_width, snake_body):

        # Initiate random position loop
        i = 0
        while i == 0:
            self.position = (random.randint(1, game_height - 2),
                random.randint(1, game_width - 2)) 

            # End loop if no conflict with snake body
            if self.position in snake_body:
                i += 1  
            if i > 0:
                i = 0
            else:
                i = 1
