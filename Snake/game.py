
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

import elements as el
import kbpoller as kb
import os, time, queue, threading
from platform import system

class Game:
    def __init__(self, height, width, refresh_rate):
        self.height = height
        self.width = width
        self.matrix = []
        self.refresh_rate = refresh_rate
        self.state = 1
        self.snake = el.Snake([(3,1),(2,1),(1,1)],el.Snake.DOWN)
        self.food = el.Food("*", (5, 5))
        self.key_press = queue.LifoQueue()
        self.score = 0

    def run(self):
        # Start listener on to seperate thread to avoid blockin
        # Trigger order: user, tick, render, sleep * refer_rate
        threading.Thread(target=kb.listen, daemon=True).start()
        while True:
            #threading.Thread(target=kb.listen, daemon=True).start()
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

        if str(kb.key) == 'w':
            self.snake.set_direction(el.Snake.UP)
        elif str(kb.key) == 'a':
            self.snake.set_direction(el.Snake.LEFT)
        elif str(kb.key) == 's':
            self.snake.set_direction(el.Snake.DOWN)
        elif str(kb.key) == 'd':
            self.snake.set_direction(el.Snake.RIGHT)
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
    

def clear_console():
    # Clear console based on OS
    clear = 'cls' if system().lower()=='windows' else 'clear'
    os.system(clear)


Game(20, 30, 0.2).run()
