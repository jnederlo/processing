
scl = 10
w = 350 #set's the width of the shape.
h = 350 #set's the height of the shape.
cols = w / scl
rows = w / scl

terrain = [[0 for x in range(cols)] for y in range(rows)]

def setup():
    size(800, 800, P3D)
    yOffset = 0
    for y in range(3, rows - 3):
        xOffset = 0
        for x in range(3, cols - 3):
            terrain[x][y] = map(noise(xOffset, yOffset), 0, 1, -30, 30)

            xOffset += 0.15
        yOffset += 0.15
        
def draw():
    background(0)
    stroke(255)
    fill(0, 0, 255, 20)
    translate(400, 450, 0)
    rotateX(PI/3)
    box(400, 400, 100)

    translate(-170, -85, 100)
    # fill(0, 200, 100)
    x,y = 10, 10

    for y in range(rows - 1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            fill(0, 0, random(50, 250))
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl, (y+1)*scl, terrain[x][y+1])
        endShape()