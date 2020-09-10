
class Menu_matrix():

    def __init__(self):
        self.height = 20
        self.width = 30

    def draw(self):
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

class Game_matrix():

    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def draw(self):
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
        #bIdx = 0
        #for _ in self.snake.body:
        #    self.matrix[self.snake.body[bIdx][0]][self.snake.body[bIdx][1]] = "#"
        #    bIdx += 1
        # Insert food 
        #self.matrix[self.food.position[0]][self.food.position[1]] = self.food.char

        return self.matrix