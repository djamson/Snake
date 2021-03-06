'''
TODO
COMPLETE - Food to not spawn on top of snake
COMPLETE - Handler for turning 180 degrees 
COMPLETE - Trigger eat food as tick enters position instead of on leave
- Create tick rate progression for difficulty increase
COMPLETE - Snake to die when boundary hit
- Display controls down side of scene
- Display score on death
- Create menu
- Snake to spawn randomly with safe padding
COMPLETE - Add full notes
'''

import elements as el
import kbpoller as kb
import os, time, queue, threading
from platform import system

class Game:

    def __init__(self, height, width, refresh_rate, difficulty):
        self.height = height
        self.width = width
        self.refresh_rate = refresh_rate
        self.snake = el.Snake([(3,1),(2,1),(1,1)],el.Snake.DOWN)
        self.food = el.Food((5, 5))
        self.score = 0
        self.difficulty = difficulty


    def run(self):

        # Start listener new thread to avoid blocking
        threading.Thread(target=kb.listen, daemon=True).start()

        # Game loop
        while True:
            tic = time.perf_counter()
            self.on_user()
            self.on_tick()
            self.set_matrix()
            self.render()
            toc = time.perf_counter()
            tElapsed = toc - tic
            time.sleep(self.refresh_rate - tElapsed)


    def on_tick(self):

        self.snake.take_step(self.height, self.width)   

        # Check if new position contains food and eat
        if self.snake.body[0] == self.food.position:

            self.snake.body.insert(0, self.food.position)
            self.food.get_position(self.height, self.width,self.snake.body)
            self.score += 1

        elif self.snake.life == 0:

            exit()


    def on_user(self):

        # Set controls
        if str(kb.key) == 'w':
            self.snake.set_direction(el.Snake.UP)
        elif str(kb.key) == 'a':
            self.snake.set_direction(el.Snake.LEFT)
        elif str(kb.key) == 's':
            self.snake.set_direction(el.Snake.DOWN)
        elif str(kb.key) == 'd':
            self.snake.set_direction(el.Snake.RIGHT)


    def set_matrix(self):

        # Create game matrix
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
        i = 0
        for _ in self.snake.body:
            self.matrix[self.snake.body[i][0]][self.snake.body[i][1]] = "#"
            i += 1

        # Insert food
            self.matrix[self.food.position[0]][self.food.position[1]] = "*"


    def render(self):

        print(f"SCORE: {self.score}")

        # Print matrix row by row
        for y in range(self.height):
            print(*self.matrix[y])
    

def clear_console():

    # Clear console based on OS
    clear = 'cls' if system().lower()=='windows' else 'clear'
    os.system(clear)

clear_console()
Game(20, 30, 0.2, "normal").run()

