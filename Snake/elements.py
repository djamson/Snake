import random

class Snake:
    # SNAKE DIRECTIONS 
    UP = (-1,0)
    DOWN = (1,0)
    RIGHT = (0,1)
    LEFT = (0,-1)
    '''
    snake_directons = {
        UP, (-1,0)
        DOWN, (1,0)
        RIGHT, (0,1)
        LEFT, (0,-1)
    }
    '''
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
        self.speed = 0.3
        self.life = 1
    
    def take_step(self, height, width):

        next_position = (
            self.body[0][0] + self.direction[0],
            self.body[0][1] + self.direction[1])

        # Check collisions body + borders
        i = 0
        for _ in self.body:
            if self.body[i] == next_position:
                self.life -= 1 
            i += 1 

        if next_position[1] == 0:
            self.life -= 1 
        elif next_position[1] == width - 1:
            self.life -= 1
        elif next_position[0] == 0:
            self.life -= 1 
        elif next_position[0] == height - 1:
            self.life -= 1
        else:
            pass
        # Add last body element to next position    
        self.body.pop()
        self.body.insert(0, next_position)
    
    def set_direction(self, direction):
        # Check direction change isn't 180 then update
        if self.direction[0] + direction[0] == 0:
            pass
        elif self.direction[1] + direction[1] == 0:
            pass
        else:
            self.direction = direction 

class Food:
    def __init__(self, char, position):
        self.char = char
        self.position = position

    def get_position(self, game_height, game_width, ignore):
        # Generate food position and regen if on snak body
        i = 0
        while i == 0:
            self.position = (random.randint(1, game_height - 2),
                random.randint(1, game_width - 2))
            idx = 0
            for _ in ignore:
                if self.position == ignore[idx]:
                   i = +1  
                idx += 1
            if i > 0:
                i = 0
            else:
                i = 1