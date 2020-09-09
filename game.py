
# TODO
# COMPLETE - Food to not spawn on top of snake
# COMPLETE - Handler for turning 180 degrees 
# COMPLETE - Trigger eat food as tick enters position instead of on leave
# - Create tick rate progression for difficulty increase
# COMPLETE - Snake to die when boundary hit
# - Display controls down side of scene
# - Display score on death
# - Create menu
# - Snake to spawn randomly with safe padding
# COMPLETE - Add full notes

import os, time, queue, threading, random
from platform import system
from pynput.keyboard import Listener, Key

class Game:
    def __init__(self, height, width, refresh_rate):
        self.height = height
        self.width = width
        self.matrix = []
        self.refresh_rate = refresh_rate
        self.state = 1
        self.snake = Snake([(3,1),(2,1),(1,1)],Snake.DOWN)
        self.food = Food("*", (5, 5))
        self.key_press = queue.LifoQueue()
        self.score = 0

    def run(self):
        # Start listener on to seperate thread to avoid blockin
        # Trigger order: user, tick, render, sleep * refer_rate
        while True:
            threading.Thread(target=self.listen, daemon=True).start()
            self.on_user()
            self.on_tick()
            self.set_scene()
            self.render()
            time.sleep(self.refresh_rate)

    def on_tick(self):
        # Trigger on every tick @ refresh_rate
        # Move snake to new position
        # Check if new position contains food and eat
        # Check is snake had died
        clear_console()
        self.snake.take_step(self.height, self.width)      
        if self.snake.body[0] == self.food.position:
            self.snake.body.insert(0, self.food.position)
            self.food.get_position(self.height, 
                self.width,self.snake.body)
            self.score += 1
        elif self.snake.life == 0:
            exit()
        else:
            pass    

    def on_user(self):
        # Trigger on user input after refresh
        # Check key_press and assign to controls
        if str(self.key_press) == "'w'":
            self.snake.set_direction(Snake.UP)
        elif str(self.key_press) == "'a'":
            self.snake.set_direction(Snake.LEFT)
        elif str(self.key_press) == "'s'":
            self.snake.set_direction(Snake.DOWN)
        elif str(self.key_press) == "'d'":
            self.snake.set_direction(Snake.RIGHT)
        else:
            pass

    def listen(self):
        # Listen for user keyboard input
        def on_press(key):
            self.key_press = key
            
        listener = Listener(on_press=on_press)
        listener.start()

    def set_scene(self):
        # create game area array 
        self.matrix = [
            [
                "-" if y == 0 or y == self.height - 1
                else "|" if x == 0 or x == self.width - 1
                else " " 
                for x 
                in range(self.width)
            ]  
            for y 
            in range(self.height)
        ]
        # Insert snake 
        bIdx = 0
        for _ in self.snake.body:
            self.matrix[self.snake.body[bIdx][0]][self.snake.body[bIdx][1]] = "#"
            bIdx += 1
        # Insert food 
        self.matrix[self.food.position[0]][self.food.position[1]] = self.food.char

        return self.matrix

    def render(self):
        #print scene
        print(f"score: {self.score}")
        for y in range(self.height):
            print(*self.matrix[y])
    
class Snake:
    # SNAKE DIRECTIONS 
    UP = (-1,0)
    DOWN = (1,0)
    RIGHT = (0,1)
    LEFT = (0,-1)

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

def clear_console():
    # Clear console based on OS
    clear = 'cls' if system().lower()=='windows' else 'clear'
    os.system(clear)



Game(20, 30, 0.2).run()
