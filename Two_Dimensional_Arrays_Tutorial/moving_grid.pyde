
cols = 10
rows = 10

grid = [[0 for x in range(cols)] for y in range(rows)]

def setup():
    size(200, 200)
    for i in range(cols):
        for j in range(rows):
            grid[i][j] = Cell(i*20, j*20, 20, 20, i+j)
        
def draw():
    background(0)
    for i in range(cols):
        for j in range(rows):
            grid[i][j].oscillate()
            grid[i][j].display()
            
class Cell():
    def __init__(self,  tempX, tempY, tempW, tempH, tempAngle):
        self.x= tempX
        self.y = tempY
        self.w = tempW
        self.h = tempH
        self.angle = tempAngle
        
    def oscillate(self):
        self.angle += 0.02
        
    def display(self):
        stroke(255)
        fill(127+127*sin(self.angle))
        rect(self.x, self.y, self.w, self.h)
        