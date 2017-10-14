
# EXAMPLE 1

# def setup():
#     size(200, 200, P3D)
#     # global x = width/2
#     # global y = height/2

# z = 0

# def draw():
#     x = width/2
#     y = height/2
#     translate(x, y, z)
#     rectMode(CENTER)
#     rect(0, 0, 100, 100)
#     global z
#     z += 1

# EXAMPLE 2

# size(200, 200, P3D)
# background(100)
# rectMode(CENTER)
# fill(51)
# stroke(255)

# translate(100, 100, 0)
# rotateZ(PI/8)
# rotateX(PI/8)
# rotateY(PI/8)
# rotateZ(PI/8)
# print(PI)
# rect(0, 0, 100, 100)

# EXAMPLE 3

size(640, 360, P3D)
background(0)
lights()

pushMatrix()
translate(130, height/2, 0)
rotateY(1.25)
rotateX(-0.4)
noStroke()
box(100)
popMatrix()

pushMatrix()
translate(500, height*0.35, -200)
noFill()
stroke(255)
sphere(280)
popMatrix()